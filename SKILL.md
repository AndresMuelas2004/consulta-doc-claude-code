---
name: consulta-doc-claude-code
description: Actívate ante CUALQUIER cosa relacionada con Claude Code, por mínima que sea — ya sean dudas a resolver (cómo funciona X, qué hace Y, por qué Z) como recolección de información previa para realizar una tarea que lo involucre (crear skills, subagentes, hooks, MCPs, equipos de agentes, slash commands, cambios en configuración/settings.json, Agent SDK, CLI flags, plugins, integraciones, memoria, permisos, troubleshooting, etc.). Si el tema roza Claude Code aunque sea de lejos, activa la skill: es preferible pasarse que quedarse corto. NO se activa para programación general ajena a Claude Code ni para la API de Anthropic directa que no pase por Claude Code. También se invoca manualmente con /consulta-doc-claude-code <texto>. SIEMPRE debe pasarse `$ARGUMENTS` (la duda concreta o la petición de información concreta); invocarla sin argumentos es un error de uso.
argument-hint: duda concreta sobre Claude Code o petición de información preparatoria (obligatorio) — p. ej. "cómo configurar un hook PostToolUse", "qué hace el flag --bare" o "lee la doc sobre skills porque voy a crear una"
allowed-tools: Read, Write, Edit, WebFetch, WebSearch, Grep, Glob
context: fork
agent: consulta-doc-agent
---

# consulta-doc-claude-code

Skill para resolver cualquier duda sobre Claude Code o reunir información oficial de referencia sobre su funcionamiento, consultando siempre la documentación oficial en https://code.claude.com/docs. La salida se basa siempre en contenido actual de la doc, no en conocimiento previo del modelo.

## Por qué esta skill existe

Claude Code evoluciona muy rápido (novedades casi semanales en el changelog). Responder o actuar basándose solo en entrenamiento es arriesgado: podrías mencionar flags o campos que ya no existen, o ignorar features recientes. Esta skill obliga a consultar la fuente oficial antes de responder o antes de ejecutar una tarea que dependa de cómo funciona Claude Code, garantizando precisión.

## Archivo de referencias cruzadas

Junto a este `SKILL.md` hay un `reference.md`: catálogo de bloques separados por `---` con pares `link`/`description`, uno por cada apartado de la documentación oficial. Las descripciones son específicas (mencionan flags, comandos, variables de entorno, nombres de features) para que el emparejamiento consulta→URL sea preciso.

Este archivo se **autoactualiza** en cada ejecución de la skill: si durante la resolución aparece una URL oficial nueva que no estaba, se añade; si una URL del reference.md ya no existe al intentar visitarla, se elimina. De esta forma el catálogo se mantiene sincronizado con la doc oficial sin intervención manual.

## Workflow

### 1. Identifica la consulta

La consulta es **siempre** `$ARGUMENTS`. No hay fallback: quien invoca la skill (modelo principal o usuario vía slash command) tiene la obligación de pasar el texto explícito como argumento. No intentes inferirlo del historial de la conversación: aunque puedas verlo, la skill está pensada para ceñirse a lo que llega en `$ARGUMENTS`.

- Trabaja exclusivamente sobre lo que dice `$ARGUMENTS`.
- Si es ambiguo, reformúlalo brevemente para ti mismo antes de proceder (no preguntes al usuario; esta skill está pensada para resolver/consultar, no para conversar).
- Si `$ARGUMENTS` llega vacío, es un error de invocación: responde con un mensaje corto pidiendo que se reinvoque pasando la consulta como argumento y termina.

### 2. En paralelo: lee el reference.md y lanza una búsqueda web

En la misma respuesta emite DOS llamadas en paralelo:

- `Read` sobre `${CLAUDE_SKILL_DIR}/reference.md`.
- `WebSearch` con la query `site:code.claude.com/docs <términos clave de la consulta>`. El prefijo `site:code.claude.com/docs` es obligatorio: el reference.md solo cataloga páginas de ese dominio, así que cualquier resultado fuera de él es irrelevante para la auto-actualización.

El objetivo de la búsqueda paralela es doble: detectar páginas oficiales nuevas que aún no estén en `reference.md` y validar bajo demanda que las URLs seleccionadas siguen existiendo.

### 3. Selecciona las URLs relevantes del reference.md

Escanea las descripciones y elige las URLs cuyo `description` encaje mejor con la consulta. Criterios:

- **Coincidencia de concepto**: la descripción menciona el tema de la consulta.
- **Coincidencia de términos técnicos**: aparecen los flags, comandos, archivos, variables o nombres de features que el usuario mencionó.
- **Nivel de especificidad**: si la consulta es sobre algo muy concreto, prioriza la página específica por encima de la de overview.

Si ninguna descripción encaja claramente, escoge la aproximación más cercana y avisa en la salida final de forma bastante clara como "WARNING!" que la doc no parece cubrir el tema de forma explícita.

### 4. Procesa los resultados de la búsqueda web

Del resultado de `WebSearch`, quédate con **todos los resultados relevantes para la consulta que pertenezcan al dominio `code.claude.com/docs`**, igual que harías en una búsqueda manual: si hay tres páginas que parecen relacionadas, captura las tres; si solo hay una útil, solo una; si ninguna encaja, ninguna. Prioriza por relevancia al tema concreto, no por posición absoluta en la SERP.

Tres casos respecto al dominio:

- **Caso A — los resultados relevantes son de `code.claude.com/docs`**: captura todos ellos como URLs candidatas.
- **Caso B — el primer resultado global NO es de `code.claude.com/docs` pero hay otros más abajo que sí y son relevantes**: captura los de `code.claude.com/docs` como URLs candidatas, Y apunta que la búsqueda web devolvió primero un resultado ajeno al dominio oficial (esto se mencionará al final de la salida).
- **Caso C — ningún resultado del dominio oficial es relevante para la consulta**: no hay URLs candidatas de la búsqueda; salta directamente al paso 6 con solo las URLs seleccionadas del reference.md.

### 5. Compara URLs candidatas vs TODO el reference.md (normalizada)

Compara **cada URL candidata** contra **TODAS las URLs presentes en `reference.md`** (no solo contra las que seleccionaste en el paso 3) de forma **normalizada**: dos URLs cuentan como iguales si apuntan al mismo contenido aunque difieran en trailing slash, anchor (`#seccion`) o query params (`?foo=bar`). No compares literalmente byte a byte: si el contenido es el mismo, no tiene sentido visitar la página dos veces ni duplicar entrada en el reference.md.

Es importante comparar contra el archivo completo y no solo contra las URLs seleccionadas: una URL que existe en `reference.md` pero que no fue seleccionada en el paso 3 (porque no encajaba con la consulta actual) ya está catalogada y NO debe añadirse de nuevo. Si solo se compara contra las seleccionadas, el archivo crecería con duplicados con cada invocación.

Para cada URL candidata:

- **Coincide (normalizada) con alguna ya presente en `reference.md`**: descártala como candidata a nueva entry. Si además es relevante para la consulta actual y no estaba en las seleccionadas del paso 3, añádela al conjunto final de URLs a visitar (sin marcarla como nueva entry).
- **NO coincide con ninguna del `reference.md`**: añádela al conjunto final de URLs a visitar y márcala como **candidata a nuevo entry** en reference.md.

El conjunto final de URLs a visitar = URLs seleccionadas del reference.md (paso 3) + URLs candidatas que han pasado el filtro (nuevas o ya catalogadas pero no seleccionadas).

### 6. Consulta las URLs con WebFetch

Para cada URL del conjunto final (reference + posible nueva), llama a `WebFetch` en paralelo (múltiples tool calls en la misma respuesta) con un prompt enfocado que extraiga solo la información relevante a la consulta, no el contenido completo de la página. Ejemplo:

- URL: `https://code.claude.com/docs/en/hooks`
- Prompt al WebFetch: "Explica cómo se configura un hook PostToolUse en settings.json, con los campos necesarios (matcher, command, type) y un ejemplo completo."

**Detección de links rotos (solo para URLs procedentes del reference.md)**: si un WebFetch devuelve 404 o redirección permanente hacia una URL ajena al dominio oficial, **marca esa URL como rota**. Los errores transitorios (500, timeout, rate limit) NO cuentan como rota — simplemente procede con las URLs que sí respondieron. No hagas chequeos adicionales de links no usados: el saneamiento es estrictamente bajo demanda.

Si una URL del reference.md se marca rota, intenta resolver la consulta con las demás URLs disponibles. Si WebFetch falla y no hay contenido suficiente en general, usa `WebSearch` como fallback adicional.

### 7. Actualiza el reference.md si procede

Usa `Edit` sobre `${CLAUDE_SKILL_DIR}/reference.md` para reflejar los cambios detectados:

- **Añadir URLs nuevas** (una por cada candidata del paso 5 cuyo WebFetch haya devuelto contenido válido): añade al FINAL del archivo un bloque por URL, en EXACTAMENTE el mismo formato que los existentes, usando como descripción un resumen de 1-3 frases en español que saque del contenido que acabas de fetchear, mencionando los conceptos, flags, comandos o variables concretos que aparezcan en esa página:

  ```
  ---
  link: <URL-nueva-exacta-tal-como-aparece>
  description: <1-3 frases en español con conceptos/flags/comandos específicos>
  ---
  ```

  Respeta el salto de línea en blanco entre bloques que hay en el resto del archivo.

- **Eliminar URL rota**: por cada URL que marcaste como rota en el paso 6, elimina su bloque completo del archivo (las tres líneas `---` / `link: ...` / `description: ...` / `---`, junto con el salto de línea que lo separa del siguiente bloque, para no dejar separadores huérfanos).

Si no hay ni URL nueva ni URL rota, NO toques el archivo.

### 8. Clasifica el tipo de invocación y redacta según corresponda

Antes de escribir nada en `template.md`, clasifica la invocación en uno de estos dos modos:

- **Modo DUDA**: `$ARGUMENTS` formula una pregunta o consulta concreta que espera una respuesta teórica que la cierre (p. ej. "cómo configuro un hook PostToolUse", "qué hace `--bare`", "por qué mi skill no se invoca"). La salida final ES la respuesta a esa duda.

- **Modo INFO-TAREA**: `$ARGUMENTS` pide reunir información sobre algún aspecto de Claude Code como paso preparatorio para una tarea distinta que el invocador va a realizar después (p. ej. "lee la doc sobre skills porque voy a crear una", "consulta cómo se configuran los hooks para montar uno nuevo", "reúne info sobre MCP servers"). Aquí NO se quiere una explicación teórica: el contenido útil ya queda en el contexto principal gracias a los WebFetch del paso 6, así que el modelo principal puede proceder con la tarea con ese material. La skill solo deja constancia de qué se consultó y del estado del catálogo.

**Reglas sintácticas duras** (aplícalas en orden; la primera que encaje decide el modo, sin excepciones):

1. Si `$ARGUMENTS` empieza con un imperativo de recolección (`Lee`, `Consulta`, `Reúne`, `Busca`, `Revisa`, `Mira`, `Trae`, `Recopila`) seguido en la misma frase de una cláusula con `porque` o `para` que justifica una tarea posterior (p. ej. `Consulta X porque voy a crear Y`, `Lee sobre Z para montar W`) → **INFO-TAREA siempre**. No la degrades a DUDA aunque el tema parezca concreto.
2. Si `$ARGUMENTS` menciona explícitamente una tarea posterior que el invocador va a realizar (`voy a crear`, `voy a montar`, `voy a configurar`, `antes de hacer`, `como paso previo a`, `quiero personalizar`, `quiero implementar`, `quiero configurar`, `para mi próximo/a`, `de cara a`), aunque el verbo inicial sea interrogativo → **INFO-TAREA**. La tarea posterior es la señal dominante y manda sobre el signo de pregunta.
3. Si `$ARGUMENTS` empieza con signo `¿` o con un verbo interrogativo directo (`cómo`, `qué`, `por qué`, `cuándo`, `dónde`, `cuál`, `cuáles`) y NO se cumple ninguna de las dos reglas anteriores → **DUDA siempre**.

Si ninguna regla dura aplica, usa las pistas heurísticas de abajo como fallback; si aun así queda genuinamente ambiguo, prefiere DUDA.

Pistas heurísticas (fallback):

- Verbos interrogativos directos ("cómo/qué/por qué/cuándo/dónde") → DUDA.
- Imperativos de recolección ("lee", "consulta", "mira", "reúne", "busca") o mención explícita de una tarea posterior ("para crear...", "antes de hacer...", "como paso previo a...") → INFO-TAREA.
- Si es genuinamente ambiguo, prefiere DUDA.

Sea cual sea el modo, al final sobrescribirás `${CLAUDE_SKILL_DIR}/template.md` íntegramente con `Write` (no `Edit`). El archivo debe contener EXACTAMENTE lo que el modelo principal imprimirá al usuario: sin comentarios HTML, sin meta-instrucciones, sin delimitadores, sin comillas envolventes.

#### 8.A — Modo DUDA

Redacta la respuesta en **ESPAÑOL** siguiendo estas pautas:

- Responde directamente a la duda, sin paja.
- Cita la URL de origen cuando aporte valor, en formato Markdown clicable: `[texto](URL)`.
- Si hay varias fuentes, organízalas lógicamente: primero la respuesta principal, luego matices o configuración relacionada.
- No inventes detalles que no aparezcan en las fuentes consultadas.
- Si la doc oficial contradice conocimiento previo que pudieras tener, prevalece la doc.
- Incluye fragmentos de código o configuración (settings.json, variables de entorno, flags CLI) literalmente tal como aparecen en la doc.
- MUST RESPECT! Solo puedes dar información que aparezca en la documentación oficial que acabas de visitar, no inventes nada.

**Al final de la respuesta incluye OBLIGATORIAMENTE estos bloques cortos**:

1. **URLs visitadas**: lista clicable en Markdown de las URLs que realmente se usaron para resolver la duda.

2. **Estado de reference.md**: UNA frase que diga si el archivo se ha actualizado o no. Opciones:
   - Sin cambios: `reference.md sin cambios.`
   - Solo se añadió una URL nueva: `reference.md actualizado: añadido [URL].`
   - Solo se eliminó una URL rota: `reference.md actualizado: eliminado [URL] (link roto).`
   - Ambos: `reference.md actualizado: añadido [URL1]; eliminado [URL2] (link roto).`

3. **Aviso de búsqueda web** (solo si aplica el Caso B del paso 4): una frase del tipo `Nota: la búsqueda web devolvió primero un resultado ajeno al dominio oficial ([URL]); se usó el primer resultado oficial que apareció más abajo.`

Sobrescribe `${CLAUDE_SKILL_DIR}/template.md` con la respuesta completa **envuelta entre los marcadores HTML `<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->` y `<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->`**, que deben ser la primera y la última línea del archivo respectivamente, con una línea en blanco a continuación y antes, así:

```
<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->

... (aquí la respuesta completa en español: título, cuerpo, URLs visitadas, estado de reference.md, aviso si aplica) ...

<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->
```

Los marcadores son comentarios HTML, por lo que no se renderizan en Markdown y el usuario no los ve. Su única función es servir de cinturón de seguridad: si por error el paso 9 falla y el sub-agente devuelve el contenido en su mensaje en lugar de la frase meta, los marcadores señalizan inequívocamente al modelo principal que todo lo que hay entre ellos es salida literal de la skill y debe imprimirse tal cual, sin resumir ni parafrasear.

#### 8.B — Modo INFO-TAREA

**LEE ESTO CON MUCHA ATENCIÓN. Es la parte más malinterpretada de la skill y la que, si haces mal, deja a la sesión principal sin material para ejecutar su tarea.**

La skill corre con `context: fork` + `agent: consulta-doc-agent`. Eso significa que tu contexto de subagente es AISLADO: todo lo que los WebFetch del paso 6 han descargado vive SOLO aquí dentro. Cuando tu ejecución termine y el fork se cierre, ese contenido se descartará y la sesión principal NUNCA lo verá.

El ÚNICO canal por el que hacer llegar material a la sesión principal es el `template.md`: solo lo que escribas en ese archivo quedará disponible cuando el modelo principal vuelva a tener el turno.

Por tanto, en modo INFO-TAREA tu trabajo en este paso NO es dejar una lista escueta de URLs y metadatos, sino **volcar al `template.md` todo el material útil que has extraído de las páginas en el paso 6**, con suficiente detalle para que la sesión principal pueda ejecutar la tarea pendiente sin volver a visitar ninguna URL. La sesión principal solo tendrá lo que tú escribas aquí; si lo dejas fuera, se pierde.

##### Qué escribir en `template.md`

Envuelve TODO el archivo entre los marcadores HTML `<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->` (primera línea) y `<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->` (última línea), con una línea en blanco tras el marcador de apertura y antes del de cierre. Los marcadores son comentarios HTML (invisibles al renderizar Markdown) y sirven como cinturón de seguridad para que la sesión principal reconozca la salida literal.

Dentro del bloque, en este orden:

1. **Línea introductoria** breve que indique que es material preparatorio. Por ejemplo: `Material preparatorio de la documentación oficial de Claude Code para la tarea pendiente de la sesión principal.`
2. **Aviso al lector** (una frase en cita Markdown con `> `) recordando que esto es TODO lo que la sesión principal tendrá del contenido oficial porque los WebFetch del subagente no sobreviven al fork.
3. **Sección `## Material extraído`**: un subbloque `### [Título de la página] — <URL>` por cada URL visitada en el paso 6, con el material útil para la tarea copiado en bullets. Qué incluir (no filtres por brevedad — si dudas, lo incluyes):
   - Campos exactos de frontmatter / settings.json / `.mcp.json` / archivos de configuración mencionados.
   - Flags de CLI, con su sintaxis exacta y alias.
   - Valores válidos de campos enum (p. ej. tipos de hook, modos de permisos, transportes MCP, variantes de `type`).
   - Bloques de JSON/YAML/Bash/PowerShell tomados literalmente de la doc, suficientemente completos para copiar-pegar.
   - Variables de entorno relevantes con sus nombres exactos.
   - Limitaciones, advertencias, notas sobre Windows vs macOS/Linux, notas sobre versiones mínimas, incompatibilidades.
   - Nombres/identificadores concretos (claves de settings, nombres de eventos, rutas por defecto, etc.).
   - **NO resumas en exceso**; el objetivo es que la sesión principal pueda ejecutar la tarea con este material como única fuente.
   - **NO redactes prosa estilo DUDA** (nada de "En este documento explicamos que..." ni introducciones ni cierres). Esto es material crudo para consumo del modelo principal, no una respuesta pulida para el usuario.
4. **Sección `## URLs visitadas`**: lista clicable en Markdown (`- [texto](URL)`) con todas las URLs abiertas con WebFetch en el paso 6.
5. **Sección `## Estado de reference.md`**: UNA frase con el mismo formato del modo DUDA:
   - Sin cambios: `reference.md sin cambios.`
   - Solo se añadió una URL nueva: `reference.md actualizado: añadido [URL].`
   - Solo se eliminó una URL rota: `reference.md actualizado: eliminado [URL] (link roto).`
   - Ambos: `reference.md actualizado: añadido [URL1]; eliminado [URL2] (link roto).`
6. **Aviso de búsqueda web** (solo si aplica el Caso B del paso 4), con el mismo formato del modo DUDA.

Estructura final esperada:

```
<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->

Material preparatorio de la documentación oficial de Claude Code para la tarea pendiente de la sesión principal.

> Nota: esto es todo lo que la sesión principal tendrá del contenido de la doc; los WebFetch del subagente ya no están disponibles al cerrarse el fork.

## Material extraído

### [Título de la página 1] — <URL>
- ... (extractos útiles literales de la doc: campos, flags, ejemplos, valores válidos, versiones, limitaciones) ...
- ...

### [Título de la página 2] — <URL>
- ...

## URLs visitadas

- [Texto](URL)
- ...

## Estado de reference.md

reference.md sin cambios.

<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->
```

El `template.md` en modo INFO-TAREA NO es una respuesta al usuario: es un dossier interno para el modelo principal. Piénsalo así: "estoy dejando aquí todo lo que la sesión principal necesitará saber de la doc para continuar con su tarea sin tener que investigar de nuevo".

### 9. Devuelve al modelo principal la frase meta que corresponde al modo elegido

**Lee esto con mucha atención. Este paso es el que más veces se ha roto históricamente y el responsable de que el usuario no vea la respuesta cuidada, o de que la sesión principal se quede sin material para su tarea.**

Tu tarea en este turno ya ha terminado. En los pasos anteriores has escrito en `template.md` el resultado íntegro de tu trabajo — **ese archivo ES el producto final de la skill**, y el modelo principal lo leerá cuando le pidas que lo haga. Tu trabajo YA NO es devolver contenido aquí; tu único trabajo restante es emitir LA frase meta que le diga al modelo principal qué hacer con ese archivo.

Hay DOS frases meta posibles — una por cada modo del paso 8 — y tienes que emitir EXACTAMENTE UNA de ellas, nunca las dos, nunca una mezcla de ambas, nunca la del modo equivocado. La elección depende únicamente de qué modo ejecutaste en el paso 8:

- Si en el paso 8 ejecutaste **8.A (modo DUDA)** → emite la **Variante 9.A**.
- Si en el paso 8 ejecutaste **8.B (modo INFO-TAREA)** → emite la **Variante 9.B**.

Resuelve primero `${CLAUDE_SKILL_DIR}/template.md` a su ruta absoluta del sistema (por ejemplo `C:\Users\amuel\.claude\skills\consulta-doc-claude-code\template.md` en Windows o `/Users/foo/.claude/skills/consulta-doc-claude-code/template.md` en macOS/Linux) y sustituye `<RUTA-ABSOLUTA-TEMPLATE>` por la ruta real en la variante que toque.

#### 9.A — Variante para modo DUDA

Emite LITERALMENTE esta cadena, sin añadir ni un solo carácter antes o después, sin envolverla entre comillas/backticks/bloques de código, sin traducirla, sin abreviarla:

    Lee el archivo <RUTA-ABSOLUTA-TEMPLATE> con la herramienta Read e imprime al usuario exactamente su contenido completo, línea a línea y carácter a carácter, incluyendo los marcadores `<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->` y `<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->` que delimitan la salida literal. No reformules, no resumas, no añadas introducciones ni cierres propios, no omitas ningún bloque. Ese archivo ES la salida de la skill para el usuario.

El efecto es: la sesión principal lee el template e imprime al usuario la respuesta redactada DUDA tal cual.

#### 9.B — Variante para modo INFO-TAREA

Emite LITERALMENTE esta cadena, con las mismas restricciones (sin caracteres extra, sin envolver, sin traducir, sin abreviar):

    Lee el archivo <RUTA-ABSOLUTA-TEMPLATE> con la herramienta Read. Dentro del bloque delimitado por los marcadores `<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->` y `<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->` encontrarás material preparatorio extraído de la documentación oficial de Claude Code que necesitas para continuar con la tarea que el usuario te había encomendado ANTES de invocar esta skill. NO imprimas ese archivo al usuario: úsalo como contexto de referencia interno para ejecutar esa tarea con información actualizada y correcta.

El efecto es: la sesión principal lee el template como dossier de contexto y sigue con la tarea original del usuario sin mostrar el archivo.

#### Violaciones prohibidas (NO hagas nada de esto)

Cada una de estas formas rompe el flujo y anula el trabajo que acabas de hacer:

- **Pegar el contenido que acabas de escribir en `template.md`** (título, cuerpo, bloques de código, listas de URLs, "Material extraído"...). Es el error más frecuente y el más dañino. Si te descubres empezando a escribir `#`, `##`, `-`, `URLs visitadas`, `Material extraído`, o un párrafo introductorio, **detente**: eso va en el template, NO aquí.
- **Emitir la variante del modo equivocado**: por ejemplo, emitir la Variante 9.A cuando el paso ejecutado fue 8.B (el modelo principal imprimiría el dossier interno al usuario como si fuera la respuesta, que no lo es), o emitir la Variante 9.B cuando el paso fue 8.A (el modelo principal se guardaría la respuesta del usuario como contexto interno y no se la imprimiría). Emitir la variante equivocada es tan malo como no emitir ninguna.
- **Emitir AMBAS variantes** o una frase híbrida con trozos de las dos. Solo UNA variante, exacta, literal.
- Añadir "Aquí tienes la respuesta:", "He consultado la documentación y...", "El material está aquí:" o cualquier otra introducción antes de la frase meta.
- Añadir un resumen, un TL;DR, una despedida, un comentario sobre lo que encontraste o cualquier otro texto después de la frase meta.
- Envolver la frase meta entre comillas (`"..."`), backticks simples (`` `...` ``) o bloques de código triple (```` ```...``` ````).
- Traducir la frase meta a otro idioma, abreviarla, parafrasearla o cambiarle puntuación/palabras.
- Olvidarte de sustituir `<RUTA-ABSOLUTA-TEMPLATE>` por la ruta absoluta real (Windows o POSIX) del sistema en el que se está ejecutando la skill.
- Responder en modo "conversacional" al invocador explicando lo que hiciste. El invocador no es el usuario; es un modelo que solo necesita la frase meta para ejecutar su siguiente paso.

#### Test mental antes de enviar

Antes de emitir tu mensaje final, haz este chequeo:

1. ¿Qué modo ejecuté en el paso 8, 8.A o 8.B? La variante de este paso 9 que voy a emitir, ¿es la que corresponde a ese modo? Si no coincide, reemito la correcta.
2. ¿Mi mensaje empieza exactamente por `Lee el archivo `? Si no, es un bug.
3. ¿Mi mensaje termina con la frase exacta de la variante elegida (variante 9.A termina por `Ese archivo ES la salida de la skill para el usuario.`; variante 9.B termina por `úsalo como contexto de referencia interno para ejecutar esa tarea con información actualizada y correcta.`) y no hay NADA más detrás? Si no, es un bug.
4. ¿He sustituido `<RUTA-ABSOLUTA-TEMPLATE>` por la ruta absoluta real? Si queda el placeholder literal, es un bug.
5. ¿Estoy tentado a añadir cualquier otra cosa «por amabilidad» o «para dar contexto»? Si la respuesta es sí: NO lo hagas. Tu tarea ya está hecha y el contenido está en `template.md`. Solo queda la frase meta de una única variante. Nada más.
