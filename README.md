# Sistema de Locação de Caçambas

Projeto desenvolvido com o objetivo de gerenciar o processo de locação de caçambas, incluindo controle de estoque, cadastro de clientes, registro de locações e controle operacional completo da locação.

---

## 📌 Descrição

O sistema simula um cenário real de uma empresa de locação de caçambas, permitindo o gerenciamento completo do fluxo operacional, desde a disponibilidade da caçamba até a finalização da locação.

---

## ⚙️ Tecnologias Utilizadas

- Python (Flask)
- MySQL
- HTML, CSS e JavaScript
- API REST (comunicação frontend e backend)

---

## 🚀 Funcionalidades

### 🟢 AC1 – Controle de Caçambas

- Listagem de caçambas
- Controle de status das caçambas
- Alteração entre disponível e alugada
- Visualização das caçambas cadastradas no sistema

---

### 🟢 AC2 – Cadastro de Clientes

- Cadastro completo de clientes
- Registro de nome, CPF/CNPJ, endereço, telefone e e-mail
- Listagem dos clientes cadastrados
- Armazenamento das informações no banco de dados

---

### 🟢 AC3 – Registro de Locações

- Associação entre cliente e caçamba
- Registro da data prevista de entrega
- Registro da data prevista de retirada
- Criação da locação no banco de dados
- Exibição das locações cadastradas no sistema

---

### 🟢 AC4 – Controle Operacional da Locação

- Controle de status da locação
- Controle de status de pagamento
- Confirmação de entrega da caçamba
- Finalização da locação
- Registro da data real de entrega
- Registro da data real de retirada
- Exibição visual dos status da locação
- Bloqueio dos botões após a finalização da locação
- Exibição das regras operacionais da locação na interface
- Notificação visual após confirmação de entrega ou finalização

---

## 📋 Regras de Negócio

- Permanência de 3 dias úteis
- Não ultrapassar a borda da caçamba
- Não movimentar a caçamba sem autorização
- Não retirar a faixa refletiva
- Entregas e retiradas realizadas no período noturno

---

## 🗄️ Banco de Dados

O sistema utiliza MySQL com as seguintes tabelas:

- cacambas
- clientes
- locacoes

---

### Tabela: cacambas

- id
- numero
- status

---

### Tabela: clientes

- id
- nome
- cpf_cnpj
- endereco
- telefone
- email

---

### Tabela: locacoes

- id
- cliente_id
- cacamba_id
- data_entrega
- data_retirada
- status_locacao
- status_pagamento
- data_entrega_real
- data_retirada_real

---

## 🔗 Integração

O sistema funciona com integração completa entre:

- Frontend
- Backend
- Banco de dados MySQL

O frontend realiza requisições para a API desenvolvida em Flask, que se comunica com o banco de dados MySQL para cadastrar, listar e atualizar as informações do sistema.

---

## 🔄 Fluxo Principal do Sistema

1. A caçamba disponível é selecionada no sistema
2. O cliente é cadastrado
3. A locação é registrada
4. O sistema gera as datas previstas de entrega e retirada
5. A entrega da caçamba é confirmada
6. O pagamento é registrado como pago
7. A retirada da caçamba é finalizada
8. A locação passa para o status finalizada

---

## ✅ Status do Projeto

Projeto finalizado com as funcionalidades das AC1, AC2, AC3 e AC4 implementadas.

O sistema contempla o fluxo completo da locação de caçambas, desde o controle de estoque até a finalização da locação.

---

## 👩‍💻 Autora

Camilla Freire

Projeto acadêmico baseado em cenário real de locação de caçambas.

---