# :alien: Closest Aliens

**Número da Lista**: Dupla 3<br>
**Conteúdo da Disciplina**: Dividir e Conquistar (D&C)<br>

## Alunos 
|Matrícula | Aluno |
| -- | -- |
| 19/0089792  |  João Victor Correia de Oliveira |
| 19/0020601  |  Victor Buendia Cruz de Alvim |

## Sobre 
O projeto **Closest Aliens** é um jogo simples feito com Pygame para a utilização do algoritmo de *Par de Pontos mais Próximos* usando o método de Dividir e Conquistar.

No jogo, você é uma nave espacial que precisa ir eliminando os alienígenas em ovnis usando seus mísseis. Como os aliens possuem uma capacidade de reagir rapidamente, você precisa sempre eliminar os dois aliens mais próximos, para impedir que eles consigam espalhar a mensagem de ataque para os outros.

Se você tocar em algum alienígena sem querer, o jogo acaba! Se você atirar em algum alienígena que não está marcado (os comparsas mais próximos), você perde ponto.

A movimentação da nave é feita usando as setinhas do teclado e o tiro do míssil é feito usando a barra de espaço.

:bulb: **BÔNUS**: No nosso jogo, criamos um menu para ordenar doze instrumentos musicais em ordem de preferência sua. A partir dessa lista ordenada, comparamos a seleção feita com a pré seleção de seis gêneros musicais (Bossa Nova, Dubstep, Hip Hop, Jazz, Pop e Rock) para calcular o número de inversões da lista criada com uma "lista ideal" de ordem de instrumentos para cada gênero musical.

Dessa forma, o gênero com menor número de inversões comparado à ordenação feita pelo usuário é selecionado para ser a música tema do jogo!

## Screenshots
![Tela Inicial](/images/homescreen.png)

![Jogo](/images/jogo.png)

![Tela Game Over](/images/gameoverscreen.png)

![Escolha da Música](/images/musica.png)

## Instalação 
**Linguagem**: Python<br>
**Framework**: Pygame e Tkinter<br>

## Uso 
Antes de rodar propriamente o projeto, precisamos garantir que alguns pré requisitos estão instalados no seu computador:

- Python
- Tkinter

Descubra qual a versão do Python você está usando:

```
python3 --version

ou

python --version
```

Agora, você precisa instalar o **Tkinter** usando a versão do Python que você tem 3.10 (por exemplo):

```
# 👇️ === UBUNTU / DEBIAN ===
sudo apt-get install python3-tk

# 🚨 Make sure to specify correct Python version using python3 --version.
# For example, my Python v is 3.10, so I would install as
sudo apt-get install python3.10-tk

# 👇️ === MacOS ===
brew install python-tk@3.10

# 🚨 Make sure to specify correct Python version  using python3 --version.
# For example, if you run Python v3.9 run adjust command to
brew install python-tk@3.9

# 👇️ === Fedora ===
sudo dnf install python3-tkinter

# 👇️ === CentOS ===
sudo yum install python3-tkinter
```

Para rodar o projeto, iremos criar um ambiente virtual do python para instalar o pygame e depois rodar o nosso joguinho. Abra seu terminal e rode o seguinte comando:

```
python3 -m venv .pv && source .pv/bin/activate && pip3 install -r requirements.txt && python3 main.py
```

## Outros 
Abaixo estão os créditos das músicas usadas no projeto e das imagens usadas.

Rock:
https://www.youtube.com/watch?v=lPHRxfQsDSk&list=PL9NkUAXO8Xdk7-Ovxae0_Wf5Zb9l0K9gX

Jazz:
https://www.youtube.com/watch?v=FLsQKYXezHw

Pop:
https://www.youtube.com/watch?v=c1ElC8NkiPI

Bossa Nova:
https://www.youtube.com/watch?v=wkthWMq7-wI

Dubstep:
https://www.youtube.com/watch?v=sv8lfUr4DHw

Hip Hop:
https://www.youtube.com/watch?v=ioMCCFlE9xs

Imagens:

https://www.istockphoto.com/br/vetor/pixel-art-ufo-gm689045030-126922383

https://br.pinterest.com/pin/335729347220890293/

https://www.reddit.com/r/PixelArt/comments/f1wg26/space_background/
