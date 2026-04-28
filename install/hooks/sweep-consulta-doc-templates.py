"""SessionStart hook: barre huerfanos de template_*.md en la skill.

Borra todos los template_*.md del directorio de la skill
consulta-doc-claude-code EXCEPTO el de la sesion que arranca ahora
(opcion A del diseno: barrido conservador). Cubre el caso de sesiones
anteriores que crashearon sin que se disparara el Stop ni el SessionEnd
y dejaron archivos huerfanos en disco.

La preservacion del template_<session_id_actual>.md evita colisionar con
una hipotetica sesion concurrente que estuviera en la ventana Write->Read
justo cuando esta sesion arranca: la nueva sesion solo puede coincidir
en nombre si comparten session_id, lo cual no ocurre en la practica.
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
    skill_dir = (
        Path.home() / ".claude" / "skills" / "consulta-doc-claude-code"
    )

    if not skill_dir.is_dir():
        sys.exit(0)

    own_filename = f"template_{session_id}.md" if session_id else None

    for f in skill_dir.glob("template_*.md"):
        if own_filename and f.name == own_filename:
            continue
        try:
            f.unlink(missing_ok=True)
        except Exception:
            pass

    sys.exit(0)


if __name__ == "__main__":
    main()
