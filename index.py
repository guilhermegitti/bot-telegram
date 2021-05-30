import dotenv
import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, FOURTH, SEVENTH = range(3)
# Handlers da linguagem
PYTHON, FUNCAO_PYTHON, CLASS_PYTHON, CONTROLE_PYTHON, ARRAYS_PYTHON, OPER_EXP_PYTHON = range(6)
# call_backs
VOLTA_PYTHON, VOLTA_ARRAY, VOLTA_EST_CONTROLE, VOLTA_OPER, LISTA_PYTHON, DIC_PYTHON, TUPLA_PYTHON, IF_PYTHON, FOR_PYTHON, TRY_PYTHON, COMP_PYTHON, LOG_PYTHON, IDENT_PYTHON, ARIT_PYTHON = range(14)


# Função de incio do bot
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Seja bem vindo ao oPython Bot. Nosso compromisso é explicar para iniciantes, de forma fácil, alguns tópicos da liguagem Python. Digite /python aproveite o conteúdo!")


def python(update: Update, _: CallbackContext) -> int:
    """Send message on `/start`."""
    user = update.message.from_user
    logger.info("User %s started the conversation. Lastname is: %s", user.first_name, user.last_name)
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_PYTHON)),
        ],
        [
            InlineKeyboardButton("Classes", callback_data=str(CLASS_PYTHON))
        ],
        [
            InlineKeyboardButton("Coleções (Lista/Tupla/Dicionario)", callback_data=str(ARRAYS_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Logicos e Expressões", callback_data=str(OPER_EXP_PYTHON))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF-Else/For/While/)", callback_data=str(CONTROLE_PYTHON)),
        ],
        [
            InlineKeyboardButton("Tratamento de Exceções (Try-Except)", callback_data=str(TRY_PYTHON)),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup)
    return FOURTH


def func_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.devmedia.com.br/funcoes-em-python/37340"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""A sintaxe de uma função é definida por três partes: nome, parâmetros e corpo, o qual agrupa uma sequência de linhas que representa algum comportamento. No código abaixo, temos um exemplo de declaração de função em Python:
    "def hello(meu_nome):
        print('Olá',meu_nome)"
Essa função, de nome hello, tem como objetivo imprimir o nome que lhe é passado por parâmetro (também chamado de argumento). 
A palavra reservada def, na primeira linha, explicita a definição da função naquele ponto. 
Em seguida, entre parênteses, temos o parâmetro meu_nome. Ainda na mesma linha, observe a utilização dos dois pontos (:), 
que indicam que o código identado nas linhas abaixo faz parte da função que está sendo criada. 
Para executar a função, devemos simplesmente chamar seu nome e passar os parâmetros esperados entre parênteses, 
conforme o código a seguir.
    >>> hello(bot_python)
    Olá Bot oPython
    >>> meu_nome
    'Bot oPython'
    """, reply_markup=reply_markup)
    return SEVENTH


def classe_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://docs.python.org/pt-br/3/tutorial/classes.html"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Classes proporcionam uma forma de organizar dados e funcionalidades juntos. 
Criar uma nova classe cria um novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. 
Cada instância da classe pode ter atributos anexados a ela, para manter seu estado. 
Instâncias da classe também podem ter métodos (definidos pela classe) para modificar seu estado.
Sintaxe da definição de uma Classe:
    class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>
""", reply_markup=reply_markup)
    return SEVENTH


def colecoes_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Listas", callback_data=str(LISTA_PYTHON)),
            InlineKeyboardButton("Tuplas", callback_data=str(TUPLA_PYTHON)),
            InlineKeyboardButton("Dicionarios", callback_data=str(DIC_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Coleções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


def lista_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/listas/"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_ARRAY)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=""" É uma estrutura de dados que armazena elementos geralmente de mesmo tamanho e mesmo tipo.
Nos arranjos, os elementos ficam agrupados em grandes blocos na memória de forma sequencial, ou seja, o N-ésimo elemento ficará salvo na memória logo após o (N-1)-ésimo. 
Então, para acharmos qualquer item de um array, basta que saibamos onde está o primeiro.
No Python temos as seguntes funções para manipular Listas:
append() - Adiciona um elemento no final da lista
clear() - Remove todos os elementos da lista
copy()- Retorna uma cópia da lista
count()- Retorna o número de elementos com o valor especificado
extend()- Adiciona os elementos de uma lista (ou qualquer iterável), ao final da lista atual
index() - Retorna o índice do primeiro elemento com o valor especificado
insert() - Adiciona um elemento na posição especificada
pop() - Remove o elemento na posição especificada
remove() - Remove o primeiro item com o valor especificado
reverse() - Inverte a ordem da lista
sort() - Classifica a list
Exemplo: Append e Pop
odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.pop(2)
print(odd)
Resposta Esperada:
[1, 3, 5, 7] # odd.append(7)
[1, 3, 7] # o   dd.pop(2)
""", reply_markup=reply_markup)
    return SEVENTH


def dic_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_ARRAY)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Dicionário é um tipo diferente de coleção. Ele é um tipo de mapeamento nativo do Python. A associação, ou mapeamento, é feita a partir de uma chave, que pode ser qualquer tipo imutável, para um valor, que pode ser qualquer objeto de dados do Python.
Como exemplo, vamos criar um dicionário para traduzir palavras em Portugues para inglês. Para este dicionário, as chaves são strings.
    br_para_en = {'um': 'one', 'dois': 'two', 'tres': 'three'}
    br_para_en['um'] - retorna 'one'
Também é possivel fazer com que uma chave numerica referencie uma string, como no exemplo:
    br_para_en = {'4': 'four', '5': 'five', '6': 'six'}
    br_para_en[4] - retorna 'four'
    """, reply_markup=reply_markup)
    return SEVENTH


def tupla_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://blog.betrybe.com/tecnologia/tuplas-em-python/"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_ARRAY)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável. 
Isso significa que quando uma tupla é criada não é possível adicionar, alterar ou remover seus elementos. 
Geralmente, ela é utilizada para adicionar tipos diferentes de informações, porém, com a quantidade de elementos definidos.
# tupla com parênteses / declaração implícita
>>> tupla_numeros = (10, 20, 30)
>>> tupla_numeros
    (10, 20, 30)
>>> 
# tupla sem parênteses / declaração implícita
>>> tupla_nova = 10, 20, 30
>>> tupla_nova
    (10, 20, 30) 
É importante dizer que a utilização dos parênteses não é obrigatória. No entanto, é considerada uma boa prática. O uso da vírgula é exigido, pois se ela tiver apenas um elemento, é preciso colocar uma vírgula depois dele para que o Python entenda que se trata de uma tupla.
""", reply_markup=reply_markup)
    return SEVENTH


def oper_exp_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Operadores de Comparação", callback_data=str(COMP_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Lógicos", callback_data=str(LOG_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores de Identidade", callback_data=str(IDENT_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Aritméticos", callback_data=str(ARIT_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores e Expressões", reply_markup=reply_markup)
    return SEVENTH


def opr_comp_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Os operadores de comparação são usados para comparar valores, o que vai retornar True ou False, dependendo da condição.	
">" (Maior que) - Verifica se um valor é maior que outro	
"<" (Menor que) - Verifica se um valor é menor que outro
"==" (Igual a) - Verifica se um valor é igual a outro
"!=" (Diferente de) - Verifica se um valor é diferente de outro
">=" (Maior ou igual a)	- Verifica se um valor é maior ou igual a outro
"<=" (Menor ou igual a)	- Verifica se um valor é menor ou igual a outro
Exemplo:
soma_1 = 7 + 8
soma_2 = 10 + 5
if soma_1 == soma_2:
    print("Os resultados são iguais")
else:
    print("Os resultados são diferentes")""", reply_markup=reply_markup)
    return SEVENTH


def opr_log_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.inf.pucrs.br/pinho/PCB/ComandosDeDecisao/Decisao.htm"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Além dos operadores de comparação, existem os chamados operadores lógicos ou "conectivos lógicos". 
Estes, servem para conectar/combinar duas expressões relacionais.

And – Retorna True se todas as condições forem verdadeiras, caso contrário retorna False
Or – Retorna True se uma das condições for verdadeiras, caso contrário retorna False	
Not - Inverte o resultado: se o resultado da expressão for True, o operador retorna false

Exemplo: Operador OR
idade_lucas = 21
idade_carolina = 19
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

Exemplo: Operador AND
idade_lucas = 21
idade_carolina = 19
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")
    """, reply_markup=reply_markup)
    return SEVENTH


def opr_identi_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Os operadores de identidade servem para a comparação de objetos. Nessa comparação é verificado se eles ocupam a mesma posição na memória, o que significará que se trata do mesmo objeto.

is - Retorna True se as variáveis comparadas forem o mesmo objeto
is not - Retorna True se as variáveis comparadas não forem o mesmo objeto

Exemplo:
time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")
if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")""", reply_markup=reply_markup)
    return SEVENTH


def opr_arit_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Os operadores aritméticos são utilizados na execução de operações matemáticas, tais como a soma e a subtração, por exemplo
+ (Adição ou sinal positivo) - Realiza a soma entre operandos - Adiciona o sinal de positivo ao número
- (Subtração ou sinal negativo) - Realiza a subtração entre operandos - Adiciona o sinal de negativo ao número
* (Multiplicação) - Realiza a multiplicação entre operandos
/ (Divisão) - Realiza a divisão entre operandos
// (Divisão inteira) - Realiza a divisão entre operandos e a parte decimal do resultado
% (Módulo) - Retorna o resto da divisão entre operandos
** (Exponenciação) - Retorna um número elevado a potência de outro

Exemplos:
numero1 = 5
numero2 = 2

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
modulo = numero1 % numero2
exponenciacao = numero1 ** numero2
print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25""", reply_markup=reply_markup)
    return SEVENTH

def est_controle_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF - Else", callback_data=str(IF_PYTHON)),
        ],
        [
            InlineKeyboardButton("For - While", callback_data=str(FOR_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


def if_else_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.devmedia.com.br/python-estrutura-condicional-if-else/38217"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_EST_CONTROLE)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""O if é uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.
No código a seguir temos um exemplo de uso do if no qual verificamos se a variável idade é menor que 20. Em caso positivo, imprimimos uma mensagem na tela e em caso negativo o código seguirá normalmente, desconsiderando a linha 3.

idade = 18
if idade < 20:
    print('Você é jovem!')

Vimos anteriormente como utilizar o if para executar uma ação caso uma condição seja atendida. No entanto, nenhum comportamento específico foi definido para o caso de a condição não ser satisfeita. Quando isso é necessário, precisamos utilizar a reservada else.

idade = 18
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')

Dessa vez, caso a condição 'maior de idade' não seja atendida, definimos o fluxo alternativo que o código deve seguir. Ou seja, se a idade não for maior ou igual a 18, o bloco abaixo da palavra reservada else deverá ser executado. Nesse caso, seria executa o bloco 'menor de idade'.
""", reply_markup=reply_markup)
    return SEVENTH


def for_while_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_EST_CONTROLE)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""O comando while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida
Exemplo:
contador = 0
while (contador < 5):
    print(contador)
    contador   = contador + 1

O laço for nos permite percorrer os itens de uma coleção e, para cada um deles, executar o bloco de código declarado no loop. Sua sintaxe é a seguinte:
    for variavel in lista
    comandos
Enquanto percorremos a lista de valores, a variável indicada no for receberá, a cada iteração, um item da coleção. Assim, podemos executar algum processamento com esse elemento. No código abaixo percorremos a lista nomes e imprimimos cada elemento.
    nomes = ['Pedro', 'João', 'Leticia']
    for n in nomes:
        print(n)
""", reply_markup=reply_markup)
    return SEVENTH


def try_except_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.w3schools.com/python/python_try_except.asp"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Quando ocorre um erro, ou exceção, o Python normalmente para e gera uma mensagem de erro. 
Essas exceções podem ser tratadas usando a instrução Try afim de que o programa não gere o erro ao usuário e muito menos pare de funcionar.
    try:
        print("Olá Mundo!)
    except:
        print("Aconteceu algum erro") 
Nesse caso, ao inves de gerar um SyntaxError por conta da falta de uma " no final do print, a exceção será lançada e iŕa retornar ao usuario apenas a mensagem de erro. 
""", reply_markup=reply_markup)
    return SEVENTH


def return_colecoes_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Listas", callback_data=str(LISTA_PYTHON)),
            InlineKeyboardButton("Tuplas", callback_data=str(TUPLA_PYTHON)),
            InlineKeyboardButton("Dicionarios", callback_data=str(DIC_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Coleções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


def return_oper_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Operadores de Comparação", callback_data=str(COMP_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Lógicos", callback_data=str(LOG_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores de Identidade", callback_data=str(IDENT_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Aritméticos", callback_data=str(ARIT_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores e Expressões", reply_markup=reply_markup)
    return SEVENTH


def return_controle_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF - Else", callback_data=str(IF_PYTHON)),
        ],
        [
            InlineKeyboardButton("For - While", callback_data=str(FOR_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


def return_python(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_PYTHON)),
        ],
        [
            InlineKeyboardButton("Classes", callback_data=str(CLASS_PYTHON))
        ],
        [
            InlineKeyboardButton("Coleções (Lista/Tupla/Dicionario)", callback_data=str(ARRAYS_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Logicos e Expressões", callback_data=str(OPER_EXP_PYTHON))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF-Else/For/While/)", callback_data=str(CONTROLE_PYTHON)),
        ],
        [
            InlineKeyboardButton("Tratamento de Exceções (Try-Except)", callback_data=str(TRY_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return FOURTH


def main() -> None:
    # Carrega o dotenv
    dotenv.load_dotenv(dotenv.find_dotenv())

    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('python', python)],
        states={
            FOURTH: [
                CallbackQueryHandler(func_python, pattern='^' + str(FUNCAO_PYTHON) + '$'),
                CallbackQueryHandler(colecoes_python, pattern='^' + str(ARRAYS_PYTHON) + '$'),
                CallbackQueryHandler(classe_python, pattern='^' + str(CLASS_PYTHON) + '$'),
                CallbackQueryHandler(oper_exp_python, pattern='^' + str(OPER_EXP_PYTHON) + '$'),
                CallbackQueryHandler(est_controle_python, pattern='^' + str(CONTROLE_PYTHON) + '$'),
                CallbackQueryHandler(try_except_python, pattern='^' + str(TRY_PYTHON) + '$'),
            ],
            SEVENTH: [
                CallbackQueryHandler(return_python, pattern='^' + str(VOLTA_PYTHON) + '$'),
                CallbackQueryHandler(return_colecoes_python, pattern='^' + str(VOLTA_ARRAY) + '$'),
                CallbackQueryHandler(return_oper_python, pattern='^' + str(VOLTA_OPER) + '$'),
                CallbackQueryHandler(return_controle_python, pattern='^' + str(VOLTA_EST_CONTROLE) + '$'),
                CallbackQueryHandler(lista_python, pattern='^' + str(LISTA_PYTHON) + '$'),
                CallbackQueryHandler(dic_python, pattern='^' + str(DIC_PYTHON) + '$'),
                CallbackQueryHandler(tupla_python, pattern='^' + str(TUPLA_PYTHON) + '$'),
                CallbackQueryHandler(opr_comp_python, pattern='^' + str(COMP_PYTHON) + '$'),
                CallbackQueryHandler(opr_log_python, pattern='^' + str(LOG_PYTHON) + '$'),
                CallbackQueryHandler(opr_identi_python, pattern='^' + str(IDENT_PYTHON) + '$'),
                CallbackQueryHandler(opr_arit_python, pattern='^' + str(ARIT_PYTHON) + '$'),
                CallbackQueryHandler(if_else_python, pattern='^' + str(IF_PYTHON) + '$'),
                CallbackQueryHandler(for_while_python, pattern='^' + str(FOR_PYTHON) + '$'),
            ],
        },
        fallbacks=[CommandHandler('python', python)],
    )

    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()