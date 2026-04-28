
---
link: https://code.claude.com/docs/en/overview
description: Página de bienvenida y visión general de Claude Code que presenta los métodos de instalación (native install con `curl`/`irm`, Homebrew, WinGet) para Terminal, Desktop, VS Code, JetBrains y Web, además de listar capacidades clave como automatización de tareas, creación de commits y PRs, integración con MCP, personalización con CLAUDE.md, skills y hooks, uso de subagentes y Agent SDK, y ejecución programada con Routines o `/loop`. Incluye una tabla comparativa de superficies (Remote Control, Channels, GitHub Actions, Slack, Chrome) para elegir dónde ejecutar Claude Code.
---

---
link: https://code.claude.com/docs/en/quickstart
description: Guía de inicio rápido para el CLI de Claude Code que recorre 8 pasos (instalación con curl, PowerShell, Homebrew, WinGet), login con `/login`, primera sesión con `claude`, hacer preguntas sobre el código, editar archivos, usar Git, arreglar bugs y flujos comunes como refactor o tests. Incluye tabla de comandos esenciales (`claude`, `claude -p`, `claude -c`, `claude -r`, `/clear`, `/help`) y consejos para principiantes.
---

---
link: https://code.claude.com/docs/en/changelog
description: Registro de cambios (changelog) de Claude Code que documenta lanzamientos desde la versión 2.1.114 (abril 2026) hacia atrás, detallando nuevas funcionalidades como `/ultrareview`, `/powerup`, soporte de PowerShell en Windows, modo sin parpadeo (`NO_FLICKER`) y correcciones de seguridad en Bash y permisos MCP. Incluye flags como `--bare`, variables de entorno como `CLAUDE_CODE_USE_POWERSHELL_TOOL` y mejoras en configuración, hooks (`PreToolUse`, `PostToolUse`) y autenticación con Bedrock, Vertex y Foundry.
---

---
link: https://code.claude.com/docs/en/how-claude-code-works
description: Explicación de la arquitectura interna de Claude Code: el bucle agéntico de tres fases (gather context, take action, verify results), los modelos disponibles (Sonnet, Opus) intercambiables con `/model` o `--model`, y las cinco categorías de herramientas integradas (File operations, Search, Execution, Web, Code intelligence). Cubre gestión de sesiones en `~/.claude/projects/`, `--fork-session`, la ventana de contexto con `/compact` y `/context`, checkpoints (doble `Esc` o `/rewind`) y los modos de permisos (Default, Auto-accept, Plan, Auto) que se alternan con `Shift+Tab`.
---

---
link: https://code.claude.com/docs/en/features-overview
description: Guía comparativa de las extensiones de Claude Code (CLAUDE.md, Skills, Subagents, Agent teams, MCP, Hooks, Plugins) con tablas que indican cuándo usar cada una, cómo se superponen entre niveles (managed, user, project, plugin) y ejemplos de combinaciones como "Skill + MCP" o "Hook + MCP". Detalla el coste de contexto de cada feature, su momento de carga (al iniciar sesión, bajo demanda, al invocar) y patrones de adopción progresiva según los disparadores habituales.
---

---
link: https://code.claude.com/docs/en/claude-directory
description: Exploración interactiva del directorio `.claude/` en el proyecto y `~/.claude/` en el home, mostrando dónde viven `CLAUDE.md`, `settings.json`, hooks, skills, commands, subagents, rules y auto memory. Describe qué archivos se versionan en Git, cuáles son locales y cómo Claude Code resuelve prioridades entre scopes project/user/managed.
---

---
link: https://code.claude.com/docs/en/context-window
description: Simulación interactiva de cómo se llena la ventana de contexto (200.000 tokens por defecto) durante una sesión de Claude Code, mostrando qué se carga automáticamente al arranque (system prompt, MEMORY.md, env info, herramientas MCP diferidas) y el coste en tokens de cada lectura de archivo, regla activada o hook ejecutado. Menciona variables como `ENABLE_TOOL_SEARCH` y flujos de compactación automática.
---

---
link: https://code.claude.com/docs/en/memory
description: Documentación completa sobre memoria persistente en Claude Code: cómo escribir y organizar archivos `CLAUDE.md` (managed, project, user, local) con imports `@path`, cómo usar `.claude/rules/` con frontmatter `paths` para reglas scoped a globs, y cómo funciona auto memory que guarda aprendizajes en `~/.claude/projects/<project>/memory/MEMORY.md` (primeras 200 líneas o 25KB). Incluye comandos `/memory`, `/init` (con `CLAUDE_CODE_NEW_INIT=1`), settings `autoMemoryEnabled`, `autoMemoryDirectory`, `claudeMdExcludes` y `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD`.
---

---
link: https://code.claude.com/docs/en/permission-modes
description: Detalla los seis modos de permisos de Claude Code (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`), qué auto-aprueba cada uno y cómo cambiar entre ellos con `Shift+Tab`, el flag `--permission-mode` o la configuración `defaultMode` en settings. Explica el clasificador de auto mode (requiere Max/Team/Enterprise/API y Sonnet 4.6, Opus 4.6 o 4.7), sus reglas por defecto, fallback tras 3 bloqueos consecutivos o 20 totales, y la lista de "protected paths" (`.git`, `.vscode`, `.claude`, `.mcp.json`, etc.) que nunca se auto-aprueban.
---

---
link: https://code.claude.com/docs/en/common-workflows
description: Recetas paso a paso para tareas habituales con Claude Code - explorar un codebase nuevo, corregir bugs, refactorizar, usar subagentes con `/agents`, trabajar en Plan Mode, añadir tests, crear PRs con `claude --from-pr`, manejar imágenes, usar referencias `@` a archivos y MCP, activar thinking extendido con `ultrathink`/`Ctrl+O`/`MAX_THINKING_TOKENS`, reanudar sesiones con `--continue`/`--resume`/`--from-pr`, ejecutar sesiones paralelas con git worktrees (`--worktree`, `.worktreeinclude`), configurar notificaciones con hooks `Notification` y usar Claude como utilidad Unix con `--output-format json/stream-json`.
---

---
link: https://code.claude.com/docs/en/best-practices
description: Patrones recomendados para sacar el máximo partido de Claude Code - dar a Claude formas de verificar su trabajo (tests, screenshots), explorar antes de planificar con Plan Mode, escribir prompts específicos, configurar el entorno (CLAUDE.md con `/init`, permisos con auto mode, `/permissions` y `/sandbox`, CLIs como `gh`, servidores MCP, hooks, skills en `.claude/skills/`, subagentes en `.claude/agents/`, plugins con `/plugin`), gestionar la sesión con `/clear`, `/compact`, `/rewind` y `/btw`, y escalar con sesiones paralelas, modo no interactivo `claude -p` y patrones fan-out con `--allowedTools`.
---

---
link: https://code.claude.com/docs/en/platforms
description: Tabla comparativa de las plataformas donde se puede ejecutar Claude Code (CLI, Desktop, VS Code, JetBrains, Web, Mobile) y las integraciones disponibles (Chrome, GitHub Actions, GitLab CI/CD, Code Review, Slack), explicando qué funcionalidades son exclusivas de cada superficie. Incluye una tabla sobre cómo trabajar sin estar en el terminal mediante Dispatch, Remote Control, Channels, Slack o Scheduled tasks.
---

---
link: https://code.claude.com/docs/en/remote-control
description: Describe Remote Control, que permite continuar una sesión local de Claude Code desde claude.ai/code o la app móvil mientras el proceso sigue ejecutándose en tu máquina con acceso a MCPs, archivos y configuración local. Explica los tres modos de inicio en CLI (`claude remote-control` server mode, `claude --remote-control`/`--rc` y `/remote-control` desde una sesión existente) con flags como `--name`, `--spawn` (same-dir/worktree/session), `--capacity`, `--sandbox`, requisitos (v2.1.51+, plan Pro/Max/Team/Enterprise, no API keys), push notifications móviles y cómo se diferencia de Claude Code on the web.
---

---
link: https://code.claude.com/docs/en/claude-code-on-the-web
description: Referencia completa de Claude Code on the web (research preview en Pro, Max, Team, Enterprise con premium seats) - autenticación GitHub vía GitHub App o `/web-setup`, entorno cloud con VMs Ubuntu 24.04 (4 vCPUs, 16 GB RAM, 30 GB disco) y herramientas preinstaladas (Python, Node, Ruby, PHP, Java, Go, Rust, Docker, PostgreSQL, Redis), setup scripts cacheados, niveles de acceso de red (None/Trusted/Full/Custom) con dominios preaprobados, variable `CLAUDE_CODE_REMOTE_SESSION_ID`, teleport entre web y terminal con `--remote`/`--teleport`/`/teleport`/`/tasks`, auto-fix de PRs vía GitHub App, y comandos como `/compact`, `/context` y `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`.
---

---
link: https://code.claude.com/docs/en/web-quickstart
description: Guía de inicio para Claude Code on the web que explica cómo conectar GitHub (instalando la Claude GitHub App o usando `/web-setup` con el `gh` CLI), crear un environment con nombre, acceso de red, variables `.env` y setup script, enviar una tarea seleccionando repositorio, rama y modo de permisos (Auto accept edits o Plan), y revisar cambios con comentarios inline antes de crear un PR. Cubre parámetros URL para pre-fill (`prompt`, `prompt_url`, `repositories`, `environment`) y troubleshooting de escenarios como "Setup script failed" o `/web-setup` inválido.
---

---
link: https://code.claude.com/docs/en/desktop
description: Referencia completa de la app Desktop de Claude Code para macOS y Windows, que añade sobre la experiencia estándar - sesiones paralelas con aislamiento Git worktree, layout drag-and-drop con terminal, editor de archivos y panel de previsualización integrados, side chats que no afectan al hilo principal, diff viewer visual con comentarios inline, preview en vivo de apps, computer use, sesiones Dispatch desde el móvil, monitorización de PRs con auto-merge y configuración empresarial mediante connectors.
---

---
link: https://code.claude.com/docs/en/desktop-quickstart
description: Guía de instalación y primer uso de la app Desktop de Claude Code (macOS universal, Windows x64, Windows ARM64; Linux no soportado) explicando las tres pestañas (Chat, Cowork, Code) y centrándose en Code. Recorre seleccionar entorno (Local, Remote, SSH), elegir modelo, iniciar sesión, revisar cambios en modo Ask permissions por defecto, y describe atajos como `Ctrl+backtick` para abrir el terminal, `@filename` para referenciar archivos y `+ → Slash commands` para invocar skills.
---

---
link: https://code.claude.com/docs/en/desktop-scheduled-tasks
description: Tareas programadas locales en Claude Code Desktop (macOS/Windows) que arrancan sesiones frescas de Claude en un horario recurrente para revisiones de código diarias, auditorías de dependencias o briefings matinales. Cada tarea se crea desde la pestaña **Schedule → New local task** con nombre (kebab-case único), descripción, prompt, frecuencia (Manual, Hourly con offset fijo de hasta 10 min, Daily, Weekdays, Weekly o intervalos custom descritos en lenguaje natural), modelo, modo de permisos, working folder y toggle de worktree para aislamiento Git. Requiere app abierta y equipo despierto (opción **Keep computer awake** en Settings → Desktop app → General); los runs perdidos durante los últimos 7 días se recuperan con una única ejecución catch-up. Permite **Run now**, pausar repeticiones, revisar history y persistir aprobaciones de herramientas con "always allow", y la definición on-disk vive en `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (o bajo `CLAUDE_CONFIG_DIR`). Incluye tabla comparativa frente a cloud Routines y al `/loop` del CLI (intervalo mínimo 1 min vs 1 h de cloud).
---

---
link: https://code.claude.com/docs/en/channels
description: Describe channels (research preview, requiere v2.1.80+ y login claude.ai), servidores MCP que empujan eventos a una sesión de Claude Code en marcha (Telegram, Discord, iMessage y el demo fakechat). Detalla instalación con `/plugin install <channel>@claude-plugins-official`, configuración con `/{channel}:configure <token>`, arranque con `claude --channels plugin:<name>@<marketplace>`, pairing con `/{channel}:access pair <code>` y allowlist con `/{channel}:access policy allowlist`, además de los settings managed `channelsEnabled` y `allowedChannelPlugins` para Team/Enterprise.
---

---
link: https://code.claude.com/docs/en/chrome
description: Integración beta de Claude Code con la extensión Claude in Chrome (v1.0.36+) para Google Chrome y Microsoft Edge (no Brave/Arc/WSL), que da a Claude capacidades de automatización de navegador - live debugging, verificación de diseños, testing de web apps, extracción de datos y grabación de GIFs. Se activa con `claude --chrome` o `/chrome` dentro de sesión, requiere plan directo Anthropic (Pro/Max/Team/Enterprise), y lista rutas de los archivos de native messaging host para macOS, Linux y Windows.
---

---
link: https://code.claude.com/docs/en/computer-use
description: Computer use en el CLI (research preview en macOS, Pro/Max, v2.1.85+, sólo sesiones interactivas) que permite a Claude abrir apps, hacer clic, teclear y leer la pantalla. Se habilita activando el MCP server `computer-use` en `/mcp` y otorgando permisos de Accessibility y Screen Recording. Incluye aprobación por app por sesión, warnings para apps con acceso amplio (terminales, Finder, System Settings), downscaling automático de screenshots, lock machine-wide y cancelación inmediata con `Esc`.
---

---
link: https://code.claude.com/docs/en/vs-code
description: Instalación y uso de la extensión Claude Code para VS Code/Cursor (requiere VS Code 1.98.0+), con interfaz gráfica que incluye diffs inline, `@-mentions` con rangos de líneas (`Option+K`/`Alt+K`), historial de sesiones, modo plan con revisión de markdown y modo terminal opcional (`claudeCode.useTerminal`). Documenta settings como `initialPermissionMode`, `preferredLocation`, `allowDangerouslySkipPermissions`, el URI handler `vscode://anthropic.claude-code/open?prompt=...&session=...`, el servidor MCP interno `ide` con herramientas `mcp__ide__getDiagnostics` y `mcp__ide__executeCode` (Jupyter), y gestión de plugins con `/plugins`.
---

---
link: https://code.claude.com/docs/en/jetbrains
description: Documentación del plugin de Claude Code para IDEs JetBrains (IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, GoLand) - atajos `Cmd+Esc`/`Ctrl+Esc` para lanzar Claude y `Cmd+Option+K`/`Alt+Ctrl+K` para referencias de archivo (`@File#L1-99`), instalación desde el JetBrains Marketplace, conexión con `/ide` desde terminal externo, settings en **Tools → Claude Code [Beta]** (Claude command, Option+Enter multi-línea, auto-updates), y troubleshooting para ESC, WSL y Remote Development.
---

---
link: https://code.claude.com/docs/en/github-actions
description: Integración de Claude Code como GitHub Action (`anthropics/claude-code-action@v1`) que responde a menciones `@claude` en issues y PRs, con setup rápido vía `/install-github-app` o manual instalando la Claude GitHub App y el secret `ANTHROPIC_API_KEY`. Incluye migración desde la beta (reemplazar `direct_prompt` por `prompt`, `custom_instructions` por `claude_args: --append-system-prompt`, eliminar `mode`), configuración para AWS Bedrock y Google Vertex AI vía OIDC/Workload Identity Federation (secrets `AWS_ROLE_TO_ASSUME`, `GCP_WORKLOAD_IDENTITY_PROVIDER`, `GCP_SERVICE_ACCOUNT`) y flags como `--max-turns`, `--model`, `--allowedTools`, `--mcp-config`.
---

---
link: https://code.claude.com/docs/en/gitlab-ci-cd
description: Integración beta de Claude Code con GitLab CI/CD (mantenida por GitLab) para responder a menciones `@claude` y crear MRs automáticamente. Muestra ejemplo de `.gitlab-ci.yml` con el job `claude` sobre `node:24-alpine3.21`, instalación mediante `curl -fsSL https://claude.ai/install.sh | bash`, invocación con `claude -p "$AI_FLOW_INPUT" --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab"`, variables CI/CD `ANTHROPIC_API_KEY`, `AWS_ROLE_TO_ASSUME`, `GCP_WORKLOAD_IDENTITY_PROVIDER`, `GCP_SERVICE_ACCOUNT`, autenticación OIDC/WIF y uso del servidor `gitlab-mcp-server`.
---

---
link: https://code.claude.com/docs/en/github-enterprise-server
description: Soporte de Claude Code para instancias self-hosted de GitHub Enterprise Server (planes Team/Enterprise) que habilita Claude Code on the web (`claude --remote`), Code Review, Teleport sessions (`--teleport`), marketplaces de plugins, contribution metrics y GitHub Actions sobre repos del GHES corporativo; el servidor GitHub MCP y el comando `/install-github-app` no son compatibles (se usa `gh auth login --hostname github.example.com` como alternativa). El admin conecta la instancia una sola vez desde claude.ai/admin-settings/claude-code mediante un manifest guiado que crea la GitHub App en un clic (o setup manual con hostname, OAuth client ID/secret, App ID, webhook secret, private key y CA opcional), con permisos Contents, Pull requests, Issues, Checks, Actions, Repository hooks y Metadata, y webhooks `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review` y `check_run`. Los desarrolladores clonan del GHES y lanzan `claude --remote` sin configuración extra: Claude detecta el host desde el git remote. Para marketplaces se usan URLs completas (`/plugin marketplace add git@github.example.com:platform/claude-plugins.git`) y managed settings `strictKnownMarketplaces` con `hostPattern` o `extraKnownMarketplaces`. Requiere que la instancia GHES sea alcanzable desde las IPs de Anthropic.
---

---
link: https://code.claude.com/docs/en/code-review
description: Servicio gestionado Code Review (research preview para Team/Enterprise, no compatible con Zero Data Retention) que analiza PRs de GitHub mediante flota de agentes en paralelo y publica comentarios inline con severidades "Important", "Nit" y "Pre-existing". Describe configuración desde claude.ai/admin-settings/claude-code, modos "Once after PR creation"/"After every push"/"Manual", triggers manuales con `@claude review` y `@claude review once`, personalización mediante `CLAUDE.md` y `REVIEW.md`, el check run "Claude Code Review" con salida machine-readable (`bughunter-severity`), precio (~$15-25 por review facturados como extra usage) y dashboard en claude.ai/analytics/code-review.
---

---
link: https://code.claude.com/docs/en/slack
description: Integración Claude Code in Slack que detecta menciones `@Claude` con intención de programación en canales (no DMs) y crea sesiones de Claude Code on the web, con requisitos de plan Pro/Max/Team/Enterprise con acceso a Claude Code on the web, GitHub conectado y cuenta Slack vinculada. Explica instalación desde Slack App Marketplace, conexión en App Home, modos de routing "Code only" y "Code + Chat", el comando `/invite @Claude` para añadir Claude a canales, botones "View Session"/"Create PR"/"Retry as Code"/"Change Repo" y límites actuales (solo GitHub, un PR por sesión).
---

---
link: https://code.claude.com/docs/en/sub-agents
description: Explica qué son los subagentes de Claude Code, asistentes especializados con su propio contexto, prompt y herramientas permitidas, que delegan tareas secundarias (búsqueda, análisis, logs) para no saturar la conversación principal. Cubre cómo definirlos, ámbitos (usuario/proyecto/plugin), campos de frontmatter y casos de uso como enrutar trabajo a modelos más baratos como Haiku.
---

---
link: https://code.claude.com/docs/en/agent-teams
description: Describe los equipos de agentes (experimentales, activados con la variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`), donde una sesión líder coordina a varios teammates que trabajan en paralelo con mensajería directa y una lista de tareas compartida. Detalla modos de visualización (in-process o split panes con tmux/iTerm2), el flag `--teammate-mode`, el almacenamiento en `~/.claude/teams/` y `~/.claude/tasks/`, hooks como `TeammateIdle`/`TaskCreated`/`TaskCompleted` y limitaciones del sistema.
---

---
link: https://code.claude.com/docs/en/mcp
description: Documenta cómo conectar Claude Code a herramientas externas vía Model Context Protocol (MCP), incluyendo un registro dinámico de servidores MCP oficiales filtrable por plataforma (Claude Code, API connector, Desktop) y guías para añadir servidores a tu configuración local.
---

---
link: https://code.claude.com/docs/en/discover-plugins
description: Guía para descubrir e instalar plugins desde marketplaces usando los comandos `/plugin`, `/plugin install`, `/plugin marketplace add/update/remove/list` y `/reload-plugins`. Cubre el marketplace oficial `claude-plugins-official`, los plugins de inteligencia de código basados en LSP (clangd-lsp, pyright-lsp, typescript-lsp, etc.), integraciones externas (github, linear, figma), ámbitos de instalación (user/project/local/managed), auto-updates con `DISABLE_AUTOUPDATER` y `FORCE_AUTOUPDATE_PLUGINS`, y la configuración de marketplaces de equipo mediante `extraKnownMarketplaces` en `.claude/settings.json`.
---

---
link: https://code.claude.com/docs/en/plugins
description: Tutorial para crear plugins de Claude Code que empaquetan skills, agents, hooks, servidores MCP y LSP. Explica el manifiesto `.claude-plugin/plugin.json` con campos name/description/version/author, la estructura de directorios (`skills/`, `agents/`, `hooks/`, `.mcp.json`, `.lsp.json`, `monitors/monitors.json`, `bin/`, `settings.json`), el testeo local con el flag `--plugin-dir`, el uso de `$ARGUMENTS` en skills, la migración desde configuración standalone en `.claude/`, y la distribución vía marketplaces.
---

---
link: https://code.claude.com/docs/en/skills
description: Documentación completa de las skills de Claude Code (archivos `SKILL.md` con frontmatter YAML), incluyendo skills bundled (`/simplify`, `/debug`, `/loop`, `/claude-api`), ubicaciones jerárquicas (enterprise > personal en `~/.claude/skills` > proyecto en `.claude/skills` > plugin), campos de frontmatter (`description`, `when_to_use`, `argument-hint`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context: fork`, `agent`, `hooks`, `paths`, `shell`), sustituciones como `$ARGUMENTS`, `$N` y `${CLAUDE_SKILL_DIR}`, inyección dinámica con comando entre backticks, ejecución en subagentes con `context: fork`, y control de acceso vía permissions (`Skill(name)`).
---

---
link: https://code.claude.com/docs/en/hooks-guide
description: Guía práctica para automatizar workflows con hooks configurados en `settings.json`, con ejemplos ready-to-use para notificaciones, auto-formateo con Prettier tras Edit/Write, bloqueo de archivos protegidos, reinyección de contexto tras compactación y auto-aprobación de permisos. Lista todos los eventos del ciclo de vida (`PreToolUse`, `PostToolUse`, `Notification`, `SessionStart`, `Stop`, `TaskCreated/Completed`, `ConfigChange`, `CwdChanged`, `FileChanged`, etc.), los tipos de hook (command, http, prompt, agent), matchers, el campo `if` para filtrado fino, y los códigos de salida (0 permite, 2 bloquea, JSON estructurado para control avanzado).
---

---
link: https://code.claude.com/docs/en/scheduled-tasks
description: Explica cómo programar prompts recurrentes en una sesión con el bundled skill `/loop` (intervalos tipo `5m`, `2h`, intervalo dinámico elegido por Claude o prompt de mantenimiento por defecto), recordatorios únicos en lenguaje natural, y las herramientas `CronCreate`/`CronList`/`CronDelete` que aceptan expresiones cron de 5 campos. Detalla `loop.md` en `.claude/` o `~/.claude/`, el jitter del scheduler, la expiración automática a los 7 días, el límite de 50 tareas por sesión, la variable `CLAUDE_CODE_DISABLE_CRON` y la comparación con Routines, Desktop scheduled tasks y GitHub Actions.
---

---
link: https://code.claude.com/docs/en/headless
description: Documenta cómo ejecutar Claude Code de forma programática con el flag `-p` (antes "headless mode") del Agent SDK, combinado con opciones como `--allowedTools`, `--output-format` (text/json/stream-json), `--json-schema`, `--append-system-prompt`, `--continue`, `--resume` y `--permission-mode` (dontAsk, acceptEdits). Presenta el modo `--bare` que omite el auto-descubrimiento de hooks, skills, plugins, servidores MCP, memoria automática y CLAUDE.md para tener ejecuciones reproducibles en CI, y describe los eventos del stream (`system/init`, `system/api_retry`, `system/plugin_install`).
---

---
link: https://code.claude.com/docs/en/troubleshooting
description: Guía exhaustiva para resolver problemas de instalación y uso de Claude Code - errores "command not found" y configuración de PATH, fallos TLS/SSL y proxies corporativos (`NODE_EXTRA_CA_CERTS`, `HTTPS_PROXY`), problemas específicos de Windows (PowerShell x86, git-bash, `CLAUDE_CODE_GIT_BASH_PATH`), WSL2 (networking NAT/mirrored, sandboxing con bubblewrap/socat), conflictos musl/glibc en Linux, autenticación (OAuth, `ANTHROPIC_API_KEY` obsoleta), rendimiento (`/compact`, `/heapdump`, ripgrep con `USE_BUILTIN_RIPGREP=0`), integración con JetBrains y el comando `/doctor` para diagnóstico general.
---

---
link: https://code.claude.com/docs/en/errors
description: Referencia de errores en tiempo de ejecución de Claude Code - errores de servidor (500, 529 Overloaded, request timed out), límites de uso (session/weekly/Opus limit, 429, credit balance too low), autenticación (Not logged in, Invalid API key, OAuth token revoked/expired), red (ECONNREFUSED, SSL certificate verification failed), y errores de petición (Prompt is too long, Request too large 30MB, Image/PDF too large, tool use mismatch). Explica los reintentos automáticos controlados por `CLAUDE_CODE_MAX_RETRIES` y `API_TIMEOUT_MS`, y comandos de recuperación como `/compact`, `/clear`, `/rewind`, `/model`, `/login` y `/feedback`.
---

---
link: https://code.claude.com/docs/en/third-party-integrations
description: Vista general para decidir cómo desplegar Claude Code en organizaciones, con tabla comparativa entre Claude for Teams/Enterprise, Anthropic Console, Amazon Bedrock, Google Vertex AI y Microsoft Foundry (facturación, regiones, autenticación, cost tracking). Explica cuándo usar proxies corporativos (`HTTPS_PROXY`) frente a LLM gateways (`ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`, `ANTHROPIC_FOUNDRY_BASE_URL`) y recoge buenas prácticas como pinear versiones de modelo, desplegar `CLAUDE.md`, configurar permisos de seguridad y centralizar MCPs mediante `.mcp.json`.
---

---
link: https://code.claude.com/docs/en/amazon-bedrock
description: Guía de configuración de Claude Code sobre Amazon Bedrock - asistente `/setup-bedrock`, variables `CLAUDE_CODE_USE_BEDROCK`, `AWS_REGION`, `AWS_BEARER_TOKEN_BEDROCK` y `ANTHROPIC_DEFAULT_OPUS/SONNET/HAIKU_MODEL` para pinear IDs de inference profile, además de credenciales vía `awsAuthRefresh`/`awsCredentialExport`, políticas IAM requeridas (`bedrock:InvokeModel`, `ListInferenceProfiles`) y mapeo por versión con `modelOverrides`. Incluye soporte de contexto 1M con sufijo `[1m]`, Bedrock Guardrails mediante `ANTHROPIC_CUSTOM_HEADERS`, endpoint Mantle (`CLAUDE_CODE_USE_MANTLE`, `ANTHROPIC_BEDROCK_MANTLE_BASE_URL`) y troubleshooting de SSO y errores de región.
---

---
link: https://code.claude.com/docs/en/google-vertex-ai
description: Configuración de Claude Code en Google Vertex AI con asistente `/setup-vertex`, habilitación de `aiplatform.googleapis.com`, solicitud de modelos en Model Garden y variables `CLAUDE_CODE_USE_VERTEX`, `CLOUD_ML_REGION` (incluido `global`), `ANTHROPIC_VERTEX_PROJECT_ID` y `VERTEX_REGION_CLAUDE_*` para rutar por modelo. Detalla el pineo con `ANTHROPIC_DEFAULT_OPUS/SONNET/HAIKU_MODEL`, el rol IAM `roles/aiplatform.user`, los chequeos de modelo al iniciar, el contexto 1M con sufijo `[1m]` y el troubleshooting de cuotas, 404 de modelo no encontrado y errores 429.
---

---
link: https://code.claude.com/docs/en/microsoft-foundry
description: Configuración de Claude Code sobre Microsoft Foundry - aprovisionamiento del recurso en ai.azure.com con despliegues de Opus/Sonnet/Haiku, autenticación mediante `ANTHROPIC_FOUNDRY_API_KEY` o Microsoft Entra ID (cadena DefaultAzureCredential), y variables `CLAUDE_CODE_USE_FOUNDRY`, `ANTHROPIC_FOUNDRY_RESOURCE` y `ANTHROPIC_FOUNDRY_BASE_URL`. Incluye pineo de modelos (`ANTHROPIC_DEFAULT_OPUS/SONNET/HAIKU_MODEL`), roles RBAC (`Azure AI User`, `Cognitive Services User`) con ejemplo de rol personalizado y troubleshooting del error "ChainedTokenCredential authentication failed".
---

---
link: https://code.claude.com/docs/en/network-config
description: Configuración de red empresarial para Claude Code con variables `HTTPS_PROXY`/`HTTP_PROXY`/`NO_PROXY` (sin soporte de SOCKS), gestión del trust store con `CLAUDE_CODE_CERT_STORE` (`bundled`,`system`), CAs personalizadas vía `NODE_EXTRA_CA_CERTS` y autenticación mTLS con `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY` y `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`. Lista los dominios que deben estar en allowlist (`api.anthropic.com`, `claude.ai`, `platform.claude.com`, `storage.googleapis.com`, `downloads.claude.ai`, `bridge.claudeusercontent.com`) y menciona el IP allow list inheritance para GitHub Apps en GHES.
---

---
link: https://code.claude.com/docs/en/llm-gateway
description: Requisitos e integración de Claude Code con LLM gateways, detallando los formatos de API admitidos (Anthropic Messages `/v1/messages`, Bedrock `/invoke`, Vertex `:rawPredict`) con las cabeceras `anthropic-beta`/`anthropic-version` y `X-Claude-Code-Session-Id` que deben reenviarse. Cubre autenticación estática con `ANTHROPIC_AUTH_TOKEN`, dinámica con `apiKeyHelper` y `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`, y configuración específica de LiteLLM vía `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL` con flags `CLAUDE_CODE_SKIP_BEDROCK_AUTH`/`CLAUDE_CODE_SKIP_VERTEX_AUTH`, incluyendo la advertencia de seguridad sobre las versiones comprometidas 1.82.7/1.82.8 de LiteLLM.
---

---
link: https://code.claude.com/docs/en/devcontainer
description: Descripción del devcontainer de referencia de Claude Code (Node.js 20) compuesto por `devcontainer.json`, `Dockerfile` e `init-firewall.sh`, pensado para usar con la extensión Dev Containers de VS Code y permitir ejecutar `claude --dangerously-skip-permissions` con aislamiento. Detalla las características de seguridad con firewall default-deny que solo permite dominios allowlisted (npm, GitHub, Claude API), persistencia de sesión entre reinicios y casos de uso como aislamiento de trabajo por cliente, onboarding de equipos y paridad con entornos CI/CD.
---

---
link: https://code.claude.com/docs/en/setup
description: Guía de instalación avanzada de Claude Code con requisitos de sistema (macOS 13+, Windows 10 1809+, Ubuntu/Debian/Alpine), métodos de instalación (script nativo, Homebrew, WinGet, npm), configuración específica para Windows (Git Bash, WSL, PowerShell), canales de release (latest/stable) vía `autoUpdatesChannel`, pin de versión con `minimumVersion`, desactivación del auto-updater (`DISABLE_AUTOUPDATER`), verificación de integridad de binarios con manifest firmado GPG y desinstalación completa.
---

---
link: https://code.claude.com/docs/en/authentication
description: Explica cómo iniciar sesión en Claude Code con cuentas Pro/Max, Claude for Teams o Enterprise, Claude Console, o proveedores cloud (Bedrock, Vertex AI, Foundry), la gestión de credenciales (macOS Keychain o `~/.claude/.credentials.json`, `apiKeyHelper`), el orden de precedencia entre `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN` y OAuth, y la generación de tokens OAuth de larga duración con `claude setup-token` para CI.
---

---
link: https://code.claude.com/docs/en/security
description: Describe el modelo de seguridad de Claude Code basado en permisos explícitos, restricción de escritura al directorio de trabajo, sandboxing bash (`/sandbox`), protecciones contra prompt injection (blocklist de `curl`/`wget`, verificación de confianza para MCP, context windows aislados para web fetch), mitigaciones específicas (riesgo WebDAV en Windows), buenas prácticas para equipos (managed settings, hooks `ConfigChange`, auditoría con OpenTelemetry) y reporte de vulnerabilidades vía HackerOne.
---

---
link: https://code.claude.com/docs/en/server-managed-settings
description: Explica cómo administradores de Claude for Teams/Enterprise configuran Claude Code centralmente desde la consola web de Claude.ai (Admin Settings > Claude Code > Managed settings) sin necesidad de MDM, cubriendo requisitos de versión, política de precedencia frente a endpoint-managed settings, caché y polling horario, `forceRemoteSettingsRefresh` para fail-closed, diálogos de aprobación de seguridad para hooks/env vars, y limitaciones como la no aplicación a proveedores terceros (Bedrock, Vertex, Foundry).
---

---
link: https://code.claude.com/docs/en/data-usage
description: Detalla las políticas de uso de datos de Anthropic para Claude Code - política de entrenamiento (opt-in para consumidores Free/Pro/Max, no entrenamiento para Team/Enterprise/API salvo Development Partner Program), periodos de retención (30 días comercial, 5 años consumer opt-in), servicios de telemetría (Statsig para métricas, Sentry para errores) con variables de opt-out (`DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`) y diferencias de comportamiento por defecto entre Claude API, Bedrock, Vertex y Foundry.
---

---
link: https://code.claude.com/docs/en/zero-data-retention
description: Describe la opción Zero Data Retention (ZDR) disponible solo para Claude Code sobre Claude for Enterprise, que evita que los prompts y respuestas se almacenen tras la inferencia, enumera las funciones cubiertas (inferencia del modelo) y no cubiertas (chat en claude.ai, Cowork, analytics de contribución, integraciones de terceros), las funciones deshabilitadas bajo ZDR (Claude Code on the Web, remote sessions desde Desktop, comando `/feedback`) y el proceso de activación por organización a través del equipo de cuenta de Anthropic.
---

---
link: https://code.claude.com/docs/en/monitoring-usage
description: Guía completa para habilitar OpenTelemetry en Claude Code con `CLAUDE_CODE_ENABLE_TELEMETRY=1`, configurando exporters de métricas (otlp/prometheus/console), logs y trazas (beta con `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`), variables OTLP (endpoint, protocol, headers, mTLS), atributos estándar (session.id, user.account_uuid), métricas emitidas (`claude_code.token.usage`, `cost.usage`, `session.count`, `lines_of_code.count`, `commit.count`, `active_time.total`) y eventos detallados (user_prompt, tool_result, api_request, tool_decision, plugin_installed, skill_activated).
---

---
link: https://code.claude.com/docs/en/costs
description: Explica cómo rastrear y reducir costes de Claude Code mediante el comando `/cost`, límites de gasto por workspace en Claude Console, recomendaciones de rate limits (TPM/RPM) según tamaño de equipo, estrategias para reducir consumo de tokens (usar `/clear` y `/compact`, elegir Sonnet frente a Opus, reducir overhead de MCP, mover instrucciones de CLAUDE.md a skills, ajustar extended thinking con `MAX_THINKING_TOKENS` y `/effort`, delegar operaciones verbosas a subagents) y la gestión específica de agent teams.
---

---
link: https://code.claude.com/docs/en/analytics
description: Documenta los paneles analíticos de Claude Code para Teams/Enterprise (en claude.ai/analytics/claude-code) y para clientes API (en platform.claude.com/claude-code), cubriendo métricas de uso (líneas de código aceptadas, accept rate, DAU), métricas de contribución con integración GitHub (PRs etiquetados `claude-code-assisted`, leaderboard, exportación CSV), el proceso de atribución de PRs (ventana temporal de 21 días antes a 2 después, archivos excluidos como lockfiles y código generado) y limitaciones con Zero Data Retention.
---

---
link: https://code.claude.com/docs/en/plugin-marketplaces
description: Tutorial para crear y distribuir marketplaces de plugins de Claude Code mediante un archivo `.claude-plugin/marketplace.json` con esquema definido (campos name, owner, plugins), soportando múltiples fuentes de plugins (relative path, github, url, git-subdir, npm), modos `strict`, canales de release (stable/latest), hosting en GitHub/GitLab o repositorios privados con tokens (`GITHUB_TOKEN`), pre-población de plugins en contenedores vía `CLAUDE_CODE_PLUGIN_SEED_DIR`, restricciones administrativas con `strictKnownMarketplaces` y subcomandos CLI `claude plugin marketplace add/list/remove/update`.
---

---
link: https://code.claude.com/docs/en/plugin-dependencies
description: Explica cómo los autores de plugins declaran dependencias versionadas en el array `dependencies` de `plugin.json` usando rangos semver (`~2.1.0`, `^2.0`), el convenio de tags git `{plugin-name}--v{version}` para resolución de versiones en el marketplace, la intersección de constraints entre múltiples plugins que comparten dependencia, el comportamiento del auto-update frente a rangos, y los errores comunes (`range-conflict`, `dependency-version-unsatisfied`, `no-matching-tag`) con sus soluciones. Requiere Claude Code v2.1.110 o superior.
---

---
link: https://code.claude.com/docs/en/settings
description: Documenta el sistema de configuración de Claude Code mediante el comando `/config` y los archivos `settings.json`, explicando los cuatro ámbitos (Managed, User en `~/.claude/`, Project en `.claude/` y Local en `.claude/settings.local.json`), su precedencia, las variables de entorno admitidas y el listado completo de claves de configuración disponibles.
---

---
link: https://code.claude.com/docs/en/permissions
description: Detalla el sistema de permisos de Claude Code gestionado con `/permissions` y las reglas `allow`/`ask`/`deny` en `settings.json`, los modos de permiso (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`), la sintaxis de reglas por herramienta (Bash con wildcards, Read/Edit con patrones gitignore, WebFetch, MCP, Agent) y opciones gestionadas como `allowManagedPermissionRulesOnly` o los flags `--add-dir`/`--allowedTools`.
---

---
link: https://code.claude.com/docs/en/sandboxing
description: Explica el sandbox nativo de Claude Code que aísla el filesystem y la red para comandos Bash usando Seatbelt en macOS y bubblewrap en Linux/WSL2, activable con `/sandbox` y configurable mediante `sandbox.filesystem.allowWrite/denyWrite/allowRead/denyRead`, `allowedDomains`, `excludedCommands` y variables como `CLAUDE_CODE_NO_FLICKER`; incluye los modos auto-allow y regular, el parámetro `dangerouslyDisableSandbox` y el paquete open source `@anthropic-ai/sandbox-runtime`.
---

---
link: https://code.claude.com/docs/en/agent-sdk/mcp
description: Referencia del SDK de agentes para conectar Claude a servidores MCP: configura servidores stdio (campos `command`, `args`, `env`) y remotos HTTP/SSE (campos `type`, `url`, `headers`) tanto en código (opción `mcpServers` de `query()`) como desde `.mcp.json` con `settingSources`; explica la convención de nombres `mcp__<servidor>__<herramienta>`, el campo `allowedTools` con wildcards, los transportes disponibles (stdio, http, sse, SDK in-process), el campo `env` con expansión `${VAR}` para credenciales, autenticación OAuth2 vía headers y manejo de errores con el mensaje `system/init`.
---

---
link: https://code.claude.com/docs/en/plugins-reference
description: Referencia técnica completa del sistema de plugins de Claude Code: esquemas de componentes (skills en `skills/`, agents en `agents/`, hooks, MCP servers en `.mcp.json` o inline en `plugin.json`, LSP servers en `.lsp.json`), campos de MCP server en plugins (`command`, `args`, `env`, `cwd`, con variables `${CLAUDE_PLUGIN_ROOT}` y `${CLAUDE_PLUGIN_DATA}`), tabla de eventos de hook con tipos `command`/`http`/`mcp_tool`/`prompt`/`agent`, comandos CLI `claude plugin marketplace add/list/remove/update` y herramientas de testing con `--plugin-dir`.
---

---
link: https://code.claude.com/docs/en/terminal-config
description: Guía para optimizar la terminal con Claude Code cubriendo el comando `/theme`, configuración de saltos de línea (Shift+Enter, Ctrl+J, `/terminal-setup` para VS Code/Alacritty/Zed/Warp, extended-keys en tmux, Option-as-Meta en macOS), alertas nativas en iTerm2/Kitty/Ghostty con `allow-passthrough` en tmux, activación de fullscreen con `/tui fullscreen` y el modo Vim habilitado vía `editorMode: "vim"` en `~/.claude.json`.
---

---
link: https://code.claude.com/docs/en/fullscreen
description: Describe el modo de renderizado fullscreen (research preview desde v2.1.89) que usa el buffer alternativo del terminal para eliminar el parpadeo y mantener la memoria estable, activable con `/tui fullscreen` o la variable `CLAUDE_CODE_NO_FLICKER=1`; añade soporte de ratón (clic, selección, rueda con `CLAUDE_CODE_SCROLL_SPEED`), modo transcript con `Ctrl+o` (teclas `/`, `n/N`, `[`, `v`) y la opción `CLAUDE_CODE_DISABLE_MOUSE=1` para conservar la selección nativa.
---

---
link: https://code.claude.com/docs/en/model-config
description: Referencia de configuración del modelo en Claude Code explicando los alias (`default`, `best`, `sonnet`, `opus`, `haiku`, `sonnet[1m]`, `opus[1m]`, `opusplan`), cómo fijarlo con `/model`, el flag `--model`, la variable `ANTHROPIC_MODEL` o el campo `model` en settings; cubre `availableModels` para restringir selección, niveles de esfuerzo con `/effort` y `CLAUDE_CODE_EFFORT_LEVEL`, contexto extendido 1M (`CLAUDE_CODE_DISABLE_1M_CONTEXT`), variables `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL`, `modelOverrides` para Bedrock/Vertex/Foundry y `DISABLE_PROMPT_CACHING*`.
---

---
link: https://code.claude.com/docs/en/fast-mode
description: Describe el modo rápido (research preview, requiere v2.1.36) que ejecuta Opus 4.6 2,5x más veloz con tarifa de 30/150 USD/MTok, activable con `/fast` o `"fastMode": true`; requiere cuenta Claude.ai con extra usage habilitado, puede forzarse a opt-in por sesión con `fastModePerSessionOptIn: true` en managed settings y deshabilitarse con `CLAUDE_CODE_DISABLE_FAST_MODE=1`.
---

---
link: https://code.claude.com/docs/en/voice-dictation
description: Explica la dictación por voz push-to-talk (requiere v2.1.69 y autenticación con cuenta Claude.ai) activada con `/voice` o `"voiceEnabled": true`, con tecla por defecto `Space` rebindable a `voice:pushToTalk` en `~/.claude/keybindings.json`; cubre los 20 idiomas soportados vía el ajuste `language`, fallback a `arecord`/`sox` en Linux y troubleshooting con `tccutil reset Microphone` en macOS.
---

---
link: https://code.claude.com/docs/en/output-styles
description: Documenta los output styles que modifican el system prompt de Claude Code para cambiar rol, tono y formato, con los estilos integrados Default, Explanatory y Learning (este último inserta marcadores `TODO(human)`); se cambian desde `/config` o con el campo `outputStyle` en settings, y se crean como archivos Markdown con frontmatter (`name`, `description`, `keep-coding-instructions`) en `~/.claude/output-styles` o `.claude/output-styles`.
---

---
link: https://code.claude.com/docs/en/statusline
description: Explica cómo configurar una status line personalizada en la parte inferior de Claude Code, que ejecuta un script shell recibiendo JSON con datos de sesión por stdin e imprime lo que quieras mostrar (uso de contexto, costes, rama git); cubre la instalación, el flujo de datos, todos los campos disponibles y ejemplos listos para usar incluyendo barras de progreso y status lines multilínea.
---

---
link: https://code.claude.com/docs/en/agent-sdk/skills
description: Documentación de Agent Skills en el Claude Agent SDK — cómo se cargan skills desde el filesystem mediante `settingSources`/`setting_sources` con valores `"user"` (para `~/.claude/skills/`) y `"project"` (para `.claude/skills/`), cómo habilitarlas añadiendo `"Skill"` a `allowedTools`, y por qué el campo `allowed-tools` del frontmatter del SKILL.md no se aplica en el SDK (el control de herramientas va por `allowedTools` de la query). Incluye ejemplos en Python y TypeScript para `ClaudeAgentOptions`/`query`.
---

---
link: https://code.claude.com/docs/en/keybindings
description: Documenta la personalización de atajos de teclado en `~/.claude/keybindings.json` (requiere v2.1.18) abierta con `/keybindings`, organizada por contextos (`Global`, `Chat`, `Autocomplete`, `Scroll`, etc.) y acciones con formato `namespace:action` (p. ej. `chat:submit`, `app:toggleTodos`, `voice:pushToTalk`); incluye la sintaxis de modificadores (`ctrl`, `alt`, `meta`), chords, desvincular con `null`, atajos reservados como `Ctrl+C`/`Ctrl+D`/`Ctrl+M` e interacción con el modo vim.
---
link: https://code.claude.com/docs/en/cli-reference
description: Referencia completa del CLI de Claude Code. Documenta los comandos (`claude`, `claude -p`, `-c`, `-r`, `claude update`, `claude auth login/logout/status`, `claude mcp`, `claude plugin`, `claude remote-control`, `claude setup-token`, `claude agents`) y todos los flags disponibles (`--add-dir`, `--agent`, `--allowedTools`, `--append-system-prompt`, `--bare`, `--debug`, `--model`, `--permission-mode`, `--resume`, `--worktree`, etc.), incluyendo los cuatro flags para personalizar el system prompt.
---

---
link: https://code.claude.com/docs/en/commands
description: Referencia de los comandos invocables con `/` dentro de una sesión de Claude Code. Lista los comandos built-in y los skills agrupados (cambiar modelo, gestionar permisos, limpiar contexto, ejecutar workflows, etc.), indicando cuáles son built-in codificados en el CLI y cuáles son skills que se pueden personalizar. Los argumentos obligatorios se marcan como `<arg>` y los opcionales como `[arg]`.
---

---
link: https://code.claude.com/docs/en/env-vars
description: Listado exhaustivo de las variables de entorno que controlan Claude Code, agrupadas por categoría - autenticación (`ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`), proveedores cloud (Bedrock, Vertex, Foundry), modelo y effort (`ANTHROPIC_MODEL`, `CLAUDE_CODE_EFFORT_LEVEL`), límites (`API_TIMEOUT_MS`, `BASH_DEFAULT_TIMEOUT_MS`, `CLAUDE_CODE_MAX_OUTPUT_TOKENS`), toggles de funciones (`CLAUDE_CODE_DISABLE_THINKING`, `CLAUDE_CODE_DISABLE_CLAUDE_MDS`), directorios (`CLAUDE_CONFIG_DIR`), seguridad, debugging y telemetría.
---

---
link: https://code.claude.com/docs/en/tools-reference
description: Referencia completa de las herramientas built-in de Claude Code (`Agent`, `Bash`, `Edit`, `Read`, `Write`, `Glob`, `Grep`, `WebFetch`, `WebSearch`, `Skill`, `Monitor`, `LSP`, `PowerShell`, `TaskCreate`/`TaskList`/`TaskUpdate`, `EnterWorktree`, `ToolSearch`, etc.) indicando si requieren permiso. Explica el comportamiento específico de Bash (persistencia de `cd` y `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR`), LSP, Monitor y PowerShell (activado con `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`).
---

---
link: https://code.claude.com/docs/en/plugins-reference
description: Especificaciones técnicas completas del sistema de plugins de Claude Code: esquema completo de `plugin.json` (campos `name`, `version`, `skills`, `agents`, `hooks`, `mcpServers`, `lspServers`, `monitors`, `userConfig`, `channels`, `dependencies`), estructura estándar de directorios del plugin, variables de entorno `${CLAUDE_PLUGIN_ROOT}` y `${CLAUDE_PLUGIN_DATA}`, scopes de instalación (`user`/`project`/`local`/`managed`), referencia CLI (`claude plugin install/uninstall/enable/disable/update/list`), sistema de caché (`~/.claude/plugins/cache`), modo de monitores background, configuración de servidores LSP integrados y herramientas de debugging con `claude --debug`.
---

---
link: https://code.claude.com/docs/en/interactive-mode
description: Referencia de atajos de teclado y funciones del modo interactivo - controles generales (`Ctrl+C`, `Ctrl+O` para transcript, `Ctrl+R` búsqueda inversa, `Esc+Esc` rewind, `Shift+Tab` cambio de permission mode), edición de texto, input multilínea (`Shift+Enter`, `Ctrl+J`), modo Vim completo, bash mode con prefijo `!`, comandos con `/`, menciones de archivos con `@`, tareas en background con `Ctrl+B`, task list con `Ctrl+T`, session recap automático, `/btw` para preguntas laterales y estado de PR en el footer.
---

---
link: https://code.claude.com/docs/en/hooks
description: Referencia completa de hooks en Claude Code: todos los eventos del ciclo de vida (`PreToolUse`, `PostToolUse`, `PermissionRequest`, `SessionStart`, `Stop`, `FileChanged`, `CwdChanged`, `ConfigChange`, `WorktreeCreate`, etc.), esquemas JSON de input/output por evento, tipos de hook (`command`, `http`, `prompt`, `agent`), campo `if` para filtrado fino por argumentos de herramienta (requiere v2.1.85+), códigos de salida (0 permite, 2 bloquea), hooks asíncronos con `async`/`asyncRewake`, variables de entorno `$CLAUDE_PROJECT_DIR`/`$CLAUDE_ENV_FILE`, control de decisiones con `permissionDecision` (`allow`, `deny`, `ask`, `defer`) y `hookSpecificOutput`, y el menú `/hooks` para inspección.
---

---
link: https://code.claude.com/docs/en/agent-sdk/hooks
description: Hooks en el Agent SDK de Claude Code (TypeScript y Python): cómo registrar callbacks en `options.hooks` con `HookMatcher`, tipos de input específicos por evento (`PreToolUseHookInput`, `NotificationHookInput`, `SubagentStopHookInput`, etc.), campos de output (`hookSpecificOutput`, `systemMessage`, `continue`/`continue_`, `updatedInput`, `async`/`async_`), diferencias entre SDKs (SessionStart/SessionEnd solo disponibles en TypeScript), ejemplos de bloqueo, modificación de inputs, auto-aprobación, hooks en cadena y webhooks HTTP desde callbacks.
---

---
link: https://code.claude.com/docs/en/checkpointing
description: Explica el sistema de checkpoints automático que captura el estado del código antes de cada edición de Claude. Documenta el rewind con `Esc+Esc` o `/rewind` y sus opciones (restaurar código, conversación, ambos o resumir desde un punto), la persistencia entre sesiones durante 30 días, y las limitaciones (no rastrea cambios hechos por comandos bash ni modificaciones externas, no sustituye al control de versiones).
---

---
link: https://code.claude.com/docs/en/admin-setup
description: Guía de decisiones para administradores que despliegan Claude Code en una organización: comparativa de API providers (Teams/Enterprise, Console, Bedrock, Vertex, Foundry), mecanismos de entrega de managed settings (server-managed, plist/MDM `com.anthropic.claudecode`, HKLM registry, file-based con rutas exactas por SO, HKCU), tabla de controles de enforcement (`allowManagedPermissionRulesOnly`, `sandbox.enabled`, `allowManagedMcpServersOnly`, `strictKnownMarketplaces`, `minimumVersion`), opciones de visibilidad de uso (OpenTelemetry, analytics dashboard, cost tracking), política de datos (sin entrenamiento en Teams/Enterprise/API, ZDR para Enterprise), y verificación con `/status` para confirmar fuente activa de managed settings.
---

---
link: https://code.claude.com/docs/en/agent-sdk/subagents
description: Documentación de subagentes en el Claude Agent SDK (TypeScript y Python): cómo definirlos programáticamente con el parámetro `agents` en `query()` usando `AgentDefinition` con campos `description`, `prompt`, `tools`, `disallowedTools`, `model` (alias `sonnet`/`opus`/`haiku`/`inherit` o ID completo), `skills`, `memory`, `mcpServers`, `maxTurns`, `background`, `effort`, `permissionMode`; tabla de qué hereda el subagente (CLAUDE.md, subset de tools) y qué no hereda (historial del padre, system prompt del padre, skills); detección de invocación vía tool `Agent` (antes `Task`, renombrado en v2.1.63); cómo reanudar subagentes por `agentId` y `session_id`; y combinaciones típicas de tools por caso de uso.
---

---
link: https://code.claude.com/docs/en/agent-sdk/plugins
description: Cómo cargar plugins desde el filesystem en el Agent SDK de Claude Code (TypeScript y Python) usando el parámetro `plugins` en `query()` con objetos `{type: "local", path: "..."}`, rutas relativas o absolutas, verificación de plugins cargados vía el mensaje `system/init` (campos `plugins` y `slash_commands`), invocación de skills con namespace `plugin-name:skill-name`, y estructura mínima requerida del directorio de plugin (`.claude-plugin/plugin.json` más `skills/`, `commands/`, `agents/`, `hooks/`, `.mcp.json` opcionales).
---

---
link: https://code.claude.com/docs/en/agent-sdk/cost-tracking
description: Documenta cómo rastrear el uso de tokens y costes en el Agent SDK (TypeScript y Python), incluyendo la configuración del prompt cache: TTL por defecto de 5 minutos para API key y proveedores cloud (Bedrock, Vertex, Foundry), cómo habilitar TTL de 1 hora con `ENABLE_PROMPT_CACHING_1H`, campos `cache_creation_input_tokens` y `cache_read_input_tokens`, y nota de que los suscriptores Claude ya tienen TTL de 1 hora automáticamente.
---

---
link: https://code.claude.com/docs/en/hooks
description: Referencia del sistema de hooks de Claude Code - eventos del ciclo de vida (`SessionStart`, `SessionEnd`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PermissionRequest`, `Stop`, `PreCompact`, `FileChanged`, `SubagentStart`, etc.), los cuatro tipos de hook (`command`, `http`, `prompt`, `agent`), formato JSON de configuración con `matcher` y `if`, ubicaciones (`~/.claude/settings.json`, `.claude/settings.json`, plugins), códigos de salida, control de decisiones (allow/deny/ask/defer) y patrones de matcher incluyendo regex y herramientas MCP.
---

---
link: https://code.claude.com/docs/en/plugins-reference
description: Especificación técnica del sistema de plugins - componentes (skills, agents, hooks, MCP servers, LSP servers, monitors), manifiesto `.claude-plugin/plugin.json` con todos sus campos, variables `${CLAUDE_PLUGIN_ROOT}` y `${CLAUDE_PLUGIN_DATA}`, `userConfig` para valores sensibles y no sensibles, estructura de directorios, scopes de instalación (`user`, `project`, `local`, `managed`), caché en `~/.claude/plugins/cache` y comandos CLI (`claude plugin install/uninstall/enable/disable/update/list`).
---

---
link: https://code.claude.com/docs/en/auto-mode-config
description: Referencia de configuración del clasificador de auto mode: campo `autoMode.environment` para declarar repos, buckets y dominios de confianza (con `"$defaults"` para heredar los defaults), campos `autoMode.allow` y `autoMode.soft_deny` para sobreescribir las reglas de excepción y bloqueo, scopes de configuración (usuario `~/.claude/settings.json`, proyecto local `.claude/settings.local.json`, managed settings, flag `--settings`), y subcomandos CLI `claude auto-mode defaults`, `claude auto-mode config` y `claude auto-mode critique` para inspeccionar y validar la configuración efectiva.
---

---
link: https://code.claude.com/docs/en/agent-sdk/overview
description: Visión general del Claude Agent SDK (antes Claude Code SDK) para construir agentes autónomos en Python (`pip install claude-agent-sdk`) y TypeScript (`npm install @anthropic-ai/claude-agent-sdk`). Explica la función central `query()`, herramientas built-in disponibles (Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, Agent, Skill, Monitor, ToolSearch, AskUserQuestion), autenticación con `ANTHROPIC_API_KEY` o proveedores cloud (`CLAUDE_CODE_USE_BEDROCK=1`, `CLAUDE_CODE_USE_VERTEX=1`, `CLAUDE_CODE_USE_FOUNDRY=1`), configuración de MCP servers, sesiones reanudables con `resume=session_id`, y diferencias frente al Client SDK y al CLI.
---

---
link: https://code.claude.com/docs/en/agent-sdk/python
description: Referencia completa del Agent SDK para Python: dataclass `ClaudeAgentOptions` con todos sus campos (`allowed_tools`, `permission_mode`, `max_turns`, `max_budget_usd`, `cwd`, `mcp_servers`, `agents`, `hooks`, `thinking`, `effort`, `setting_sources`, `plugins`, `sandbox`, `resume`, `fork_session`, `enable_file_checkpointing`), `PermissionMode` (valores `"default"`, `"acceptEdits"`, `"plan"`, `"dontAsk"`, `"bypassPermissions"`), tipos de mensaje (`UserMessage`, `AssistantMessage`, `SystemMessage`, `ResultMessage`, `StreamEvent`), `ResultMessage.subtype` (`"success"`, `"error_max_turns"`, `"error_max_budget_usd"`, `"error_during_execution"`), clase `ClaudeSDKClient` para conversaciones continuas con métodos `query()`, `interrupt()`, `receive_response()`, decorador `@tool` para herramientas custom, `create_sdk_mcp_server()` y funciones de gestión de sesiones (`list_sessions`, `get_session_messages`, `rename_session`, `tag_session`).
---

---
link: https://code.claude.com/docs/en/agent-sdk/agent-loop
description: Explica el funcionamiento interno del agent loop del SDK: fases (recibir prompt → evaluar → ejecutar herramientas → repetir → ResultMessage), concepto de turn, ejecución paralela vs secuencial de herramientas (read-only en paralelo con `readOnlyHint`/`readOnly`), niveles de `effort` (`"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`), compactación automática con evento `compact_boundary`, hook `PreCompact` con campo `trigger` (`"manual"`/`"auto"`), `settingSources`/`setting_sources` (valores `"project"`, `"user"`), `ResultMessage.subtype` con todos sus valores de error, `stop_reason` (`"end_turn"`, `"max_tokens"`, `"refusal"`), y gestión del contexto con subagentes.
---

---
link: https://code.claude.com/docs/en/agent-sdk/subagents
description: Documentación de subagentes en el Agent SDK: tres formas de crearlos (programáticamente con parámetro `agents`, ficheros en `.claude/agents/`, subagente built-in `general-purpose`), campos de `AgentDefinition` (`description`, `prompt`, `tools`, `disallowedTools`, `model` con alias `"sonnet"`/`"opus"`/`"haiku"`/`"inherit"`, `skills`, `memory`, `mcpServers`, `maxTurns`, `background`, `effort`, `permissionMode`), requisito de incluir `"Agent"` en `allowedTools`, herencia de contexto (NO hereda historial del padre ni sus skills), limitación de que subagentes no pueden invocar sub-subagentes, detección por `parent_tool_use_id` y nombre de herramienta `"Agent"` (antes `"Task"` < v2.1.63), reanudación con `resume=session_id` + `agentId`, y limitación de 8191 chars en Windows.
---

---
link: https://code.claude.com/docs/en/agent-sdk/hosting
description: Guía para desplegar el Claude Agent SDK en producción: requisitos (Python 3.10+/Node.js 18+, 1 GiB RAM, 5 GiB disco, HTTPS a `api.anthropic.com`), el SDK como proceso de larga duración (no stateless), proveedores de sandbox recomendados (Modal, Cloudflare, Daytona, E2B, Fly Machines, Vercel), cuatro patrones de despliegue (Ephemeral sessions, Long-running sessions, Hybrid sessions, Single containers), configuración del campo `sandbox` en `ClaudeAgentOptions`, y recomendación de fijar `maxTurns` en producción.
---

---
link: https://code.claude.com/docs/en/agent-sdk/plugins
description: Cómo cargar plugins en el Agent SDK mediante el campo `plugins` con objetos `{"type": "local", "path": "..."}` (rutas relativas o absolutas al directorio raíz del plugin que contiene `.claude-plugin/plugin.json`), verificación en el `SystemMessage` de `subtype="init"` (campos `plugins` y `slash_commands`), namespace de skills como `plugin-name:skill-name`, estructura del directorio del plugin (`skills/`, `agents/`, `hooks/`, `.mcp.json`), y localización de plugins instalados via CLI en `~/.claude/plugins/`.
---

---
link: https://code.claude.com/docs/en/channels-reference
description: Guía para construir servidores MCP tipo "channel" que inyectan eventos externos (webhooks, alertas, chats) en una sesión de Claude Code. Documenta el contrato - capacidad `claude/channel`, notificaciones `notifications/claude/channel` con `content` y `meta`, herramientas de respuesta para canales bidireccionales, gating de remitentes para evitar prompt injection, y relay de permisos (`claude/channel/permission`) para aprobar o denegar tool use remotamente con IDs de cinco letras. Incluye ejemplo completo en Bun/TypeScript y requiere `--dangerously-load-development-channels` durante el research preview.
---
link: https://code.claude.com/docs/en/agent-sdk/overview
description: Introduce el Agent SDK (antes Claude Code SDK) para construir agentes en Python y TypeScript con `query()` y `ClaudeAgentOptions`, listando herramientas integradas (Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, AskUserQuestion) y capacidades clave como hooks, subagents, MCP, permisos y sesiones. Incluye instalación (`@anthropic-ai/claude-agent-sdk` / `claude-agent-sdk`), autenticación (Anthropic, Bedrock, Vertex, Foundry) y comparativa con Client SDK y CLI.
---

---
link: https://code.claude.com/docs/en/agent-sdk/quickstart
description: Tutorial paso a paso para crear un agente que detecta y corrige bugs usando `query()` con opciones `allowed_tools=["Read","Edit","Glob"]` y `permission_mode="acceptEdits"`, iterando mensajes con `AssistantMessage` y `ResultMessage`. Explica los modos de permiso (`acceptEdits`, `dontAsk`, `auto`, `bypassPermissions`, `default`) y el error `thinking.type.enabled` que requiere SDK v0.2.111 para Opus 4.7.
---

---
link: https://code.claude.com/docs/en/agent-sdk/agent-loop
description: Detalla el ciclo de ejecución del agente (recibir prompt, evaluar, ejecutar herramientas, repetir, devolver resultado) y los cinco tipos de mensaje (`SystemMessage`, `AssistantMessage`, `UserMessage`, `StreamEvent`, `ResultMessage`). Cubre opciones de control como `max_turns`/`maxTurns`, `max_budget_usd`/`maxBudgetUsd`, niveles de `effort` (low/medium/high/xhigh/max), compactación automática con `compact_boundary` y los subtipos de resultado (`success`, `error_max_turns`, `error_max_budget_usd`, etc.).
---

---
link: https://code.claude.com/docs/en/agent-sdk/claude-code-features
description: Explica cómo cargar configuración filesystem (CLAUDE.md, `.claude/rules/*.md`, skills, hooks, `settings.json`) mediante la opción `setting_sources`/`settingSources` con valores `"user"`, `"project"` y `"local"`. Describe la precedencia, qué NO controla (settings de política, `~/.claude.json`, memoria automática), y cuándo usar skills, subagents, hooks filesystem vs programáticos, y MCP.
---

---
link: https://code.claude.com/docs/en/agent-sdk/sessions
description: Describe la gestión de sesiones para persistir conversaciones - uso de `ClaudeSDKClient` (Python) o `continue: true` (TypeScript) para multi-turno automático, captura de `session_id` desde `ResultMessage`, y opciones `resume` y `fork_session`/`forkSession` para retomar o bifurcar historiales. Incluye almacenamiento en `~/.claude/projects/<encoded-cwd>/*.jsonl`, resumen entre hosts, y funciones utilitarias (`listSessions()`, `getSessionMessages()`, `renameSession()`, `tagSession()`).
---

---
link: https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode
description: Compara los dos modos de entrada del SDK - Streaming Input Mode (recomendado, con `AsyncGenerator` y `ClaudeSDKClient`) que permite imágenes, mensajes en cola, interrupciones y hooks; frente a Single Message Input para consultas one-shot o entornos stateless como lambdas. Muestra ejemplos con `yield` de mensajes user con bloques `text` e `image` base64.
---

---
link: https://code.claude.com/docs/en/agent-sdk/user-input
description: Explica cómo surfacer peticiones de Claude al usuario mediante el callback `can_use_tool`/`canUseTool`, que recibe `tool_name`, `input_data` y contexto, y devuelve `PermissionResultAllow(updated_input=...)` o `PermissionResultDeny(message=...)`. Cubre el manejo de la herramienta `AskUserQuestion` con preguntas de opción múltiple (campos `question`, `header`, `options`, `multiSelect`), previsualizaciones HTML/markdown en TypeScript, y el workaround de Python que requiere hook `PreToolUse` devolviendo `{"continue_": True}`.
---

---
link: https://code.claude.com/docs/en/agent-sdk/streaming-output
description: Explica cómo activar streaming de tokens en tiempo real con `include_partial_messages=True` (Python) o `includePartialMessages: true` (TypeScript) para recibir `StreamEvent`/`SDKPartialAssistantMessage` con eventos raw de la API (`message_start`, `content_block_delta` con `text_delta` o `input_json_delta`, `message_stop`). Advierte de incompatibilidades con `max_thinking_tokens` y salida estructurada.
---

---
link: https://code.claude.com/docs/en/agent-sdk/structured-outputs
description: Describe cómo obtener JSON validado desde el agente definiendo un JSON Schema y pasándolo en `output_format`/`outputFormat` con `type: "json_schema"`; el resultado aparece en `ResultMessage.structured_output`. Incluye integración con Zod (`z.toJSONSchema()`) en TypeScript y Pydantic (`.model_json_schema()`) en Python, y el subtipo de error `error_max_structured_output_retries`.
---

---
link: https://code.claude.com/docs/en/agent-sdk/custom-tools
description: Guía para definir herramientas personalizadas con el decorador `@tool` (Python) o helper `tool()` (TypeScript), y empaquetarlas en un servidor MCP in-process mediante `create_sdk_mcp_server`/`createSdkMcpServer` pasado en `mcp_servers`. Cubre el formato de nombres `mcp__{server}__{tool}`, anotaciones (`readOnlyHint`, `destructiveHint`, etc.), manejo de errores con `isError: true`, y retorno de bloques `text`, `image` (base64) y `resource`.
---

---
link: https://code.claude.com/docs/en/agent-sdk/mcp
description: Explica cómo conectar servidores MCP externos configurando `mcp_servers`/`mcpServers` con transports stdio (`command`, `args`, `env`), HTTP (`type: "http"`, `url`, `headers`) o SSE (`type: "sse"`), o cargándolos desde `.mcp.json`. Detalla la convención de nombres `mcp__<server>__<tool>`, aprobación con `allowedTools` y comodines, autenticación OAuth2/Bearer y el chequeo de estado de conexión en `system/init`.
---

---
link: https://code.claude.com/docs/en/agent-sdk/tool-search
description: Describe la función Tool Search que carga definiciones de herramientas on-demand cuando hay muchas (hasta 10.000), configurable con la variable de entorno `ENABLE_TOOL_SEARCH` (valores `true`, `auto`, `auto:N`, `false`). Explica umbrales por porcentaje del context window, requisito de Sonnet 4 u Opus 4+, y prácticas para optimizar descripciones y nombres de herramientas.
---

---
link: https://code.claude.com/docs/en/agent-sdk/subagents
description: Enseña a definir subagents programáticamente con el parámetro `agents` y `AgentDefinition` (campos `description`, `prompt`, `tools`, `model`, `skills`, `memory`, `mcpServers`), requiriendo `Agent` en `allowedTools`. Cubre invocación automática vs explícita, detección vía bloques `tool_use` con `name === "Agent"` y `parent_tool_use_id`, reanudación de subagents con `agentId` y restricciones de herramientas por subagent.
---

---
link: https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts
description: Compara cuatro métodos para personalizar el system prompt - archivos CLAUDE.md vía `settingSources`, output styles guardados en `~/.claude/output-styles/` o `.claude/output-styles/`, el preset `{type: "preset", preset: "claude_code", append: "..."}` con opción `excludeDynamicSections` para mejorar caching, y un `systemPrompt` personalizado como string. Muestra cuándo usar cada aproximación.
---

---
link: https://code.claude.com/docs/en/agent-sdk/slash-commands
description: Explica cómo descubrir comandos slash disponibles en `system/init.slash_commands`, enviar builtins como `/compact` o `/context` como prompts, y crear comandos personalizados en `.claude/commands/*.md` (legacy) o `.claude/skills/` con frontmatter YAML (`allowed-tools`, `description`, `model`, `argument-hint`). Incluye placeholders de argumentos (`$1`, `$ARGUMENTS`), ejecución de bash entre backticks y referencias de archivos con `@`.
---

---
link: https://code.claude.com/docs/en/agent-sdk/skills
description: Explica que las Skills son artefactos filesystem (`.claude/skills/<name>/SKILL.md`) descubiertos mediante `setting_sources` incluyendo `"user"` o `"project"`, y requieren `"Skill"` en `allowed_tools`. Aclara que el SDK no ofrece API programática para registrar Skills y que el campo `allowed-tools` del frontmatter solo aplica en CLI, no en SDK.
---

---
link: https://code.claude.com/docs/en/agent-sdk/plugins
description: Describe cómo cargar plugins locales pasando el parámetro `plugins` con entradas `{type: "local", path: "..."}` apuntando a directorios con `.claude-plugin/plugin.json`. Los plugins pueden incluir skills, agents, hooks y MCP servers; sus comandos/skills aparecen namespaced como `plugin-name:skill-name` en `slash_commands` del mensaje init.
---

---
link: https://code.claude.com/docs/en/agent-sdk/permissions
description: Detalla el orden de evaluación de permisos (hooks -> deny rules -> permission mode -> allow rules -> `canUseTool`) y documenta las opciones `allowed_tools`/`disallowed_tools` y los modos `default`, `dontAsk`, `acceptEdits`, `bypassPermissions`, `plan` y `auto` (solo TypeScript). Incluye el método dinámico `set_permission_mode()`/`setPermissionMode()` para cambiar modo a mitad de sesión.
---

---
link: https://code.claude.com/docs/en/agent-sdk/hooks
description: Guía completa sobre hooks como callbacks para eventos del agente (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `UserPromptSubmit`, `Stop`, `SubagentStart/Stop`, `PreCompact`, `PermissionRequest`, `Notification`, y en TypeScript `SessionStart/End`, `TeammateIdle`, `TaskCompleted`, etc.). Muestra configuración con `HookMatcher`, outputs con `permissionDecision` (allow/deny/ask), `updatedInput`, `systemMessage`, `additionalContext` y el modo asíncrono (`async: true`).
---

---
link: https://code.claude.com/docs/en/agent-sdk/typescript
description: Referencia completa de la API del Agent SDK de TypeScript para Claude Code: funciones `query()`, `startup()`, `tool()`, `createSdkMcpServer()`, gestión de sesiones, tipos de mensajes y la definición completa del tipo `HookEvent` con todos los eventos disponibles (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `Notification`, `UserPromptSubmit`, `SessionStart`, `SessionEnd`, `Stop`, `SubagentStart`, `SubagentStop`, `PreCompact`, `PermissionRequest`, `Setup`, `TeammateIdle`, `TaskCompleted`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove`), junto con la interfaz `HookCallbackMatcher` y los tipos de input/output por hook.
---

---
link: https://code.claude.com/docs/en/agent-sdk/file-checkpointing
description: Explica el checkpointing de archivos modificados por Write/Edit/NotebookEdit activando `enable_file_checkpointing=True` y `extra_args={"replay-user-messages": None}` para recibir UUIDs en mensajes de usuario. Usa `rewind_files(checkpoint_id)`/`rewindFiles()` tras reanudar la sesión con `resume=session_id` y prompt vacío para restaurar archivos al estado previo; no afecta la historia conversacional ni cambios hechos por Bash.
---

---
link: https://code.claude.com/docs/en/agent-sdk/session-storage
description: Documenta el adaptador `SessionStore` para persistir transcripts de sesión en almacenamiento externo (S3, Redis, Postgres) con los métodos requeridos `append`/`load` y los opcionales `listSessions`/`delete`/`listSubkeys`. Explica `SessionKey` (campos `projectKey`, `sessionId`, `subpath`), `InMemorySessionStore` para desarrollo/tests, el patrón dual-write (el SDK escribe localmente y luego sincroniza al store), que `forkSession` reescribe los `sessionId` internos (no es una copia byte a byte), y que `sessionStore` es incompatible con `persistSession: false` y con `enableFileCheckpointing`. Incluye referencias a adaptadores de ejemplo para S3 (`S3SessionStore`), Redis (`RedisSessionStore`) y Postgres (`PostgresSessionStore`) en el repositorio oficial.

---
link: https://code.claude.com/docs/en/agent-sdk/cost-tracking
description: Describe cómo leer tokens y coste estimado desde `ResultMessage.total_cost_usd` y `usage`, diferenciando uso por paso (deduplicando por `message.id` en llamadas paralelas) y por modelo (`model_usage`/`modelUsage`). Advierte que `total_cost_usd` es una estimación cliente, no facturación autoritativa, y explica los campos de cache (`cache_creation_input_tokens`, `cache_read_input_tokens`).
---

---
link: https://code.claude.com/docs/en/agent-sdk/observability
description: Explica cómo exportar telemetría OpenTelemetry (métricas, eventos de log, traces) configurando variables de entorno como `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER`, `OTEL_TRACES_EXPORTER` (con `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`) y `OTEL_EXPORTER_OTLP_ENDPOINT`. Documenta los spans emitidos (`claude_code.interaction`, `claude_code.llm_request`, `claude_code.tool`, `claude_code.hook`) y variables para contenido sensible (`OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_LOG_TOOL_CONTENT`).
---

---
link: https://code.claude.com/docs/en/agent-sdk/todo-tracking
description: Explica el seguimiento de tareas mediante la herramienta built-in `TodoWrite` que crea listas con estados `pending`, `in_progress` y `completed`. Muestra cómo monitorizar los cambios inspeccionando bloques `tool_use` con `name === "TodoWrite"` en `AssistantMessage` para construir UIs de progreso en tiempo real.
---

---
link: https://code.claude.com/docs/en/agent-sdk/hosting
description: Guía de hospedaje del SDK en producción con contenedores sandbox, describiendo requisitos (Python 3.10+/Node.js 18+, 1GiB RAM, HTTPS a api.anthropic.com) y proveedores (Modal, Cloudflare Sandboxes, Daytona, E2B, Fly Machines, Vercel Sandbox). Detalla cuatro patrones de despliegue - Ephemeral Sessions, Long-Running Sessions, Hybrid Sessions y Single Containers.
---

---
link: https://code.claude.com/docs/en/agent-sdk/secure-deployment
description: Guía de despliegue seguro cubriendo amenazas (prompt injection), features built-in (permisos, parseo AST de bash, sandbox mode) y tecnologías de aislamiento comparadas (sandbox-runtime, Docker con `--cap-drop`, `--security-opt`, `--network none` y socket Unix, gVisor/runsc, VMs Firecracker). Detalla el patrón proxy para credenciales con `ANTHROPIC_BASE_URL` o `HTTP_PROXY`/`HTTPS_PROXY`, y montajes filesystem read-only evitando directorios sensibles (`.env`, `~/.aws`, `~/.ssh`).
---

---
link: https://code.claude.com/docs/en/agent-sdk/typescript
description: Referencia completa de la API del SDK TypeScript, incluyendo las funciones `query()`, `startup()`, `tool()`, `createSdkMcpServer()` y utilidades de sesión (`listSessions()`, `getSessionMessages()`, `renameSession()`, `tagSession()`). Documenta la interfaz `Query` con métodos `interrupt()`, `rewindFiles()`, `setPermissionMode()`, el objeto `Options` con 40+ propiedades, y los tipos de mensaje SDK (`SDKAssistantMessage`, `SDKUserMessage`, `SDKResultMessage`, etc.) junto a esquemas de herramientas built-in.
---

---
link: https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview
description: Preview inestable de la API V2 del SDK TypeScript que reemplaza los async generators de V1 por un patrón session-based con `unstable_v2_createSession()`, `unstable_v2_resumeSession()` y `unstable_v2_prompt()`, y los métodos `session.send()`, `session.stream()` y `session.close()`. Soporta `await using` para cleanup automático (TS 5.2+); algunas features como forking siguen siendo solo de V1.
---

---
link: https://code.claude.com/docs/en/agent-sdk/python
description: Referencia completa de la API Python del Agent SDK, documentando la función `query()`, el decorador `@tool`, `create_sdk_mcp_server()` y utilidades de sesión (`list_sessions()`, `get_session_messages()`, etc.). Describe la clase `ClaudeSDKClient` para conversaciones multi-turno, `ClaudeAgentOptions` con 30+ campos, `AgentDefinition` para subagents, configs MCP (`McpStdioServerConfig`, `McpSSEServerConfig`), tipos de mensaje (`UserMessage`, `AssistantMessage`, `ResultMessage`, `StreamEvent`) y todos los eventos de hook con sus callbacks tipados.
---

---
link: https://code.claude.com/docs/en/agent-sdk/migration-guide
description: Guía para migrar del Claude Code SDK al Claude Agent SDK, cambiando paquetes (`@anthropic-ai/claude-code` -> `@anthropic-ai/claude-agent-sdk`, `claude-code-sdk` -> `claude-agent-sdk`) y renombrando `ClaudeCodeOptions` a `ClaudeAgentOptions`. Enumera los breaking changes de v0.1.0 - el system prompt de Claude Code ya no es el default (requiere `systemPrompt: {type: "preset", preset: "claude_code"}`) y los setting sources ya no cargan automáticamente sin pasar `settingSources`/`setting_sources`.
---
link: https://code.claude.com/docs/en/whats-new
description: Página índice del "What's New" de Claude Code que recopila los digests semanales de novedades destacadas, con fragmentos de código, demos y enlaces. Incluye resúmenes introductorios de las semanas 13, 14 y 15 de 2026, y remite al changelog completo para bugs y mejoras menores.
---

---
link: https://code.claude.com/docs/en/whats-new/2026-w15
description: Digest de la semana 15 (6-10 de abril de 2026, versiones v2.1.92 a v2.1.101) que anuncia Ultraplan (preview de planificación en la nube desde el CLI con revisión en navegador), la herramienta Monitor (streaming de eventos de procesos en segundo plano hacia la conversación), `/loop` autoajustable, `/autofix-pr` desde terminal y `/team-onboarding` para generar guías de ramp-up. Incluye mejoras adicionales como vista Focus con Ctrl+O, asistentes guiados para Bedrock y Vertex AI, layout con pestañas en `/agents`, nivel de esfuerzo "high" por defecto, desglose por modelo en `/cost`, confianza en el almacén de CAs del SO y permisos endurecidos del Bash tool.
---

---
link: https://code.claude.com/docs/en/whats-new/2026-w14
description: Digest de la semana 14 (30 de marzo - 3 de abril de 2026, versiones v2.1.86 a v2.1.91) que introduce computer use en el CLI (preview para controlar apps nativas desde la terminal), `/powerup` con lecciones interactivas animadas, renderizado sin parpadeo mediante alt-screen (`CLAUDE_CODE_NO_FLICKER`), override por herramienta del tope de tamaño de resultados MCP hasta 500K (`anthropic/maxResultSizeChars`), y ejecutables de plugins en el PATH del Bash tool mediante un directorio `bin/`. Añade extras como el hook `PermissionDenied`, valor `defer` en `PreToolUse`, `/buddy`, `disableSkillShellExecution`, Edit sobre archivos vistos con cat/sed, y mejoras de modo voz.
---

---
link: https://code.claude.com/docs/en/whats-new/2026-w13
description: Digest de la semana 13 (23-27 de marzo de 2026, versiones v2.1.83 a v2.1.85) que presenta Auto mode en research preview (clasificador que gestiona los permisos automáticamente), computer use integrado en la app de escritorio, PR auto-fix en Claude Code Web, búsqueda en transcripciones con "/", una herramienta nativa de PowerShell para Windows (`CLAUDE_CODE_USE_POWERSHELL_TOOL`) y hooks condicionales con campo "if". Incluye mejoras como `userConfig` público en plugins, chips [Image #N] para imágenes pegadas, directorio `managed-settings.d/`, hooks `CwdChanged` y `FileChanged`, `initialPrompt` en agentes y atajos tipo readline (`Ctrl+X Ctrl+E`).
---

---
link: https://code.claude.com/docs/en/legal-and-compliance
description: Recopila los acuerdos legales y de cumplimiento aplicables a Claude Code, incluyendo los Términos Comerciales y de Consumidor, la extensión automática del BAA sanitario cuando hay Zero Data Retention activado, la política de uso aceptable de Anthropic y las reglas de autenticación (OAuth para planes Free/Pro/Max/Team/Enterprise frente a API keys para desarrolladores del Agent SDK). Enlaza además al Trust Center, al Transparency Hub y al formulario de HackerOne para reportar vulnerabilidades de seguridad.
---

---
link: https://code.claude.com/docs/en/terminal-guide
description: Guía paso a paso para usuarios novatos de terminal que explica cómo abrir una terminal en macOS, Linux y Windows, instalar Claude Code con `curl -fsSL https://claude.ai/install.sh | bash` (macOS/Linux), `irm https://claude.ai/install.ps1 | iex` (PowerShell) o el equivalente en CMD, y arrancar con `claude`. Incluye primeros pasos (usar flechas, `Esc` para interrumpir, `Ctrl+D` o `exit` para salir, `/help`), ejemplos de prompts básicos y troubleshooting para errores comunes como `command not found`, `irm is not recognized`, `git-bash` no encontrado con `CLAUDE_CODE_GIT_BASH_PATH`, y errores SSL/TLS.
---

---
link: https://code.claude.com/docs/en/amazon-bedrock
description: Explica cómo usar Claude Code con Amazon Bedrock: wizard de login (`/setup-bedrock`), configuración manual con variables de entorno (`CLAUDE_CODE_USE_BEDROCK=1`, `AWS_REGION`, `AWS_BEARER_TOKEN_BEDROCK`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`), opciones de autenticación AWS (CLI, access key, SSO, Bedrock API keys), configuración de IAM, endpoint Mantle (`CLAUDE_CODE_USE_MANTLE=1`), AWS Guardrails mediante `ANTHROPIC_CUSTOM_HEADERS`, y `awsAuthRefresh`/`awsCredentialExport` para refresco automático de credenciales.
---

---
link: https://code.claude.com/docs/en/google-vertex-ai
description: Explica cómo usar Claude Code con Google Vertex AI: wizard de login (`/setup-vertex`), configuración manual con variables de entorno (`CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION`, `ANTHROPIC_VERTEX_PROJECT_ID`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`, `VERTEX_REGION_CLAUDE_*`), autenticación mediante Application Default Credentials o service account key, permisos IAM (`roles/aiplatform.user`, `aiplatform.endpoints.predict`), soporte a ventana de contexto 1M y troubleshooting de errores 404/429.
---
