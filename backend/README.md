# Backend – Sistema de Locação de Caçambas

Este diretório contém o backend do sistema de locação de caçambas, responsável pelo processamento das informações, regras de negócio e integração com o banco de dados.

---

## 📌 Descrição

O backend foi desenvolvido com o objetivo de dar suporte às operações do sistema, permitindo o controle de caçambas, cadastro de clientes e registro de locações.

A aplicação realiza a comunicação com o frontend por meio de uma API, garantindo a troca de dados em formato JSON.

---

## ⚙️ Tecnologias Utilizadas

- Python
- Flask
- MySQL
- JSON (comunicação entre frontend e backend)

---

## 🔧 Responsabilidades do Backend

- Receber requisições do frontend
- Processar e validar os dados
- Gerenciar o status das caçambas
- Realizar cadastro de clientes
- Registrar locações
- Armazenar e consultar dados no banco MySQL
- Retornar respostas em formato JSON

---

## 🚀 Funcionalidades Implementadas

### 🟢 AC1 – Controle de Caçambas
- Listagem de caçambas disponíveis e alugadas
- Alteração de status (disponível / alugada)

### 🟢 AC2 – Cadastro de Clientes
- Cadastro de clientes com:
  - Nome ou Razão Social
  - CPF ou CNPJ
  - Endereço
  - Telefone
  - E-mail
- Listagem de clientes cadastrados

### 🟢 AC3 – Registro de Locações
- Vinculação entre cliente e caçamba
- Registro automático de:
  - Data de entrega
  - Data de retirada (3 dias após)
- Armazenamento das locações no banco de dados
- Consulta das locações cadastradas

---

## 🗄️ Banco de Dados

O sistema utiliza MySQL para armazenamento das informações, com tabelas principais:

- `cacambas`
- `clientes`
- `locacoes`

---

## 🔗 Comunicação com o Frontend

O backend disponibiliza endpoints para:

- Consulta de caçambas
- Cadastro de clientes
- Registro de locações
- Consulta de locações

---

## 📌 Status do Projeto

Sistema funcional com integração completa entre:

- Frontend
- Backend
- Banco de dados (MySQL)

As funcionalidades principais de controle, cadastro e locação estão implementadas e operacionais.

---

## 📈 Próximas Melhorias (AC4)

- Implementação de controle de pagamentos
- Envio de informações operacionais ao cliente
- Regras de negócio mais detalhadas

---

## 👩‍💻 Autora

Projeto desenvolvido como atividade acadêmica, baseado em um cenário real de locação de caçambas.

