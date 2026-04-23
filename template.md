<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->

Material preparatorio de la documentación oficial de Claude Code para la tarea pendiente de la sesión principal: diseñar una skill user-invocable en español que reciba una descripción de idea de negocio, haga rondas de AskUserQuestion multi-choice para cubrir 10 puntos y genere un .md por punto en una carpeta con el nombre de la idea.

> Nota: esto es todo lo que la sesión principal tendrá del contenido de la doc; los WebFetch del subagente ya no están disponibles al cerrarse el fork. Úsalo como dossier de referencia antes de escribir la skill.

## Material extraído

### Extend Claude with skills (página principal de Skills) — https://code.claude.com/docs/en/skills

**Concepto general**
- Una skill es un directorio con un `SKILL.md` dentro. Claude la añade a su toolkit y puede invocarla automáticamente cuando sea relevante, o el usuario puede invocarla con `/skill-name`.
- `SKILL.md` tiene dos partes: **frontmatter YAML** entre `---` y el **cuerpo markdown** con las instrucciones que Claude sigue cuando la skill se invoca.
- "Custom commands have been merged into skills." Un archivo en `.claude/commands/deploy.md` y una skill en `.claude/skills/deploy/SKILL.md` crean ambos `/deploy` y funcionan igual. El formato skill es el recomendado hoy.
- Las skills siguen el open standard [Agent Skills](https://agentskills.io). Claude Code añade invocation control, subagent execution (`context: fork`) e inyección dinámica de contexto.

**Ubicaciones y precedencia** (tabla literal "Where skills live")

| Location   | Path                                                | Applies to                     |
| :--------- | :-------------------------------------------------- | :----------------------------- |
| Enterprise | See managed settings                                | All users in your organization |
| Personal   | `~/.claude/skills/<skill-name>/SKILL.md`            | All your projects              |
| Project    | `.claude/skills/<skill-name>/SKILL.md`              | This project only              |
| Plugin     | `<plugin>/skills/<skill-name>/SKILL.md`             | Where plugin is enabled        |

- **Para alcance global (válido en todos los proyectos del usuario): `~/.claude/skills/<skill-name>/SKILL.md`.**
- Cuando hay colisión de nombres: enterprise > personal > project. Plugin skills viven en namespace `plugin-name:skill-name`.
- Si existe skill y comando con el mismo nombre, **la skill tiene precedencia**.
- Claude Code vigila directorios de skills y detecta cambios en vivo (añadir/editar/quitar `SKILL.md` bajo `~/.claude/skills/` o el project `.claude/skills/` surte efecto sin reiniciar). Si se crea por primera vez un directorio top-level de skills durante la sesión, hay que reiniciar para que empiece a vigilarlo.

**Estructura de directorio de una skill**

```text
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output showing expected format
└── scripts/
    └── validate.sh    # Script Claude can execute
```

Solo `SKILL.md` es obligatorio. El resto son archivos de apoyo que se cargan solo cuando la skill los necesita (mantener `SKILL.md` bajo 500 líneas, mover reference material a archivos separados).

**Ejemplo básico Getting Started** (skill `explain-code`)

```bash
mkdir -p ~/.claude/skills/explain-code
```

Contenido de `~/.claude/skills/explain-code/SKILL.md`:

```yaml
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works, teaching about a codebase, or when the user asks "how does this work?"
---

When explaining code, always include:

1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow, structure, or relationships
3. **Walk through the code**: Explain step-by-step what happens
4. **Highlight a gotcha**: What's a common mistake or misconception?

Keep explanations conversational. For complex concepts, use multiple analogies.
```

**Frontmatter reference (tabla literal completa — TODOS los campos del frontmatter)**

Ejemplo de frontmatter con varios campos:

```yaml
---
name: my-skill
description: What this skill does
disable-model-invocation: true
allowed-tools: Read Grep
---

Your skill instructions here...
```

"All fields are optional. Only `description` is recommended so Claude knows when to use the skill."

| Field                      | Required    | Description                                                                                                                                                                                                                                                                                                         |
| :------------------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`                     | No          | Display name for the skill. If omitted, uses the directory name. Lowercase letters, numbers, and hyphens only (max 64 characters).                                                                                                                                                                                  |
| `description`              | Recommended | What the skill does and when to use it. Claude uses this to decide when to apply the skill. If omitted, uses the first paragraph of markdown content. Front-load the key use case: the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage. |
| `when_to_use`              | No          | Additional context for when Claude should invoke the skill, such as trigger phrases or example requests. Appended to `description` in the skill listing and counts toward the 1,536-character cap.                                                                                                                  |
| `argument-hint`            | No          | Hint shown during autocomplete to indicate expected arguments. Example: `[issue-number]` or `[filename] [format]`.                                                                                                                                                                                                  |
| `arguments`                | No          | Named positional arguments for `$name` substitution in the skill content. Accepts a space-separated string or a YAML list. Names map to argument positions in order.                                                                                                                                                |
| `disable-model-invocation` | No          | Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`. Also prevents the skill from being preloaded into subagents. Default: `false`.                                                                                                  |
| `user-invocable`           | No          | Set to `false` to hide from the `/` menu. Use for background knowledge users shouldn't invoke directly. Default: `true`.                                                                                                                                                                                            |
| `allowed-tools`            | No          | Tools Claude can use without asking permission when this skill is active. Accepts a space-separated string or a YAML list.                                                                                                                                                                                          |
| `model`                    | No          | Model to use when this skill is active. Override applies for the rest of the current turn; session model resumes on next prompt. Accepts same values as `/model`, or `inherit`.                                                                                                                                     |
| `effort`                   | No          | Effort level when skill is active. Overrides session effort. Options: `low`, `medium`, `high`, `xhigh`, `max`.                                                                                                                                                                                                      |
| `context`                  | No          | Set to `fork` to run in a forked subagent context.                                                                                                                                                                                                                                                                  |
| `agent`                    | No          | Which subagent type to use when `context: fork` is set.                                                                                                                                                                                                                                                             |
| `hooks`                    | No          | Hooks scoped to this skill's lifecycle. See Hooks in skills and agents.                                                                                                                                                                                                                                             |
| `paths`                    | No          | Glob patterns that limit when this skill is activated. Accepts a comma-separated string or a YAML list.                                                                                                                                                                                                             |
| `shell`                    | No          | Shell for `` !`command` `` and ` ```! ` blocks. Accepts `bash` (default) or `powershell`. PowerShell requires `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`.                                                                                                                                                                  |

**Control de quién invoca la skill (CRÍTICO para el caso del usuario)**

Texto literal de la doc:
- `disable-model-invocation: true` → **Only you can invoke the skill.** Use this for workflows with side effects or that you want to control timing, like `/commit`, `/deploy`, or `/send-slack-message`. You don't want Claude deciding to deploy because your code looks ready.
- `user-invocable: false` → **Only Claude can invoke the skill.** Use this for background knowledge that isn't actionable as a command.

Tabla "How the two fields affect invocation and context loading":

| Frontmatter                      | You can invoke | Claude can invoke | When loaded into context                                     |
| :------------------------------- | :------------- | :---------------- | :----------------------------------------------------------- |
| (default)                        | Yes            | Yes               | Description always in context, full skill loads when invoked |
| `disable-model-invocation: true` | Yes            | No                | Description not in context, full skill loads when you invoke |
| `user-invocable: false`          | No             | Yes               | Description always in context, full skill loads when invoked |

**PARA EL CASO DEL USUARIO (solo invocable con `/nombre` por el usuario, no auto-activable por el modelo): usar `disable-model-invocation: true`.** Este es el combo correcto. `user-invocable: false` es lo contrario (oculta la skill del menú `/` y solo deja que la invoque Claude), no lo que quiere.

Ejemplo literal con `disable-model-invocation: true`:

```yaml
---
name: deploy
description: Deploy the application to production
disable-model-invocation: true
---

Deploy $ARGUMENTS to production:

1. Run the test suite
2. Build the application
3. Push to the deployment target
4. Verify the deployment succeeded
```

**Substituciones de string disponibles (tabla literal)**

| Variable               | Description                                                                                                                                                                                                                                                                              |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$ARGUMENTS`           | All arguments passed when invoking the skill. If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`.                                                                                                                                             |
| `$ARGUMENTS[N]`        | Access a specific argument by 0-based index, such as `$ARGUMENTS[0]` for the first argument.                                                                                                                                                                                             |
| `$N`                   | Shorthand for `$ARGUMENTS[N]`, such as `$0` for the first argument or `$1` for the second.                                                                                                                                                                                               |
| `$name`                | Named argument declared in the `arguments` frontmatter list. Names map to positions in order, so with `arguments: [issue, branch]` the placeholder `$issue` expands to the first argument and `$branch` to the second.                                                                   |
| `${CLAUDE_SESSION_ID}` | The current session ID. Useful for logging, creating session-specific files.                                                                                                                                                                                                             |
| `${CLAUDE_SKILL_DIR}`  | The directory containing the skill's `SKILL.md` file. For plugin skills, this is the skill's subdirectory within the plugin, not the plugin root. Use this in bash injection commands to reference scripts or files bundled with the skill, regardless of the current working directory. |

**Notas sobre argumentos:**
- Indexed arguments usan shell-style quoting: `/my-skill "hello world" second` hace que `$0` sea `hello world` y `$1` sea `second`.
- `$ARGUMENTS` siempre expande al string completo tal como fue tecleado.
- Si invocas una skill con argumentos pero el SKILL.md NO incluye `$ARGUMENTS`, Claude Code **añade `ARGUMENTS: <your input>` al final del contenido** para que Claude vea lo tecleado.

Ejemplo con `$ARGUMENTS` literal:

```yaml
---
name: session-logger
description: Log activity for this session
---

Log the following to logs/${CLAUDE_SESSION_ID}.log:

$ARGUMENTS
```

Ejemplo con argumentos posicionales (`$ARGUMENTS[N]`):

```yaml
---
name: migrate-component
description: Migrate a component from one framework to another
---

Migrate the $ARGUMENTS[0] component from $ARGUMENTS[1] to $ARGUMENTS[2].
Preserve all existing behavior and tests.
```

Versión con shorthand `$N`:

```yaml
---
name: migrate-component
description: Migrate a component from one framework to another
---

Migrate the $0 component from $1 to $2.
Preserve all existing behavior and tests.
```

**Pre-aprobar tools con `allowed-tools`**

"The `allowed-tools` field grants permission for the listed tools while the skill is active, so Claude can use them without prompting you for approval. It does not restrict which tools are available: every tool remains callable, and your permission settings still govern tools that are not listed."

Punto clave: `allowed-tools` **no restringe** qué herramientas puede usar la skill, solo pre-aprueba las listadas para evitar prompts. Cualquier tool sigue siendo callable (sujeta al sistema de permisos global). AskUserQuestion por ejemplo no requiere permission (Permission Required = No en la tabla de tools-reference), así que es invocable sin pre-aprobación.

Ejemplo con tools pre-aprobadas:

```yaml
---
name: commit
description: Stage and commit the current changes
disable-model-invocation: true
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)
---
```

**Inyección dinámica de contexto** — sintaxis `` !`<command>` `` ejecuta shell antes de mandar el contenido a Claude; la salida reemplaza el placeholder. Para multilínea, fenced block abierto con ` ```! `. Se puede desactivar con `"disableSkillShellExecution": true` en settings.

**Run skills in a subagent** (`context: fork`) — el contenido de la skill se convierte en el prompt que conduce al subagente; no tiene acceso al historial de conversación. Campo `agent` elige qué subagent (Explore, Plan, general-purpose o custom de `.claude/agents/`). Default si se omite: `general-purpose`.

**Ciclo de vida del contenido de la skill**
- Cuando se invoca una skill (por ti o por Claude), el contenido renderizado de `SKILL.md` entra en la conversación como un único mensaje y se queda ahí el resto de la sesión.
- Claude Code **no re-lee el archivo** en turnos posteriores — escribe las instrucciones como standing instructions, no como pasos one-time.
- Auto-compaction: tras compactación, Claude Code re-attacha la invocación más reciente de cada skill conservando los primeros 5,000 tokens, con budget combinado de 25,000 tokens entre skills.

**Troubleshooting clave**
- "Skill not triggering" → revisar description, verificar en "What skills are available?", invocar directamente con `/skill-name`.
- "Skill triggers too often" → description más específica o añadir `disable-model-invocation: true`.

### Slash Commands in the SDK — https://code.claude.com/docs/en/agent-sdk/slash-commands

**Nota oficial:** "The `.claude/commands/` directory is the legacy format. The recommended format is `.claude/skills/<name>/SKILL.md`, which supports the same slash-command invocation (`/name`) plus autonomous invocation by Claude. The CLI continues to support both formats."

**Ubicaciones legacy (para comandos .md planos en commands/)**
- **Project commands**: `.claude/commands/` — Available only in the current project (legacy; prefer `.claude/skills/`)
- **Personal commands**: `~/.claude/commands/` — Available across all your projects (legacy; prefer `~/.claude/skills/`)

**Formato con frontmatter — ejemplo literal mostrando `allowed-tools`, `description`, `model`:**

Archivo `.claude/commands/security-check.md`:

```markdown
---
allowed-tools: Read, Grep, Glob
description: Run security vulnerability scan
model: claude-opus-4-7
---

Analyze the codebase for security vulnerabilities including:
- SQL injection risks
- XSS vulnerabilities
- Exposed credentials
- Insecure configurations
```

**Ejemplo con `argument-hint` + placeholders posicionales $1 $2:**

Archivo `.claude/commands/fix-issue.md`:

```markdown
---
argument-hint: [issue-number] [priority]
description: Fix a GitHub issue
---

Fix issue #$1 with priority $2.
Check the issue description and implement the necessary changes.
```

Uso: `/fix-issue 123 high` procesa con `$1="123"` y `$2="high"`.

**Ejecución de bash commands con `!` inline:**

Archivo `.claude/commands/git-commit.md`:

```markdown
---
allowed-tools: Bash(git add *), Bash(git status *), Bash(git commit *)
description: Create a git commit
---

## Context

- Current status: !`git status`
- Current diff: !`git diff HEAD`

## Task

Create a git commit with appropriate message based on the changes.
```

**File references con `@`:**

```markdown
---
description: Review configuration files
---

Review the following configuration files for issues:
- Package config: @package.json
- TypeScript config: @tsconfig.json
- Environment config: @.env
```

**Namespacing por subdirectorios** (organización de comandos en carpetas — la subdir aparece en la descripción del comando pero no afecta el nombre):

```bash
.claude/commands/
├── frontend/
│   ├── component.md      # Creates /component (project:frontend)
│   └── style-check.md     # Creates /style-check (project:frontend)
├── backend/
│   ├── api-test.md        # Creates /api-test (project:backend)
│   └── db-migrate.md      # Creates /db-migrate (project:backend)
└── review.md              # Creates /review (project)
```

**Ejemplo práctico Test Runner con `$ARGUMENTS`:**

```markdown
---
allowed-tools: Bash, Read, Edit
argument-hint: [test-pattern]
description: Run tests with optional pattern
---

Run tests matching pattern: $ARGUMENTS

1. Detect the test framework (Jest, pytest, etc.)
2. Run tests with the provided pattern
3. If tests fail, analyze and fix them
4. Re-run to verify fixes
```

### Tools reference — https://code.claude.com/docs/en/tools-reference

**AskUserQuestion en la tabla oficial de tools built-in:**

| Tool              | Description                                                                                | Permission Required |
| :---------------- | :----------------------------------------------------------------------------------------- | :------------------ |
| `AskUserQuestion` | Asks multiple-choice questions to gather requirements or clarify ambiguity                 | No                  |

- Permission Required = **No** → no requiere permission. AskUserQuestion se puede invocar desde cualquier sesión (incluidas skills) sin necesidad de declararla en `allowed-tools` ni de ningún prompt de permisos.
- El nombre exacto del tool (string a usar en permissions, allowed-tools listas, subagent tool lists, hook matchers) es `AskUserQuestion`.
- La descripción oficial confirma capacidad de **multiple-choice**, que es justo lo que el usuario necesita para sus rondas de los 10 puntos.
- No hay tool-specific behavior sección para AskUserQuestion en la página de tools-reference (la página extiende con notas solo para `Bash`, `LSP`, `Monitor`, `PowerShell`). No se documenta schema detallado de argumentos (question/header/options/multiSelect) en esta página — esa información se describe en `/en/agent-sdk/user-input` (ya catalogada en reference.md) pero no fue fetcheada en esta ejecución; si necesitas detalle de los campos, consúltala aparte.

**Sobre skills y el tool `Skill`:**

| Tool    | Description                                                                              | Permission Required |
| :------ | :--------------------------------------------------------------------------------------- | :------------------ |
| `Skill` | Executes a skill within the main conversation                                            | Yes                 |

- "To extend Claude with reusable prompt-based workflows, write a skill, which runs through the existing `Skill` tool rather than adding a new tool entry."
- Para denegar todas las skills: añadir `Skill` a deny rules en `/permissions`.
- Para permitir/denegar específicas: `Skill(commit)` (exact match) o `Skill(review-pr *)` (prefix con args).

**Aclaración importante en la doc de skills (página principal):**

> "The `user-invocable` field only controls menu visibility, not Skill tool access. Use `disable-model-invocation: true` to block programmatic invocation."

Esto reafirma: para bloquear invocación automática del modelo hay que usar `disable-model-invocation: true`, no `user-invocable: false`.

### Commands (invocación con `/`) — https://code.claude.com/docs/en/commands

- "Commands control Claude Code from inside a session."
- Type `/` to see every command available; escribir `/` + letras filtra.
- Las entradas marcadas **Skill** en la tabla son bundled skills (mismo mecanismo que las que escribes tú: un prompt manejado a Claude, que también puede invocarlas automáticamente). Todo lo demás son built-in commands cuya lógica está hardcoded en el CLI.
- Notación: `<arg>` indica argumento **obligatorio**, `[arg]` indica **opcional**. Esta es la convención que se usa también en `argument-hint`.
- Para añadir tus propios comandos, la doc apunta directamente a la página de Skills (es el único camino recomendado).

## Síntesis lista para aplicar al caso del usuario

Para la skill user-invocable que pide una idea de negocio, hace rondas de AskUserQuestion multi-choice cubriendo 10 puntos y genera un .md por punto en una carpeta con el nombre de la idea:

- **Ubicación global** (pedida por el usuario): `~/.claude/skills/<nombre-skill>/SKILL.md`.
- **Frontmatter mínimo recomendado**:
  - `name:` el nombre de la skill (lowercase, números, hyphens, max 64 chars).
  - `description:` una descripción corta — aunque se use `disable-model-invocation: true`, la description sirve para `/` autocompletado y future maintenance. Con `disable-model-invocation: true`, la description NO se mete en contexto, así que puede ser breve.
  - `argument-hint: [descripcion-idea]` — hint que aparece durante autocompletado para guiar al usuario sobre qué pasar.
  - `disable-model-invocation: true` — ESTE es el campo clave para que SOLO el usuario pueda invocarla con `/nombre` y Claude no la auto-active.
  - **NO usar `user-invocable: false`** — eso haría lo contrario (ocultar del menú `/` y dejar que solo Claude la invoque).
- **NO hace falta declarar `AskUserQuestion` en `allowed-tools`**: según tools-reference esta tool tiene Permission Required = No, así que es invocable sin pre-aprobación. `allowed-tools` se usa solo para pre-aprobar tools que sí requieren permiso (Bash, Edit, Write, WebFetch, etc.). Para el caso del usuario posiblemente SÍ convenga declarar `Write` o `Bash(mkdir *)` en `allowed-tools` si la skill va a crear el directorio y los .md sin pedir aprobación en cada paso:
  ```yaml
  allowed-tools: Write Bash(mkdir *)
  ```
- **Recibir la descripción de la idea**: en el cuerpo del SKILL.md usar `$ARGUMENTS` para que lo que el usuario teclee tras `/nombre <descripcion>` llegue al prompt. Si el usuario no teclea nada, Claude Code no añade nada; hay que instruir en el cuerpo "si `$ARGUMENTS` viene vacío, pide al usuario con AskUserQuestion la descripción de la idea".
- **Invocación desde la skill de AskUserQuestion**: está confirmada como built-in tool sin restricción de permiso, así que el flujo "haz rondas de AskUserQuestion multi-choice cubriendo 10 puntos" se describe en el cuerpo del SKILL.md como standing instructions. Recordar: el cuerpo de la skill entra en la conversación como un único mensaje y se queda para el resto de la sesión, así que hay que describir los 10 puntos como instrucciones válidas durante toda la ejecución, no como pasos one-time.
- **Crear carpeta y escribir 10 .md**: instrucciones en el cuerpo para que Claude use `Bash(mkdir <slug-idea>)` y luego `Write` para cada `<slug-idea>/<N>-<nombre-punto>.md`. Alternativamente `${CLAUDE_SKILL_DIR}` da la ruta de la skill si se quiere guardar allí, pero para "carpeta con el nombre de la idea" parece querer relativo al cwd del usuario.
- **Plantilla de SKILL.md esqueleto sugerida** (combinando todo lo anterior — adaptar texto al caso):
  ```yaml
  ---
  name: idea-negocio
  description: Genera 10 .md estructurados sobre una idea de negocio tras rondas de preguntas multi-choice.
  argument-hint: [descripcion-breve-de-la-idea]
  disable-model-invocation: true
  allowed-tools: Write Bash(mkdir *)
  ---

  Idea de negocio a analizar: $ARGUMENTS

  (si $ARGUMENTS viene vacío, invocar AskUserQuestion para pedir la descripción).

  Para cada uno de los 10 puntos siguientes, usa AskUserQuestion multi-choice para completar los datos que falten y luego escribe un archivo Markdown en la carpeta `<slug-idea>/`:

  1. ...
  2. ...
  ...
  10. ...

  Al terminar, muestra un resumen de los 10 archivos creados.
  ```

## URLs visitadas

- [Extend Claude with skills — página principal de Skills](https://code.claude.com/docs/en/skills)
- [Slash Commands in the SDK](https://code.claude.com/docs/en/agent-sdk/slash-commands)
- [Tools reference](https://code.claude.com/docs/en/tools-reference)
- [Commands](https://code.claude.com/docs/en/commands)

## Estado de reference.md

reference.md sin cambios.

<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->
