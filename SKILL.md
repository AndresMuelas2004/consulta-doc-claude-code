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

NO redactes respuesta teórica, ni resumen del contenido. Escribe en `${CLAUDE_SKILL_DIR}/template.md` SOLO lo siguiente, envuelto entre los marcadores HTML `<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->` y `<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->` (primera y última línea del archivo respectivamente, con una línea en blanco a continuación y antes), en este orden:

1. Una línea introductoria breve, por ejemplo: `Información preparatoria de Claude Code consultada para la tarea en curso:`.

2. **URLs visitadas**: lista clicable en Markdown (`- [texto](URL)`) con las URLs que se abrieron con WebFetch en el paso 6.

3. **Estado de reference.md**: UNA frase con el mismo formato del modo DUDA:
   - Sin cambios: `reference.md sin cambios.`
   - Solo se añadió una URL nueva: `reference.md actualizado: añadido [URL].`
   - Solo se eliminó una URL rota: `reference.md actualizado: eliminado [URL] (link roto).`
   - Ambos: `reference.md actualizado: añadido [URL1]; eliminado [URL2] (link roto).`

4. **Aviso de búsqueda web** si aplica el Caso B del paso 4, con el mismo formato del modo DUDA.

Los marcadores son comentarios HTML, por lo que no se renderizan en Markdown y el usuario no los ve; su única función es servir de cinturón de seguridad para que el modelo principal reconozca la salida como literal si por error llega a su contexto fuera del archivo.

El contenido real de la documentación ya quedó en el contexto del modelo principal gracias a los WebFetch del paso 6, por lo que este puede proceder con la tarea que tuviera pendiente. El `template.md` en este modo solo cumple la función de dejar trazabilidad de qué se consultó y de cómo quedó el catálogo.

### 9. Devuelve al modelo principal la instrucción de imprimir `template.md`

**Lee esto con mucha atención. Este paso es el que más veces se ha roto históricamente y el responsable de que el usuario no vea la respuesta cuidada que acabas de escribir.**

Tu tarea en este turno ya ha terminado. En los pasos anteriores has escrito en `template.md` el resultado íntegro de la investigación — **ese archivo ES la salida final de la skill para el usuario**, y el modelo principal lo imprimirá tal cual cuando le pidas leerlo. Tu trabajo YA NO es devolver esa respuesta aquí; tu trabajo aquí es SOLO emitir la frase meta que le dice al modelo principal qué archivo leer e imprimir literal. No tienes que devolver el contenido otra vez por este canal: el modelo principal no necesita verlo inline, necesita verlo cuando lea `template.md`.

Dicho de otra forma: **tu tarea era escribir en `template.md` el resultado de la investigación y nada más; no tienes que devolver ese resultado aquí por el mensaje final. Tienes que devolver simplemente el texto literal indicado abajo a la sesión principal, para que esa sesión lea `template.md` y lo imprima literal por pantalla al usuario.** Si copias el contenido, el modelo principal perderá la pista de que debe imprimir literal y terminará parafraseando o resumiendo — y el usuario no verá tu respuesta.

#### Qué debes emitir

Resuelve `${CLAUDE_SKILL_DIR}/template.md` a su ruta absoluta del sistema (por ejemplo `C:\Users\amuel\.claude\skills\consulta-doc-claude-code\template.md` en Windows o `/Users/foo/.claude/skills/consulta-doc-claude-code/template.md` en macOS/Linux). Tu ÚNICA salida en este turno debe ser LITERALMENTE esta cadena, sustituyendo `<RUTA-ABSOLUTA-TEMPLATE>` por la ruta real ya resuelta, sin añadir ni un solo carácter antes o después, sin envolverla entre comillas, backticks ni bloques de código, sin traducirla y sin abreviarla:

    Lee el archivo <RUTA-ABSOLUTA-TEMPLATE> con la herramienta Read e imprime al usuario exactamente su contenido completo, línea a línea y carácter a carácter, incluyendo los marcadores `<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->` y `<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->` que delimitan la salida literal. No reformules, no resumas, no añadas introducciones ni cierres propios, no omitas ningún bloque. Ese archivo ES la salida de la skill para el usuario.

#### Violaciones prohibidas (NO hagas nada de esto)

Estas son las formas concretas en las que se ha roto este paso en el pasado. Cada una invalida la skill entera porque impide que el usuario vea literalmente `template.md`:

- **Pegar el contenido técnico que ya escribiste en `template.md`** (título, cuerpo con bloques de código, "URLs visitadas", "Estado de reference.md"). Es el error más frecuente y el más dañino. Si te descubres a ti mismo empezando a escribir `## ...` o `# ...` o un párrafo introductorio de la respuesta, **detente**: ese contenido ya está en `template.md`, NO lo dupliques aquí.
- Añadir "Aquí tienes la respuesta:", "He consultado la documentación y...", "La respuesta es la siguiente:" o cualquier otra introducción antes de la frase meta.
- Añadir un resumen, un TL;DR, una despedida, un comentario sobre lo que encontraste o cualquier otro texto después de la frase meta.
- Envolver la frase meta entre comillas (`"..."`), backticks simples (`` `...` ``) o bloques de código triple (```` ```...``` ````).
- Traducir la frase meta a otro idioma, abreviarla, parafrasearla o cambiarle puntuación/palabras.
- Olvidarte de sustituir `<RUTA-ABSOLUTA-TEMPLATE>` por la ruta absoluta real (Windows o POSIX) del sistema en el que se está ejecutando la skill.
- Responder en modo "conversacional" al invocador explicando lo que hiciste. El invocador no es el usuario; es un modelo que solo necesita la frase meta para ejecutar un Read.

#### Test mental antes de enviar

Antes de emitir tu mensaje final, haz este chequeo:

1. ¿Mi mensaje empieza exactamente por `Lee el archivo `? Si no, es un bug.
2. ¿Mi mensaje termina exactamente con `Ese archivo ES la salida de la skill para el usuario.` y no hay nada más detrás? Si no, es un bug.
3. ¿He sustituido `<RUTA-ABSOLUTA-TEMPLATE>` por la ruta absoluta real? Si queda el placeholder literal, es un bug.
4. ¿Estoy tentado a añadir cualquier otra cosa «por amabilidad» o «para dar contexto»? Si la respuesta es sí: NO lo hagas. Tu tarea ya está hecha y el contenido está en `template.md`. Solo queda la frase meta. Nada más.
