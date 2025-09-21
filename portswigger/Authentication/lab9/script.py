// Fuzzer HTTP Processor — Macro de login previa a cada payload
// Flujo: GET /login -> POST /login -> GET /login2 -> actualiza el POST /login2 (cookies + CSRF2)

var count = 1;

// === Helpers ===
function buildMsgFrom(message, path, method) {
    var reqHeader = message.getRequestHeader();
    var host = reqHeader.getHostName();
    var port = reqHeader.getHostPort();
    var isHttps = reqHeader.isSecure();

    var URI = new org.apache.commons.httpclient.URI(
        (isHttps ? "https" : "http") + "://" + host + (port ? ":" + port : "") + path, true
    );
    var msg = new org.parosproxy.paros.network.HttpMessage();
    msg.setRequestHeader(method + " " + URI.getEscapedURI() + " HTTP/1.1");
    msg.getRequestHeader().setHeader(
        "Host",
        host + (port && port !== (isHttps ? 443 : 80) ? ":" + port : "")
    );
    return msg;
}

function extractHidden(body, namesCsv) {
    if (!body) return null;
    var names = (namesCsv || "").split(",").map(function(s){ return s.trim(); }).filter(Boolean);
    // añade defaults comunes por si te olvidas
    if (names.length === 0) names = ["csrf","csrf_token","__RequestVerificationToken","authenticity_token","token"];
    for (var i=0;i<names.length;i++) {
        var n = names[i];
        var re = new RegExp('name=["\\\']'+n+'["\\\']\\s+value=["\\\']([^"\\\']+)["\\\']','i');
        var m = body.match(re);
        if (m) return {name:n, value:m[1]};
    }
    return null;
}

function setFormParam(bodyStr, name, value) {
    if (!name) return bodyStr || "";
    var encName = encodeURIComponent(name);
    var encVal  = encodeURIComponent(value);
    if (!bodyStr || bodyStr.length === 0) return encName + "=" + encVal;

    // reemplaza si existe
    var re = new RegExp('(^|&)' + name.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\$&') + '=([^&]*)','i');
    if (re.test(bodyStr)) {
        return bodyStr.replace(re, function(_, p1){ return p1 + name + "=" + encVal; });
    }
    // si no, añade al final
    return bodyStr + "&" + encName + "=" + encVal;
}

// === Processor principal ===
function processMessage(utils, message) {
    var params = utils.getParameters(); // del diálogo "Add Message Processor"
    // Requeridos (ponlos tal cual en el diálogo)
    var loginPath      = params.get("loginPath");      // ej: /login
    var login2Path     = params.get("login2Path");     // ej: /login2
    var userParam      = params.get("userParam");      // ej: username
    var passParam      = params.get("passParam");      // ej: password
    var usernameValue  = params.get("username");       // ej: carlos
    var passwordValue  = params.get("password");       // ej: s3cret

    // Opcionales
    var csrf1Names     = params.get("csrf1Names");     // ej: csrf,csrf_token
    var csrf2Names     = params.get("csrf2Names");     // ej: csrf,csrf_token
    var addReferer     = params.get("addReferer");     // "true"/"false"
    var refererLogin   = params.get("refererLogin");   // ej: /login (se antepone host)

    // 1) GET /login
    var m1 = buildMsgFrom(message, loginPath, "GET");
    utils.sendMessage(m1, true); // seguir redirecciones
    var body1 = m1.getResponseBody().toString();
    var csrf1 = extractHidden(body1, csrf1Names);

    // 2) POST /login (user+pass [+csrf1])
    var m2 = buildMsgFrom(message, loginPath, "POST");
    m2.getRequestHeader().setHeader("Content-Type", "application/x-www-form-urlencoded");
    if (addReferer && refererLogin && refererLogin.length>0) {
        var base = message.getRequestHeader().getURI().toString();
        var idx = base.indexOf("://");
        var schemeHost = base.substring(0, base.indexOf("/", idx+3));
        m2.getRequestHeader().setHeader("Referer", schemeHost + refererLogin);
    }
    var loginBody = encodeURIComponent(userParam) + "=" + encodeURIComponent(usernameValue) +
                    "&" + encodeURIComponent(passParam) + "=" + encodeURIComponent(passwordValue);
    if (csrf1) loginBody = setFormParam(loginBody, csrf1.name, csrf1.value);

    m2.setRequestBody(loginBody);
    m2.getRequestHeader().setContentLength(m2.getRequestBody().length());
    utils.sendMessage(m2, true);

    // 3) GET /login2 (extraer CSRF2/token secundario)
    var m3 = buildMsgFrom(message, login2Path, "GET");
    utils.sendMessage(m3, true);
    var body3 = m3.getResponseBody().toString();
    var csrf2 = extractHidden(body3, csrf2Names);

    // 4) Preparar el POST /login2 que se va a enviar (message):
    //    - Limpiar Cookie para que ZAP ponga el jar actual
    //    - Asegurar Content-Type
    //    - Inyectar/actualizar CSRF2 (si existe)
    message.getRequestHeader().setHeader("Cookie", null);
    if (!/application\/x-www-form-urlencoded/i.test(message.getRequestHeader().getHeader("Content-Type")||"")) {
        message.getRequestHeader().setHeader("Content-Type", "application/x-www-form-urlencoded");
    }

    var reqBody = message.getRequestBody().toString();
    if (csrf2) {
        reqBody = setFormParam(reqBody, csrf2.name, csrf2.value);
    }
    message.setRequestBody(reqBody);
    message.getRequestHeader().setContentLength(message.getRequestBody().length());

    // (Opcional) marca única por depuración
    message.getRequestHeader().setHeader("X-Macro-Step", String(count++));
    return true; // continuar con el envío del payload al servidor
}

function processResult(utils, fuzzResult){
    // Marca éxito si hay 302 o texto típico de sesión válida
    var msg  = fuzzResult.getHttpMessage();
    var code = msg.getResponseHeader().getStatusCode();
    var body = msg.getResponseBody().toString();
    if (code === 302 || /Welcome|Mi cuenta|Logout|Log out/i.test(body)) {
        fuzzResult.addCustomState("Success","Possible");
    }
    return true; // mostrar el resultado
}

// === Parámetros configurables en el diálogo ===
function getRequiredParamsNames(){
    return [
        "https://0a7b009c04f4518e80b02151006200ac.web-security-academy.net/login",   // /login
        "https://0a7b009c04f4518e80b02151006200ac.web-security-academy.net/login2",  // /login2
        "carlos",   // username
        "montoya",   // password
        "username",    // carlos
        "password"     // s3cret
    ];
}
function getOptionalParamsNames(){
    return [
        "csrf1Names",  // ej: csrf,csrf_token
        "csrf2Names",  // ej: csrf,csrf_token
        "addReferer",  // true/false
        "refererLogin" // ej: /login
    ];
}
