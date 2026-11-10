# Laboratório 1 · Permitir a compra da última unidade

## Requisito para a issue

Como cliente, quero comprar até a quantidade disponível. O saldo inicial é um inteiro não negativo. A quantidade solicitada é inteira. A regra calcula o novo saldo e informa o motivo de uma recusa.

| Saldo inicial | Quantidade | Resultado esperado |
| --- | --- | --- |
| 5 | 4 | Restar 1 |
| 5 | 5 | Restar 0 |
| 5 | 6 | Recusar por estoque insuficiente |
| 5 | 0 ou −1 | Recusar por quantidade inválida |
| 0 | 1 | Recusar por estoque insuficiente |

```gherkin
# language: pt
Funcionalidade: Compra de unidades disponíveis
  Cenário: Comprar a última unidade
    Dado que há 1 unidade disponível
    Quando solicito 1 unidade
    Então o saldo resultante é 0
```

## Execute no PowerShell

Na raiz do projeto, prepare o ambiente uma vez.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Execute a suíte e leia os nomes dos casos coletados.

```powershell
.\.venv\Scripts\python.exe -m pytest -v tests/unit
```

Abra `tests/unit/test_inventory.py`. Cada linha de dados em `parametrize` vira uma execução independente. O `assert` compara o saldo com um valor definido no requisito. Nos casos de recusa, `pytest.raises` verifica a exceção e o motivo. A função recebe apenas números, então cada caso roda sem servidor ou banco.

## Investigue a fronteira

1. Anote o resultado da suíte original. Em `inventory.py`, localize a comparação entre quantidade e saldo. Preveja quais casos falhariam se o operador passasse de `>` para `>=`.
2. Faça a troca temporária e repita a suíte. Leia a primeira falha desde os valores de entrada até a exceção. Registre qual comportamento o comprador observaria.
3. Ainda com o defeito, execute a suíte com `-k "not exact-stock"`. Explique por que o resultado muda mesmo com o mesmo código de produção.
4. Restaure `>`, execute todos os testes e escreva um caso para o cenário de uma unidade descrito acima. Avalie se ele detecta um defeito diferente.
5. Compare sua investigação com o [gabarito](gabarito-01.md).

## Pratique a revisão no GitHub

Em um repositório público com uma main inicial, abra a issue **Permitir a compra da última unidade disponível** e copie a tabela de aceite. Crie uma branch a partir de main para a entrega. Inclua a regra, os testes e o arquivo de workflow no PR. No corpo do PR, associe a issue com `Closes #N` usando o número real.

Anexe a previsão, o resumo da execução com o defeito e o resumo após a correção. Na revisão, confira se o resultado esperado veio da tabela e se a suíte detecta a recusa indevida. Antes do merge, confira o job `unit` no GitHub Actions.
