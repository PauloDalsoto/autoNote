# AutoNote

Ferramenta de automação para implementação de SAP Notes

## Descrição

AutoNote é uma ferramenta de linha de comando desenvolvida para automatizar o processo de implementação de SAP Notes em sistemas SAP. A ferramenta simplifica o processo manual de análise e implementação de notas, fornecendo um relatório detalhado das etapas necessárias.

## Funcionalidades

- Processamento de listas de SAP Notes via arquivo Excel
- Verificação automática da versão do sistema SAP
- Download automático de SAP Notes
- Análise de dependências entre notas
- Extração de passos manuais
- Verificação de compatibilidade
- Geração de relatórios detalhados

## Instalação

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Instalar dependências usando Poetry
poetry install
```

## Uso

```bash
autonote process --input notas.xlsx --output relatorio.xlsx
```

## Estrutura do Projeto

```
autonote/
├── autonote/
│   ├── __init__.py
│   ├── cli.py              # Interface de linha de comando
│   ├── core/               # Lógica principal
│   │   ├── __init__.py
│   │   ├── note.py        # Modelo de SAP Note
│   │   ├── processor.py    # Processamento de notas
│   │   └── reporter.py     # Geração de relatórios
│   ├── sap/                # Integração com SAP
│   │   ├── __init__.py
│   │   ├── connection.py   # Conexão com SAP GUI
│   │   └── downloader.py   # Download de notas
│   └── utils/              # Utilitários
│       ├── __init__.py
│       ├── excel.py        # Manipulação de arquivos Excel
│       └── logger.py       # Configuração de logs
├── tests/                  # Testes unitários
├── pyproject.toml         # Configuração do projeto
└── README.md
```

## Requisitos

- Python 3.8+
- SAP GUI instalado
- Acesso ao SAP Service Marketplace