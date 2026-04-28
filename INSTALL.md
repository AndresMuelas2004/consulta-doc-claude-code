# Instalación de `consulta-doc-claude-code`

Esta skill no funciona con sólo clonar el repo: necesita **un agent custom**, **tres hooks Python** y **un bloque de configuración en `~/.claude/settings.json`** que viven fuera del directorio de la skill. Esos artefactos van empaquetados en la carpeta [`install/`](./install/) de este mismo repo.

## Por qué hacen falta esos archivos externos

| Archivo | Para qué sirve |
|---|---|
| `install/agents/consulta-doc-agent.md` | Agent custom que la skill invoca con `context: fork; agent: consulta-doc-agent`. Sin él, la skill no puede correr en su subagente aislado. |
| `install/hooks/validate-consulta-doc-output.py` | Hook `SubagentStop` declarado en el agent: fuerza una auto-revisión del subagente antes de cerrar para evitar emitir la frase meta del modo equivocado. |
| `install/hooks/cleanup-consulta-doc-template.py` | Hook `Stop` y `SessionEnd`: borra el `template_<session_id>.md` propio de la sesión cuando termina el turno o la sesión. |
| `install/hooks/sweep-consulta-doc-templates.py` | Hook `SessionStart`: barre `template_*.md` huérfanos al arrancar (sesiones anteriores que crashearon), preservando el de la sesión actual. |
| Bloque de hooks en `~/.claude/settings.json` | Registra los tres hooks de cleanup/sweep en los eventos correspondientes. |

> Sin la pieza de cleanup, dos sesiones simultáneas que invoquen la skill se machacarían el `template.md` mutuamente. Con ella, cada sesión escribe en su propio `template_<session_id>.md` y los hooks se encargan de limpiarlo.

---

## Opción A — Instalación en una línea con Claude Code

Abre Claude Code en cualquier directorio y pega esto (sin argumentos):

> Lee `~/.claude/skills/consulta-doc-claude-code/INSTALL.md` y configura la skill por mí siguiendo la sección "Instalación manual paso a paso". Copia los archivos del directorio `install/` a sus rutas finales en `~/.claude/`, fusiona el bloque JSON de hooks con `~/.claude/settings.json` sin pisar mis hooks existentes, y verifica que todo está en su sitio.

Claude Code interpretará esta instrucción, leerá los `.py` y `.md` del directorio `install/`, los copiará a `~/.claude/hooks/` y `~/.claude/agents/`, y fusionará el bloque de hooks con tu `settings.json` respetando lo que ya tengas.

Tras la instalación, **reinicia Claude Code** para que detecte el nuevo agent y los hooks de `SessionStart`.

---

## Opción B — Instalación manual paso a paso

### 1. Copia los hooks Python

Copia los tres archivos de `install/hooks/` a `~/.claude/hooks/`:

```bash
cp install/hooks/cleanup-consulta-doc-template.py    ~/.claude/hooks/
cp install/hooks/sweep-consulta-doc-templates.py     ~/.claude/hooks/
cp install/hooks/validate-consulta-doc-output.py     ~/.claude/hooks/
```

(En Windows con Git Bash funcionan estos mismos comandos. En PowerShell nativa: `Copy-Item install\hooks\*.py $HOME\.claude\hooks\`.)

### 2. Copia el agent custom

```bash
cp install/agents/consulta-doc-agent.md ~/.claude/agents/
```

> El comando del hook dentro del agent usa `$HOME/.claude/hooks/validate-consulta-doc-output.py`. Esto se expande correctamente en bash (Linux, macOS, Git Bash sobre Windows). Si tu Claude Code corre los hooks en PowerShell nativa, sustituye `$HOME` por la ruta absoluta de tu home.

### 3. Fusiona los hooks en `~/.claude/settings.json`

Abre `~/.claude/settings.json` y añade los tres bloques siguientes dentro del objeto `"hooks"`. Si ya tienes hooks definidos para `Stop` (lo más probable), **añade el nuevo entry al array existente, no lo reemplaces**. `SessionStart` y `SessionEnd` normalmente serán claves nuevas.

**Bloque a fusionar** (sustituye `<PYTHON-EXE>` por el comando que invoque tu Python 3.x — en Windows típicamente la ruta absoluta a `python.exe`; en Linux/macOS basta con `python3`):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "<PYTHON-EXE> /ABSOLUTE/PATH/TO/.claude/hooks/cleanup-consulta-doc-template.py",
            "timeout": 10
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "<PYTHON-EXE> /ABSOLUTE/PATH/TO/.claude/hooks/sweep-consulta-doc-templates.py",
            "timeout": 10
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "<PYTHON-EXE> /ABSOLUTE/PATH/TO/.claude/hooks/cleanup-consulta-doc-template.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

Ejemplo concreto para Windows con Python 3.12:

```json
"command": "C:/Users/<TU-USUARIO>/AppData/Local/Programs/Python/Python312/python.exe C:/Users/<TU-USUARIO>/.claude/hooks/cleanup-consulta-doc-template.py"
```

Ejemplo para Linux/macOS:

```json
"command": "python3 /home/<TU-USUARIO>/.claude/hooks/cleanup-consulta-doc-template.py"
```

### 4. Reinicia Claude Code

Cierra y vuelve a abrir Claude Code para que detecte el nuevo agent. Los hooks de `Stop`, `SessionStart` y `SessionEnd` recién declarados también se leen al arrancar.

### 5. Verifica

Dentro de cualquier sesión de Claude Code, invoca la skill con una pregunta corta:

```
/consulta-doc-claude-code ¿Qué es un output style?
```

Deberías ver:

1. Una "frase meta" que apunta a un archivo `template_<UUID>.md` en `~/.claude/skills/consulta-doc-claude-code/`.
2. La respuesta a la pregunta cuando Claude lea ese archivo.
3. Tras terminar el turno, el archivo `template_<UUID>.md` desaparece (lo borra el `Stop` hook).

Si los tres puntos se cumplen, la skill funciona correctamente.

---

## Desinstalación

1. Elimina los tres `.py` de `~/.claude/hooks/`.
2. Elimina `~/.claude/agents/consulta-doc-agent.md`.
3. Quita los entries que añadiste al `Stop`, `SessionStart` y `SessionEnd` en `~/.claude/settings.json`.
4. Borra el directorio de la skill: `~/.claude/skills/consulta-doc-claude-code/`.

---

## Notas

- **Precedencia de versiones**: si modifico los hooks o el agent en `~/.claude/`, las copias en este `install/` pueden quedar desactualizadas. Cuando hago una mejora a la skill, sincronizo manualmente las copias antes de commitear. Si detectas divergencia, los archivos de `~/.claude/` son la fuente de verdad.
- **Aislamiento por sesión**: el diseño se basa en el campo universal `session_id` que reciben los hooks por stdin (igual valor que `${CLAUDE_SESSION_ID}` dentro de la skill). Si Claude Code cambia el comportamiento en futuras versiones, los hooks pueden necesitar adaptación.
- **Sólo skill personal**: no probado como plugin namespacado.
