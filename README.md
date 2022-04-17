# Sobre o projeto
A aplicação consiste na visualização didática de operações com frações de forma interativa através de comandos no teclado.
A aplicação se destina a ensino de frações a alunos da eduação fundamental 2 primeiros anos (6º e 7º), com a construção de frações, leitura e interpretação de diagramas, operação com frações e simplificação de frações.

# Tecnologias utilizadas
- python 3
- biblioteca pygames
- biblioteca lcm
- bilbioteca time

# Apresentação de forma visual:
- 3 Frações, 2 de entrada e 1 de saída.
- 3 Diagramas, 2 de entrada e 1 de saída.
- Simplificações das 3 Frações.
- Pointe para visualização da interação via teclado.
![soma de frações](https://drive.google.com/drive/folders/1fuSvicXU-k8ltQL319IY_cM34HLSrjvQ)
## Frações impróprias:
Para as frações impróprias foi adotado uma notação, que a cada novo número inteiro é adicionado uma nova barra menor ao lado do corpo do diagrama para representar um diagrama completo.
## Números negativos:
Em casos de números negativos a coloração da fração negativa será representada em violeta para facilitar a identificação de negativo.
## Denominador igual a 0:
Em casos de denominadores iguais a zero, uma mensagem de que não é possível dividir por zero aparecerá na tela.

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
