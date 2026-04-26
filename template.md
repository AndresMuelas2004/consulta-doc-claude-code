<!-- SKILL-CONSULTA-DOC:OUTPUT-START -->

## Sintaxis `@path/to/file` en CLAUDE.md: reglas exactas de detección

### La respuesta corta: `@` puede ir en cualquier parte de la línea

La [documentación oficial de memoria](https://code.claude.com/docs/en/memory#import-additional-files) establece literalmente:

> CLAUDE.md files can import additional files using `@path/to/import` syntax. [...] reference them with `@` syntax **anywhere in your CLAUDE.md**

La palabra clave es **anywhere** ("en cualquier lugar"). El parser no requiere que el `@` esté al principio de línea.

---

### Ejemplos que aparecen textualmente en la doc

```text
See @README for project overview and @package.json for available npm commands for this project.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

Estos dos ejemplos demuestran concretamente dos casos:

1. **`@` embebido dentro de una oración en prosa** (`See @README for...`) — funciona.
2. **`@` dentro de una lista con guion** (`- git workflow @docs/git-instructions.md`) — funciona.

Un tercer ejemplo en la misma doc muestra `@` dentro de una lista con sangría en un archivo `CLAUDE.md`:

```markdown
# Individual Preferences
- @~/.claude/my-project-instructions.md
```

Y el ejemplo con `AGENTS.md`:

```markdown
@AGENTS.md

## Claude Code

Use plan mode for changes under `src/billing/`.
```

Aquí el `@` sí está al principio de línea, pero eso no es un requisito — simplemente es así en este ejemplo concreto.

---

### Reglas de resolución de rutas

- Se permiten **rutas relativas y absolutas**.
- Las rutas relativas se resuelven **relativas al archivo que contiene el import**, no al directorio de trabajo.
- Los archivos importados pueden importar otros archivos a su vez (**recursividad**), con un **máximo de 5 saltos** de profundidad.
- Se puede usar `~` para referenciar el home del usuario (p. ej. `@~/.claude/my-project-instructions.md`).

---

### Cuándo se carga el archivo importado

Los archivos referenciados con `@` se **expanden y cargan en el contexto al inicio de la sesión** (al lanzar Claude Code), junto con el CLAUDE.md que los referencia. No son carga bajo demanda: se incluyen en el contexto desde el primer momento, igual que si su contenido estuviera inline en el CLAUDE.md.

Implicación importante documentada: dividir el contenido en múltiples archivos con `@path` **no reduce el consumo de tokens** — toda la cadena importada se carga en contexto al inicio. Cito la doc:

> Splitting into `@path` imports helps organization but does not reduce context, since imported files load at launch.

---

### Aviso de importaciones externas al proyecto

La doc incluye esta advertencia:

> The first time Claude Code encounters external imports in a project, it shows an approval dialog listing the files. If you decline, the imports stay disabled and the dialog does not appear again.

Es decir: la primera vez que un CLAUDE.md importa archivos externos al proyecto (p. ej. desde `~/.claude/`), Claude Code pide aprobación explícita al usuario. Si se rechaza, los imports quedan desactivados permanentemente para ese proyecto y el diálogo no vuelve a aparecer.

---

### Qué hace que un `@` NO se reconozca como import

La documentación no especifica explícitamente patrones que fallen. De los ejemplos y la frase "anywhere" se infiere que no hay restricción de posición en la línea (inicio, mitad de oración, dentro de lista con o sin sangría). Lo que sí puede hacer que los imports queden **desactivados** es rechazar el diálogo de aprobación la primera vez que se encuentran imports externos.

---

## URLs visitadas

- [How Claude remembers your project — Import additional files](https://code.claude.com/docs/en/memory#import-additional-files)

## Estado de reference.md

reference.md sin cambios.

<!-- SKILL-CONSULTA-DOC:OUTPUT-END -->
