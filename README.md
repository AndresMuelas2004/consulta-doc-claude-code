# consulta-doc-claude-code

Skill personal para Claude Code que resuelve dudas o reúne información preparatoria sobre cualquier feature de Claude Code consultando **siempre** la [documentación oficial](https://code.claude.com/docs) en lugar del conocimiento de entrenamiento del modelo. Pensada como contramedida al ritmo de cambios semanales del producto, donde un modelo respondiendo "de memoria" puede mencionar flags o campos que ya no existen.

## Cómo funciona

La skill corre en un subagente forkeado (`context: fork` + `agent: consulta-doc-agent`) que:

1. Lee `reference.md`, un catálogo curado de URLs de `code.claude.com/docs` con descripciones específicas.
2. Lanza una `WebSearch` con `site:code.claude.com/docs` para detectar páginas nuevas no catalogadas.
3. Visita las URLs relevantes con `WebFetch`.
4. Auto-actualiza `reference.md` (añade URLs nuevas, elimina las rotas).
5. Clasifica la consulta en uno de dos modos:
   - **DUDA**: la consulta es una pregunta que espera respuesta. La skill redacta la respuesta y la deja en `template_<session_id>.md`.
   - **INFO-TAREA**: la consulta es preparatoria para una tarea posterior. La skill deja material crudo en `template_<session_id>.md` para que la sesión principal continúe.
6. Devuelve a la sesión principal una "frase meta" con la ruta absoluta del template para que se imprima al usuario o se use como contexto interno.

## El agent custom (`consulta-doc-agent`)

La skill no podría correr sin el agent custom que ejecuta el fork. Este es el archivo completo, tal y como vive en [`install/agents/consulta-doc-agent.md`](./install/agents/consulta-doc-agent.md) y debe instalarse en `~/.claude/agents/consulta-doc-agent.md`:

```yaml
---
name: consulta-doc-agent
description: NUNCA EJECUTAR. Uso interno exclusivo de la skill consulta-doc-claude-code.
tools: Read, Write, Edit, WebFetch, WebSearch, Grep, Glob
model: claude-sonnet-4-6
hooks:
  SubagentStop:
    - hooks:
        - type: command
          command: python $HOME/.claude/hooks/validate-consulta-doc-output.py
---
```

Detalle de cada campo:

| Campo | Por qué está ahí |
|---|---|
| `name: consulta-doc-agent` | Identificador del agent. Debe coincidir con el `agent:` que aparece en el frontmatter de `SKILL.md`. |
| `description: NUNCA EJECUTAR…` | Marca este agent como uso interno de la skill. Evita que el modelo principal lo invoque por su cuenta como si fuera un agent reutilizable. |
| `tools` | Conjunto mínimo necesario para que el subagente lea/escriba archivos, edite el `reference.md` y consulte la doc oficial vía web. |
| `model: claude-sonnet-4-6` | El subagente corre con un modelo más barato y rápido que Opus. Suficiente porque la tarea es de extracción/resumen guiada por un playbook muy estructurado. |
| `hooks.SubagentStop` | Hook de ciclo de vida del agent: dispara `validate-consulta-doc-output.py` cuando el subagente intenta cerrar. El script bloquea el primer cierre con un `decision: "block"` y un `reason` que fuerza al subagente a auto-revisar la elección de modo (8.A vs 8.B) y la frase meta del paso 9 antes de salir. Anti-loop: solo bloquea una vez. |

El path `python $HOME/.claude/hooks/validate-consulta-doc-output.py` se expande en bash (Linux, macOS, Git Bash sobre Windows). Si tu Claude Code corre los hooks en PowerShell nativa, sustituye `$HOME` por la ruta absoluta de tu home.

## Invocación

Manualmente con argumento obligatorio:

```
/consulta-doc-claude-code <duda concreta o petición de información>
```

Ejemplos:

```
/consulta-doc-claude-code ¿Qué es un output style?
/consulta-doc-claude-code Lee la doc de skills porque voy a crear una nueva mañana
```

También se invoca automáticamente por el modelo principal cuando detecta que tu petición toca cualquier aspecto de Claude Code y necesita verificar la información antes de actuar.

## Estructura del repo

```
consulta-doc-claude-code/
├── README.md                           ← este archivo (overview y entrypoint)
├── INSTALL.md                          ← guía de instalación (LEER ANTES DE USAR)
├── SKILL.md                            ← playbook que el modelo ejecuta (interno)
├── reference.md                        ← catálogo auto-actualizable de URLs oficiales
├── evals/evals.json                    ← casos de prueba
├── .gitignore                          ← ignora template_*.md (huérfanos por sesión)
└── install/                            ← payload que va a ~/.claude/ tras instalación
    ├── agents/consulta-doc-agent.md    ← agent custom requerido
    └── hooks/
        ├── cleanup-consulta-doc-template.py    (Stop + SessionEnd)
        ├── sweep-consulta-doc-templates.py     (SessionStart)
        └── validate-consulta-doc-output.py     (SubagentStop del agent)
```

## Instalación

**La skill no funciona con sólo clonar el repo.** Necesita un agent custom, tres hooks Python y un bloque de configuración en `~/.claude/settings.json` que viven fuera del directorio de la skill.

→ Sigue las instrucciones de [INSTALL.md](./INSTALL.md). Hay opción de instalación manual paso a paso o automatizada con un solo prompt a Claude Code.

## Por qué tantas dependencias externas

- **El agent custom** es necesario porque la skill se ejecuta en un subagente con contexto aislado del hilo principal, y Claude Code no permite declarar agents inline desde el `SKILL.md`.
- **El hook validator** (SubagentStop, declarado dentro del agent) fuerza una auto-revisión antes de que el subagente cierre, para evitar que emita la frase meta del modo equivocado o filtre contenido del dossier al chat principal.
- **Los hooks cleanup y sweep** son necesarios porque cada sesión escribe su propio `template_<session_id>.md` (para evitar colisiones entre sesiones simultáneas) y alguien tiene que limpiar tras la lectura.

## Notas

- **Autoactualización del catálogo**: cada invocación puede modificar `reference.md`. Es comportamiento esperado.
- **Skill personal**: no probada como plugin namespacado.
- **Dependencias del entorno**: Python 3 disponible (los hooks son scripts Python, sin librerías externas), Claude Code instalado.
