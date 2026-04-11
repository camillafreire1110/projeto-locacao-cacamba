# Sistema de Locação de Caçambas

## 📖 Descrição
Sistema desenvolvido em Flask + MySQL para controle de locação de caçambas, incluindo gerenciamento de estoque e cadastro de clientes.

O projeto foi inspirado em uma necessidade real da área de locação de caçambas, permitindo simular o controle operacional de estoque e atendimento.

## 🚀 Funcionalidades

### 🔹 AC1 – Controle de Caçambas
- Controle de 50 caçambas numeradas
- Status: disponível / alugada
- Alteração de status das caçambas (disponível/alugada)
- Painel resumo com contagem automática
- Integração entre Frontend, Backend e Banco de Dados

### 🔹 AC2 – Cadastro de Clientes
- Cadastro de clientes (nome, CPF/CNPJ, endereço da obra, telefone e email)
- Listagem de clientes em tabela no frontend
- Integração com API REST (Flask)
- Atualização da lista de clientes após cadastro, mediante solicitação do usuário
- Exibição de mensagem de confirmação de cadastro
- Exibição dos dados apenas quando solicitado pelo usuário
- Direcionamento automático para o cadastro de cliente ao selecionar uma caçamba disponível

## 🛠 Tecnologias Utilizadas
- Python
- Flask
- MySQL
- HTML
- JavaScript
- Git
- GitHub

## 📁 Estrutura do Projeto

backend/
 └── src/
     ├── controllers/
     ├── models/
     ├── routes/
     ├── app.py
     ├── db.py
     └── test_db.py

frontend/
 └── index.html

## 🎯 Objetivo do Projeto
Aplicar conceitos de desenvolvimento de software com separação em camadas (frontend, backend e banco de dados), utilizando metodologia incremental por funcionalidades (AC1, AC2).

## 🚀 Próximos Passos
- Integração entre clientes e caçambas (locação)
- Controle de prazo de permanência (3 dias úteis)
- Organização de itinerário por data