Desafio Stalse – API de Gerenciamento de Tickets e Pedidos

Este projeto consiste em uma API desenvolvida em FastAPI para gerenciamento de pedidos e tickets, incluindo carga de dados, ETL e exposição de endpoints documentados via Swagger.

⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

Python 3.9+
Gerenciador de pacotes UV - Instalação rápida:
🪟 Windows

bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
🐧 Linux / 🍎 macOS

bash
curl -LsSf https://astral.sh/uv/install.sh | sh
Ou via pip (alternativa):

bash
pip install uv
📥 Clone do repositório

bash
git clone https://github.com/Dyego-Barros/desafio-stalse.git
cd desafio-stalse
🐍 Criação do ambiente virtual com UV

Crie e ative um ambiente virtual usando UV:

bash
# Criar ambiente virtual
uv venv .venv

# Ativar ambiente virtual
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Linux/macOS:
source .venv/bin/activate
📦 Instalação das dependências

Instale as dependências do projeto usando UV:

bash
uv sync
📊 Preparação dos dados

1️⃣ Navegar até o diretório data/raw e executar o dataset

bash
cd data/raw
python dataset.py
Esse passo é responsável por preparar ou baixar o dataset bruto.

2️⃣ Navegar até o diretório data e executar o ETL

bash
cd ../
python etl.py
O script de ETL realiza o processamento e gera os dados prontos para consumo pela API.

🚀 Executando a API

Navegue até o diretório api e execute a aplicação:

bash
cd api
python main.py
A API será inicializada e o banco de dados será criado automaticamente.

📚 Documentação da API (Swagger)

Após iniciar a aplicação, acesse no navegador:

text
http://localhost:8000/docs
No Swagger você poderá:

📋 Visualizar todos os endpoints
🔧 Testar as rotas da API diretamente na interface
📄 Ver os schemas de request e response
▶️ Executar requisições de exemplo
🗂️ Estrutura do Projeto

text
desafio-stalse/
├── api/                    # Código da API FastAPI
│   ├── main.py            # Ponto de entrada da aplicação
│   └── ...                # Outros módulos da API
├── data/                   # Processamento de dados
│   ├── raw/               # Dados brutos
│   │   └── dataset.py     # Geração do dataset
│   └── etl.py             # Pipeline de ETL
├── .venv/                 # Ambiente virtual (gerado)
├── requirements.txt       # Dependências do projeto
└── README.md             # Este arquivo
✅ Observações Importantes

✅ Certifique-se de que o ambiente virtual esteja ativado antes de executar os scripts
✅ Para evitar problemas com SQLite, utilize apenas 1 worker ao rodar a aplicação
✅ O projeto segue uma estrutura baseada em DDD (Domain Driven Design)
✅ UV oferece instalação mais rápida e confiável que pip tradicional
✅ Todos os caminhos são relativos à raiz do projeto
🔧 Comandos Úteis UV

bash
# Atualizar dependências
uv sync --upgrade

# Listar dependências instaladas
uv pip list

# Adicionar nova dependência
uv add nome-da-dependencia

# Remover dependência
uv remove nome-da-dependencia
🐛 Solução de Problemas

Se encontrar erros:

Erro de importação: Verifique se o ambiente virtual está ativado
Erro de porta em uso: Altere a porta no arquivo api/main.py
Erro no banco de dados: Delete o arquivo database.db e execute novamente
Erro de permissão: Execute como administrador ou ajuste permissões
📞 Suporte

Para problemas ou dúvidas:

Consulte os logs exibidos no terminal durante a execução
Verifique se todas as etapas foram seguidas corretamente
Para problemas com UV, consulte a documentação oficial