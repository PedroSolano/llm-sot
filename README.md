# Codex Registry — GitHub Source of Truth

Este diretório é o conteúdo inicial do repositório GitHub central.

Fonte da verdade:

```text
GitHub repository
├── AGENTS.md
├── agents/
├── skills/
└── routing/router_policy.json
```

O GitHub é independente do Control Plane, GT 730, RX 6800 XT, Ollama e Qwen.
Todas as máquinas Codex devem apontar para o mesmo repositório.

Não coloque segredos, PATs, chaves privadas ou senhas neste Git.

## Publicação inicial

```bash
./git-tools/publish-git-source.sh \
  --remote git@github.com:SEU_USUARIO/codex-registry.git \
  --source ./git-source
```

Ou publique manualmente.

## Alterações

Faça alterações em um clone normal e use commit/push. As demais máquinas fazem
sync automaticamente ou via `codex-bootstrap`/`codex-registry-sync`.

## Offline

Se o GitHub estiver temporariamente indisponível, a última revisão local válida
continua em uso.
