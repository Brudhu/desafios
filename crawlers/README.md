# Desafio 2: Crawlers

Solução do desafio 2 da idwall, implementada em Python.

## Requisitos:

Para rodar esse script Python, o usuário deve ter Python 3 instalado globalmente na sua máquina ou instalá-lo usando alguma ferramenta como [Anaconda](https://www.anaconda.com/). Ele foi testado apenas com a versão de Python 3.7.3 em ambiente Linux (Ubuntu 18.04).

São necessários dois pacotes Python adicionais:
* selenium
* python-telegram-bot

Que podem ser instalados usando o seguinte comando, desde que o usuário tenha o programa pip instalado em sua máquina:
```
$ cd crawlers/solucao
$ pip install -r requirements.txt
```

Além disso, para a utilização do selenium para fazer o download do código fonte da página do Reddit, é necessário que o usuário tenha o executável geckodriver na variável PATH. Para usuários Linux, disponibilizei um script que vai fazer o download desse executável e movê-lo para /usr/bin. Para rodar esse script:
```
$ sudo ./install.sh
```

Uma vez que as dependências estejam instaladas, podemos partir para a execução dos scripts.

## Como usar:

Podemos utilizar esse script para imprimir no terminal as threads dos subreddits que estejam "bombando" ou rodar um bot do telegram que retorna as threads numa conversa.

### Imprimindo no terminal:

Entre no subdiretório onde o arquivo redditcrawler.py está localizado:
```
$ cd crawlers/solucao/
```

Execute o script passando os argumentos descritos no _help_ do script:
```
$ ./redditcrawler.py -h
usage: redditcrawler.py [-h] [-n NUMBER_OF_VOTES] subreddits

Find "hot threads" in a groups of subreddits

positional arguments:
  subreddits            a list of subreddits to check separated by ";". Eg.:
                        "dogs;cats;brazil"

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_VOTES, --number-of-votes NUMBER_OF_VOTES
                        minimum number of votes for a thread to be "hot"
```

* -n NUMBER_OF_VOTES: Opcional (default: 5000) - número mínimo de up votes para considerar que uma thread está "bombando".
* subreddits: Obrigatório - lista de subreddits para buscar, separados por ";". Ex: cats;futurology

Exemplo:
```
$ ./redditcrawler.py -n 2000 'cats;futurology'
________________________________________
futurology | Impossible Burgers are hitting their first grocery stores tomorrow - the plant-based burger plans to reach every region of the US by the middle of next year.
Up votes: 42300
Link: https://www.theverge.com/2019/9/19/20869271/impossible-burger-foods-gelsons-markets-southern-california-meat-free-plant-based
Comments: https://old.reddit.com/r/Futurology/comments/d6dufc/impossible_burgers_are_hitting_their_first/

________________________________________
cats | Proud Mommy ❤
Up votes: 12200
Link: https://old.reddit.com/r/cats/comments/d6i2ze/proud_mommy/
Comments: https://old.reddit.com/r/cats/comments/d6i2ze/proud_mommy/

________________________________________
cats | Choices
Up votes: 9004
Link: https://old.reddit.com/r/cats/comments/d6ou4e/choices/
Comments: https://old.reddit.com/r/cats/comments/d6ou4e/choices/

________________________________________
cats | She’s proud of the post-diet bod.
Up votes: 8617
Link: https://old.reddit.com/r/cats/comments/d6l0ux/shes_proud_of_the_postdiet_bod/
Comments: https://old.reddit.com/r/cats/comments/d6l0ux/shes_proud_of_the_postdiet_bod/

```

Caso queira especificar o executável do Python3, o usuário pode fazer as seguintes chamadas: ```python3 redditcrawler.py -n 2000 'cats;futurology'``` ou ```/absolute/path/to/python3 redditcrawler.py -n 2000 'cats;futurology'```

### Executando o Bot do Telegram:

Também é possível receber essas respostas num Bot do Telegram. Para isso, o usuário deve criar um arquivo "credentials.py" dentro do diretório crawlers/solucao, com o seguinte conteúdo:
```
TELEGRAM_API_KEY='DIGITE_AQUI_A_API_KEY_DO_SEU_BOT'
```
Em seguida, basta chamar o script "brunosownbot.py" da mesma maneira citada anteriormente:
./brunosownbot

Depois, é só procurar pelo bot no Telegram e enviar uma mensagem com o seguinte formato:
```
/nadaparafazer cats;futurology
```
ou
```
/nadaparafazer cats futurology
```

Como exemplo, deixe o meu próprio bot rodando no Telegram. Para usá-lo, basta buscar por @BrunosOwnBot e enviar mensagens para ele.

Seguem dois prints da sua utilização:

![Exemplo de resposta](https://github.com/Brudhu/desafios/blob/master/crawlers/solucao/imagens/bot-details.jpg?raw=true)

![Informações do Bot](https://github.com/Brudhu/desafios/blob/master/crawlers/solucao/imagens/bot-example.jpg?raw=true)

## Casos Atípicos (Parâmetros):

### String subreddits vazia:

Caso a lista de subreddits seja uma string vazia, o programa vai emitir o erro ```ValueError: subreddits não pode ser uma string vazia``` e encerrar a execução.

### Parâmetro NUMBER_OF_VOTES igual a zero ou negativo:

Para casos onde NUMBER_OF_VOTES é menor ou igual a zero, o programa considerará todas as threads como "bombantes", retornando todas elas.
