"""Stop / SessionEnd hook: borra el template de la sesion actual.

Lee el JSON del payload por stdin, extrae el `session_id` (campo universal
presente en todos los eventos de hook) y elimina
~/.claude/skills/consulta-doc-claude-code/template_<session_id>.md
si existe. Idempotente y silencioso: cualquier error se traga y devuelve 0.

Forma parte del trio de hooks (Stop + SessionEnd + SessionStart) que
garantizan que ningun template_*.md quede huerfano en el directorio de
la skill, evitando colisiones entre sesiones concurrentes y commits
sucios al repo publico.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    try:
        payload = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)

    session_id = payload.get("session_id")
    if not session_id:
        sys.exit(0)

    target = (
        Path.home()
        / ".claude"
        / "skills"
        / "consulta-doc-claude-code"
        / f"template_{session_id}.md"
    )

    try:
        target.unlink(missing_ok=True)
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
