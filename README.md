# Sistema de Aprovação de Pedidos

Projeto desenvolvido durante o bootcamp **TOTVS - Fundamentos de Engenharia de Dados e Machine Learning** da DIO.

---

## 📌 Descrição

O desafio consistiu em criar um sistema simples de automação para análise de pedidos empresariais.

O programa recebe:
- O valor do pedido
- A prioridade do pedido ("alta", "media" ou "baixa")

Com base nessas informações, o sistema decide automaticamente se o pedido será:
- aprovado
- encaminhado para revisão
- rejeitado

---

## 🚀 Tecnologias utilizadas

- Python 3

---

## 🧠 Lógica aplicada

As decisões são tomadas utilizando estruturas condicionais (`if`, `elif`, `else`) e operadores lógicos (`and`, `or`).

### Regras implementadas:

✅ Pedidos até 1000:
- prioridade alta → aprovado
- prioridade média → aprovado

⚠️ Pedidos acima de 1000:
- prioridade alta → revisão

❌ Todos os demais:
- rejeitado

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
