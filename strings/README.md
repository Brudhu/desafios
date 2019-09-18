# Desafio 1: Strings

Solução do desafio 1 da idwall, implementado em Python.

## Requisitos:

Para rodar esse script Python, o usuário deve ter Python 3 instalado globalmente na sua máquina ou instalá-lo usando alguma ferramenta como [Anaconda](https://www.anaconda.com/). Ele foi testado apenas com a versão de Python 3.7.3 em ambiente Linux (Ubuntu 18.04).

## Como usar:

Existem duas maneiras de executar esse script: como um script com argumentos ou como um módulo Python que será importado em outro arquivo.

### Script no terminal:

Entre no subdiretório onde o arquivo textformatting.py está localizado:
```
$ cd strings/solucao/
```

Execute o script, passando os seguintes argumentos:
* -j : Opcional - irá justificar o texto com espaços em branco.
* -m \<max-len\>: Obrigatório - número máximo de caracteres em cada linha.
* -i \<inputfile\>: Obrigatório - arquivo com o texto que será formatado.
* -o \<outputfile\>: Opcional - arquivo onde o text formatado será salvo. Caso esse argumento não seja passado, o script irá imprimir o text formatado na tela.

Exemplo:
```
$ ./textformatting.py -j -m 40 -i example_text.txt
In the beginning God created the heavens
and   the   earth.  Now  the  earth  was
formless  and  empty,  darkness was over
the  surface of the deep, and the Spirit
of  God  was  hovering  over the waters.

And  God said, "Let there be light," and
there  was light. God saw that the light
was  good,  and  he  separated the light
from  the darkness. God called the light
"day,"   and   the  darkness  he  called
"night."  And  there  was  evening,  and
there  was  morning  -  the  first  day.

```

Para executar o script diretamente como um executável no terminal, o host deve ter o programa python3 dentro de /usr/bin: ```/usr/bin/python3```. 

Caso contrário, o usuário pode fazer a chamada utilizando o executável do interpretador de Python3: ```python3 textformatting.py -j -m 30 -i example_text.txt``` ou ```/absolute/path/to/python3 textformatting.py -j -m 30 -i example_text.txt```

### Como um módulo:
O arquivo textformatting.py pode ser importado no seu próprio arquivo com a seguinte sintaxe:
```
import textformatting as txtfmt
```
e, com isso, a função 'format_text' pode ser usada. 

Definição da função:
```
def format_text(text, max_len, justify=False):
    """ Return formatted text with max_len length and optionally justified.

    Keyword arguments:
    text -- the text (string) to be formatted
    max_len -- the max length (int) of each line of the output formatted text
    justify -- boolean to tell the function to justify the text with extra
               spaces.

    Returns:
    Text formatted properly according to the arguments (string)
    """
```

Ou seja, para formatar o text, os seguintes passos devem ser executados:
```
import textformatting as txtfmt


text = "In the beginning God created the heavens and the earth. Now "\
       "the earth was formless and empty, darkness was over the "\
       "surface of the deep, and the Spirit of God was hovering "\
       "over the waters.\n\nAnd God said, \"Let there be light,\" "\
       "and there was light. God saw that the light was good, and "\
       "he separated the light from the darkness. God called the "\
       "light \"day,\" and the darkness he called \"night.\" And "\
       "there was evening, and there was morning - the first day."
       
print(txtfmt.format_text(text, 40, True))
```

e o output do _snippet_ acima é o seguinte:

```
In the beginning God created the heavens
and   the   earth.  Now  the  earth  was
formless  and  empty,  darkness was over
the  surface of the deep, and the Spirit
of  God  was  hovering  over the waters.

And  God said, "Let there be light," and
there  was light. God saw that the light
was  good,  and  he  separated the light
from  the darkness. God called the light
"day,"   and   the  darkness  he  called
"night."  And  there  was  evening,  and
there  was  morning  -  the  first  day.
```

## Teste Unitário:

Para o teste unitário, utilizei o módulo _unittest_ do Python.

Para executar os testes unitários descritos em test_textformatting.py, basta executar o arquivo:

```
$ ./test_textformatting.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

