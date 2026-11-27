# AGENTS.md — keytyper

> Contrato de contexto para agentes (LLM) e para o operador. Atualize "Estado atual" ao encerrar
> uma sessão relevante. Data plane do portfólio: `~/Tarscase/workspacePessoal/leosavio-org`.

## O que é

Lib Python MIT, repo `leosavio/keytyper`: saída de terminal com efeito de digitação, cores e
formatação, sem dependências (só a biblioteca padrão). Publicada no PyPI como `keytyper`.

## Stack

| Componente | Tecnologia | Nota |
|---|---|---|
| Código | `keytyper/keytyper.py`, `keytyper/__init__.py` (`__version__`) | Python 3.11–3.15, tipado (`py.typed`) |
| Empacotamento | `pyproject.toml` (setuptools ≥ 77, licença SPDX `MIT`) | sem `setup.py` |
| Testes | `tests/` (pytest), `.github/workflows/test.yml` | Linux 3.11–3.15, macOS e Windows 3.15; flake8, black 26.10.1, mypy |
| Release | `.github/workflows/publish.yml` (tag `v*`) | versão da tag confere com o `pyproject.toml`; build com `uv build`, `twine check`, instalação em 3 SOs × 2 Pythons, Trusted Publishing (`testpypi` para `-rc.N`, `pypi` para a final), release no GitHub com os mesmos arquivos |
| Segurança | `.github/workflows/security.yml` (zizmor), `.github/dependabot.yml`, settings do repo | CodeQL, Dependabot, secret scanning e push protection pelas settings |

## Estado atual

> Última atualização: 2026-11-27

Primeira publicação no PyPI (0.1.0) preparada: empacotamento só no `pyproject.toml`, Python
3.11+, workflows com actions fixadas por SHA e Trusted Publishing pela conta `leosavio` (pending
publishers no PyPI e no TestPyPI). Acompanhamento: leosavio/leosavio-org#91.

## Comandos

```sh
uv run --no-project --python 3.12 --with pytest --with pytest-mock --with . pytest -q tests
uvx black --check keytyper tests examples
uvx mypy keytyper
uv build && uvx twine check --strict dist/*
git tag -a v0.1.1-rc.1 -m "keytyper v0.1.1-rc.1" && git push origin v0.1.1-rc.1   # TestPyPI
```

## Guardrails

- Versão: o `pyproject.toml` e o `__version__` guardam a versão base (`X.Y.Z`); a tag de
  pré-release só acrescenta o sufixo no build. Versão publicada no PyPI não pode ser substituída:
  teste antes com uma tag `-rc.N` (TestPyPI).
- Nenhum token do PyPI em secret: a publicação é só por Trusted Publishing.
