# Laboratorio SCN — Deploy e CI/CD com Docker

## Requisitos
Python 3.12+, Docker Engine com Compose plugin, Git e uma conta GitHub.

## Execucao local
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest -q
docker compose up -d --build --wait
curl -i http://localhost:8000/health
docker compose ps
docker compose down
```

## CI
1. Crie um repositorio GitHub e copie os arquivos, inclusive `.github/workflows/ci.yaml`.
2. Publique na branch `main`.
3. Abra a aba **Actions**; observe testes, build e smoke test.

**Importante:** o 'deploy' do workflow ocorre apenas no runner temporario do GitHub Actions, nao em um servidor persistente. O ambiente sera destruido apos a execucao. Para CD real, adicione um job separado, credenciais restritas e aprovacao para ambiente de producao.

## Desafio
Altere `/health` para responder 503 e explique qual etapa falha no pipeline. Depois reverta a alteracao.

## Segurança (proximos passos)
Fixar actions por SHA, scanning de dependencias/imagem, SBOM, minimo privilegio, segredos em GitHub Environments e promocao de imagens imutaveis por digest.
