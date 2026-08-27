# Projeto locadora de filmes

Uma locadora trabalha com jogos para diferentes plataformas, como PlayStation, Xbox e Nintendo Switch.

- Cada **Jogo** possui um título, uma plataforma, um gênero e um valor de locação por dia.
- Cada **Cliente** possui nome e telefone.
- As **Locações** registram o jogo escolhido, a quantidade de dias e o valor total da locação.

A locadora oferece descontos de acordo com o período da locação:

- **Até 3 dias:** sem desconto.
- **Acima de 3 dias:** 5% de desconto.
- **Acima de 7 dias:** 10% de desconto.
- **Nota:** O desconto é aplicado sobre o valor total da locação.

### Exemplo

Considere um jogo com valor de **R$ 10,00 por dia**.

Se o cliente alugá-lo por **5 dias**:

- Valor sem desconto: **5 × R$ 10,00 = R$ 50,00**
- Desconto: **5% de R$ 50,00 = R$ 2,50**
- Valor final: **R$ 47,50**

### Considere as seguintes regras:

- **Jogo:** Possui título, plataforma, gênero, valor da diária e quantidade de cópias disponíveis.
- **Cliente:** Possui nome e telefone.
- **Locação:** Registra o cliente, o jogo escolhido, a quantidade de dias e o valor final.
- **Cópias:** Uma locação somente pode ser realizada se houver pelo menos uma cópia disponível.

### Desenvolva uma aplicação em **Python** que permita:

- Cadastrar jogos.
- Listar os jogos cadastrados.
- Cadastrar clientes.
- Listar os clientes cadastrados.
- Realizar uma locação.
- Calcular automaticamente o desconto e o valor final.
- Listar as locações realizadas.
- Atualizar a quantidade de cópias disponíveis após uma locação.

### Os dados devem ser armazenados em três arquivos diferentes:

- `jogos.json` – cadastro dos jogos.
- `clientes.json` – cadastro dos clientes.
- `locacoes.json` – histórico das locações.

Ao iniciar o programa, os dados existentes nos arquivos JSON devem ser carregados.

Sempre que um novo jogo, cliente ou locação for cadastrado, os dados correspondentes devem ser atualizados no respectivo arquivo JSON.

Use **funções, parâmetros, listas, dicionários, estruturas de decisão, estruturas de repetição, arquivos JSON** e organize o projeto em **mais de um arquivo**.

**Sugestão de organização**

```text
locadora/
├── main.py
├── jogos.py
├── clientes.py
├── locacoes.py
├── persistencia.py
├── jogos.json
├── clientes.json
└── locacoes.json
