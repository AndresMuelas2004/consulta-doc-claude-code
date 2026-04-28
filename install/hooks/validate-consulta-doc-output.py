"""
SubagentStop hook for the `consulta-doc-claude-code` skill.

Non-deterministic self-review hook. Unlike a prefix validator, this hook
does NOT inspect the content of `last_assistant_message`. Instead, it
always blocks the first stop with a generic `reason` that forces the
subagent to self-review its choice of mode (step 8.A vs 8.B) and the
corresponding meta-phrase (step 9.A vs 9.B) before closing.

The LLM itself decides, on the retry, whether its previous final message
was already correct (in which case it reemits it unchanged) or whether
it needs to be corrected (wrong variant, pasted content, missing path
substitution, mixed variants, etc.).

Anti-loop: if the hook already fired once (stop_hook_active=true), it
lets the second stop pass through unchanged so we never enter an
infinite block loop. Worst case we accept an imperfect final message.
"""

from __future__ import annotations

import json
import sys

# Ensure stdout carries UTF-8 on Windows (default is cp1252 and would
# mangle accented characters in `reason`).
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


SELF_REVIEW_REASON = (
    "Antes de dar por buena tu respuesta final, haz una auto-revision rapida en dos puntos: "
    "(1) Clasificacion: revisa el paso 8 de SKILL.md y confirma si la consulta actual corresponde "
    "al modo DUDA (8.A) o al modo INFO-TAREA (8.B), aplicando las reglas sintacticas duras del paso 8. "
    "(2) revisa el paso 9 y confirma que tu mensaje final actual es EXACTAMENTE la "
    "variante que corresponde al modo elegido: variante 9.A si es DUDA, variante 9.B si es "
    "INFO-TAREA. Una sola variante, literal, sin caracteres extra antes o despues, sin envolver "
    "entre comillas ni backticks, sin traducir, sin abreviar, con <RUTA-ABSOLUTA-TEMPLATE> "
    "sustituido por la ruta real al template_<session_id>.md de la skill. "
    "Si detectas que elegiste el modo equivocado, que pegaste contenido tecnico en el mensaje, "
    "que mezclaste trozos de ambas variantes o que olvidaste sustituir la ruta, reemite ahora tu "
    "respuesta final corrigiendolo. Si tu respuesta anterior ya era correcta, reemite exactamente "
    "la misma frase sin cambios. "
    "¡ASEGURATE DE RESPETAR LA RESPUESTA LITERAL DE LA VARIANTE ESCOGIDA, NO INVENTES NI "
    "AÑADAS NADA; PON LA FRASE LITERAL!"
)


def main() -> None:
    try:
        payload = json.loads(sys.stdin.read())
    except Exception:
        # If we cannot parse the input, let the stop proceed.
        sys.exit(0)

    # Anti-loop: only force a review once. If we already blocked, accept
    # whatever the subagent produced on the retry, even if still imperfect.
    if payload.get("stop_hook_active"):
        sys.exit(0)

    # Always block the first stop with the self-review reason. The LLM
    # decides on the retry whether its previous message was already right
    # or needs correction.
    print(json.dumps({"decision": "block", "reason": SELF_REVIEW_REASON}))
    sys.exit(0)


if __name__ == "__main__":
    main()
