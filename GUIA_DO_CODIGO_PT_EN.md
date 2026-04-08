# EventMaster Pro - Guia do Codigo (PT-BR / EN)

Este arquivo explica, de forma simples, o que o sistema faz por dentro.
A ideia e ajudar qualquer pessoa, mesmo sem experiencia tecnica.

---

## PT-BR

### 1) O que este projeto faz

O EventMaster Pro e um sistema de orcamento para eventos.
Ele ajuda a:

- cadastrar servicos do evento (buffet, salao, decoracao etc.)
- calcular total automaticamente
- simular parcelamento com juros
- comparar com o caixa disponivel do cliente
- gerar um PDF profissional para enviar

Resumindo: ele organiza os custos do evento em uma tela bonita e pratica.

### 2) Como o sistema e dividido

Mesmo sendo um arquivo principal grande, o projeto tem duas partes:

- Front-end: o que aparece para o usuario (tela, botoes, imagens, formularios)
- Back-end: a parte Python/Streamlit que carrega o app no navegador

### 3) Front-end (explicado para leigos)

O front-end e como a "cara" do sistema.

Ele usa:

- HTML: estrutura da pagina (onde cada bloco fica)
- CSS: visual (cores, fontes, espacamento, estilo profissional)
- JavaScript: comportamento (cliques, calculos, salvar dados, gerar PDF)

No dia a dia do usuario, o front-end:

- mostra os cards de servicos
- permite adicionar, editar e remover itens
- atualiza o total em tempo real
- mostra se o caixa esta suficiente ou estourado
- guarda sessao no navegador para nao pedir login toda hora
- gera o PDF de proposta com tema visual do sistema

### 4) Back-end (explicado para leigos)

O back-end aqui e leve e direto.

Ele usa:

- Python + Streamlit para abrir a aplicacao web
- um "container" de HTML para renderizar toda a interface

Na pratica, o back-end:

- inicia a pagina
- aplica configuracoes gerais do app
- entrega a interface para o navegador do usuario

Importante: a maior parte da inteligencia de tela (interacao, calculos, PDF) acontece no JavaScript, no lado do navegador.

### 5) Onde os dados ficam

Os dados da sessao ficam no navegador do proprio usuario (localStorage).

Isso significa que:

- ao atualizar a pagina, a sessao pode voltar automaticamente
- ao clicar em "Sair", a sessao ativa e limpa
- nao existe banco remoto neste fluxo atual

### 6) Geracao de PDF

Quando o usuario clica para gerar a proposta:

- o sistema pega os itens do orcamento
- monta uma tabela com valores e condicoes
- aplica identidade visual (tema vinho/dourado)
- adiciona resumo financeiro
- baixa o arquivo PDF pronto

### 7) Em uma frase

O EventMaster Pro e uma aplicacao web de orcamentos de eventos com visual profissional, calculo automatico e exportacao de proposta em PDF.

---

## EN

### 1) What this project does

EventMaster Pro is an event budgeting system.
It helps users:

- add event services (buffet, venue, decoration, etc.)
- calculate totals automatically
- simulate installment payments with interest
- compare planned costs against the client budget
- export a professional PDF proposal

In short: it organizes event costs in a clean and practical interface.

### 2) How the system is organized

Even though the main app is concentrated in one large file, the project has two clear layers:

- Front-end: what users see and interact with (UI)
- Back-end: Python/Streamlit layer that serves the app

### 3) Front-end (beginner-friendly)

The front-end is the "face" of the system.

It uses:

- HTML: page structure
- CSS: styling (colors, typography, spacing, premium look)
- JavaScript: behavior (clicks, calculations, session, PDF generation)

From the user perspective, the front-end:

- displays service cards
- allows adding, editing, and removing budget items
- updates totals in real time
- shows whether the client budget is enough
- keeps session data in the browser
- generates a branded proposal PDF

### 4) Back-end (beginner-friendly)

The back-end in this project is lightweight.

It uses:

- Python + Streamlit to launch the web app
- an embedded HTML component to render the full interface

In practice, the back-end:

- starts the application
- applies global app settings
- delivers the UI to the browser

Important: most screen logic (interactions, calculations, PDF layout) runs on JavaScript in the browser.

### 5) Where data is stored

Session data is stored in the user's own browser (localStorage).

That means:

- refreshing the page can restore the active session
- clicking "Logout" clears the active session
- there is no remote database in the current flow

### 6) PDF generation

When the user clicks to export:

- the app reads current budget items
- builds a detailed table with prices and payment terms
- applies the same visual theme (burgundy/gold)
- adds a financial summary section
- downloads a ready-to-send PDF file

### 7) One-line summary

EventMaster Pro is a professional event budgeting web app with automatic calculations and branded PDF proposal export.
