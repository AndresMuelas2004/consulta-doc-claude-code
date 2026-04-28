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
