# Desafio Stalse – API de Gerenciamento de Tickets e Pedidos

Este projeto consiste em uma API desenvolvida em **FastAPI** para gerenciamento de pedidos e tickets, incluindo carga de dados, ETL e exposição de endpoints documentados via Swagger.

---

## 📥 Clone do repositório

```bash
git clone https://github.com/Dyego-Barros/desafio-stalse.git
cd desafio-stalse
```

---

## 🐍 Criação do ambiente virtual (Python)

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\\Scripts\\activate  # Windows
```

---

## 📦 Instalação das dependências

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## 📊 Preparação dos dados

### 1️⃣ Navegar até o diretório `data/raw` e executar o dataset

```bash
cd data/raw
python dataset.py
```

Esse passo é responsável por preparar ou baixar o dataset bruto.

---

### 2️⃣ Navegar até o diretório `data` e executar o ETL

```bash
cd ../
python etl.py
```

O script de ETL realiza o processamento e gera os dados prontos para consumo pela API.

---

## 🚀 Executando a API

Navegue até o diretório `api` e execute a aplicação:

```bash
cd api
python main.py
```

A API será inicializada e o banco de dados será criado automaticamente.

---

## 📚 Documentação da API (Swagger)

Após iniciar a aplicação, acesse no navegador:

```
http://localhost:<PORTA>/docs
```

> Substitua `<PORTA>` pela porta configurada (ex: `8000`).

No Swagger você poderá:

* Visualizar todos os endpoints
* Testar as rotas da API
* Ver os schemas de request e response

---

## ✅ Observações

* Certifique-se de que o ambiente virtual esteja ativado antes de executar os scripts.
* Para evitar problemas com SQLite, utilize apenas **1 worker** ao rodar a aplicação.
* O projeto segue uma estrutura baseada em **DDD (Domain Driven Design)**.

---

📌 Em caso de dúvidas ou problemas, consulte os logs exibidos no terminal durante a execução.
