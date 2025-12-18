# 🚀 Desafio Stalse – API de Gerenciamento de Tickets e Pedidos

Este projeto consiste em uma **API desenvolvida em FastAPI** para gerenciamento de **pedidos e tickets**, incluindo:

* 📥 Carga de dados
* 🔄 Pipeline de ETL
* 🌐 Exposição de endpoints REST
* 📚 Documentação automática via Swagger

---

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

* **Python 3.9+**
* **UV** – gerenciador de pacotes e ambientes virtuais

### 📦 Instalação do UV

#### 🪟 Windows (PowerShell)

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 🐧 Linux / 🍎 macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 🔁 Alternativa via pip

```bash
pip install uv
```

---

## 📥 Clone do repositório

```bash
git clone https://github.com/Dyego-Barros/desafio-stalse.git
cd desafio-stalse
```

---

## 🐍 Criação do ambiente virtual com UV

Crie e ative um ambiente virtual:

```bash
# Criar ambiente virtual
uv venv .venv
```

### ▶️ Ativação do ambiente virtual

* **Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

* **Windows (CMD):**

```bash
.venv\Scripts\activate.bat
```

* **Linux/macOS:**

```bash
source .venv/bin/activate
```

---

## 📦 Instalação das dependências

Instale todas as dependências do projeto:

```bash
uv sync
```

---

## 📊 Preparação dos dados

### 1️⃣ Executar o dataset bruto

Navegue até o diretório `data/raw` e execute:

```bash
cd data/raw
python dataset.py
```

Esse passo é responsável por **baixar ou gerar o dataset bruto**.

---

### 2️⃣ Executar o ETL

Retorne para o diretório `data` e execute:

```bash
cd ../
python etl.py
```

O script de **ETL** processa os dados e os prepara para consumo pela API.

---

## 🚀 Executando a API

Navegue até o diretório da API e execute:

```bash
cd api
python main.py
```

* A API será inicializada
* O banco de dados será criado automaticamente

---

## 📚 Documentação da API (Swagger)

Após iniciar a aplicação, acesse:

```
http://localhost:8000/docs
```

No Swagger você poderá:

* 📋 Visualizar todos os endpoints
* 🔧 Testar as rotas diretamente pela interface
* 📄 Consultar schemas de request e response
* ▶️ Executar requisições de exemplo

---

## 🗂️ Estrutura do Projeto

```text
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
└── README.md              # Documentação do projeto
```

---

## ✅ Observações Importantes

* ✅ Ative o ambiente virtual antes de executar os scripts
* ✅ Para evitar problemas com **SQLite**, utilize apenas **1 worker**
* ✅ O projeto segue conceitos de **DDD (Domain Driven Design)**
* ✅ O **UV** oferece instalação mais rápida e confiável que o pip tradicional
* ✅ Todos os caminhos são relativos à **raiz do projeto**

---

## 🔧 Comandos Úteis do UV

```bash
# Atualizar dependências
uv sync --upgrade

# Listar dependências instaladas
uv pip list

# Adicionar nova dependência
uv add nome-da-dependencia

# Remover dependência
uv remove nome-da-dependencia
```

---

## 🐛 Solução de Problemas

Caso encontre erros:

* **Erro de importação:** verifique se o ambiente virtual está ativado
* **Porta em uso:** altere a porta no arquivo `api/main.py`
* **Erro no banco de dados:** delete o arquivo `database.db` e execute novamente
* **Erro de permissão:** execute como administrador ou ajuste as permissões

---

## 📞 Suporte

Para dúvidas ou problemas:

* Consulte os logs exibidos no terminal
* Verifique se todas as etapas foram seguidas corretamente
* Para problemas com o **UV**, consulte a documentação oficial

---

✨ *Projeto desenvolvido para o Desafio Técnico Stalse*
