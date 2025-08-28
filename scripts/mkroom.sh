#!/usr/bin/env bash
# Helper to scaffold a new lab folder.
# Usage: ./scripts/mkroom.sh THM FakeBank

set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: $0 <Category: THM|HTB|LocalLab> <RoomName>"
  exit 1
fi

CAT="$1"
ROOM="$2"
ROOT="$(cd "$(dirname "$0")"/.. && pwd)"
DEST="$ROOT/labs/$CAT/$ROOM"

mkdir -p "$DEST"

# Copy templates if available
cp "$ROOT/templates/pentest-report-template.md" "$DEST/report.md"
cp "$ROOT/templates/note-template.md" "$DEST/notes.md"

echo "# $CAT/$ROOM created at $DEST"
echo "Next: edit $DEST/report.md with your findings and add concise evidence."
