# Gabarito · Compra no limite

Com o operador original, os sete casos fornecidos passam. Com `>=`, o caso `exact-stock` recebe uma exceção de estoque insuficiente quando esperava saldo zero. Os outros seis passam. O filtro retira o único exemplo em que a quantidade positiva é igual ao saldo.

Com saldo 1 e quantidade 1, o comprador também deve obter zero. Esse exemplo traduz o cenário Gherkin literalmente e detecta a mesma troca de operador. Para revelar outra classe de defeito, experimente trocar a subtração por soma e antecipe quais casos distinguem os resultados.
