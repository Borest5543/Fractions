# Aplicação para estudo de orientação a objetos, classes e heranças utilizando python.
A aplicação consiste na visualização didática de operações com frações de forma interativa através de comandos no teclado.
## Apresenta de forma visual:
- 3 Frações, 2 de entrada e 1 de saída.
- 3 Diagramas, 2 de entrada e 1 de saída.
- Simplificações das 3 Frações.
- Pointe para visualização da interação via teclado.

## Comandos
### Setas do teclado:
- '<' Esquerda: retrocede a o foco do indicador.
- '>' Direita: avança o foco do indicador. 
- '^' Cima: adiciona 1 ao número indicado pelo foco do indicador.
- 'v' Baixo: retira 1 ao número indicado pelo foco do indicador.

## Operações matemáticas
#### OS ARGUMENTOS DA INSTÂNCIAS DEVEM SEGUIR SEM ALTERAÇÃO.
- As operações matemáticas básicas (soma, subtração, multiplicação e divisão) estão disponíveis.
- Para mudar a operação é necessário alterar o comando da linha 249.
- Soma: Fraction.sum(...)
- Subtração: Fraction.subtraction(...)
- Multiplicação: Fraction.multiplication(...)
- Divisão: Fraction.division(...)

## Visualização de apenas uma fração:
#### OS ARGUMENTOS DA INSTÂNCIAS DEVEM SEGUIR SEM ALTERAÇÃO.
É possível realizar a renderização de apenas uma fração se necessário.
- Para isso é necessário comentar(#) o comando da linha 249 e descomentar() a linha 250.
