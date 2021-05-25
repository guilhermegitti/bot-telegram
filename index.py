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
FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH = range(7)
# Callback data
ONE, TWO, THREE, FOUR, FIVE, RETURN_LING_JS, RETURN_LING_JAVA, RETURN_LING_PYTHON = range(8)
# Handlers das linguagens
JS, FUNCAO_JS, CONTROLE_JS, ARRAYS_JS, OPER_EXP_JS, VOLTA_JS = range(6)
PYTHON, FUNCAO_PYTHON, CONTROLE_PYTHON, ARRAYS_PYTHON, OPER_EXP_PYTHON, VOLTA_JAVA = range(6)
JAVA, FUNCAO_JAVA, CONTROLE_JAVA, ARRAYS_JAVA, OPER_EXP_JAVA, VOLTA_PYTHON = range(6)

# Função de incio do bot
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Bem vindos ao nosso bot que tem como meta ajudar a duvidas simples de programação. Digite /linguagens e faça bom uso!")

# Opções de linguagens
def linguagens(update: Update, _: CallbackContext) -> int:
    """Send message on `/start`."""
    user = update.message.from_user
    logger.info("User %s started the conversation. Lastname is: %s", user.first_name, user.last_name)
    keyboard = [
        [
            InlineKeyboardButton("JavaScript", callback_data=str(ONE)),
            InlineKeyboardButton("Java", callback_data=str(TWO))
        ],
        [
            InlineKeyboardButton("Python", callback_data=str(THREE)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Escolha a Linguagem relacionada a sua duvida:", reply_markup=reply_markup)
    return FIRST


# Escolhas do JavaScript
def javascript(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_JS)),
        ],
        [
            InlineKeyboardButton("Arrays", callback_data=str(ARRAYS_JS))
        ],
        [
            InlineKeyboardButton("Operadores e Expressões", callback_data=str(OPER_EXP_JS))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_JS))
        ],
        [
            InlineKeyboardButton("Voltar", callback_data=str(RETURN_LING_JS))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="JavaSciprt selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return SECOND


# Escolhas do Java
def java(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_JAVA)),
        ],
        [
            InlineKeyboardButton("Arrays", callback_data=str(ARRAYS_JAVA))
        ],
        [
            InlineKeyboardButton("Operadores e Expressões", callback_data=str(OPER_EXP_JAVA))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_JAVA))
        ],
        [
            InlineKeyboardButton("Voltar", callback_data=str(RETURN_LING_JAVA))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Java selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return THIRD


# Escolhas do Python
def python(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_PYTHON)),
        ],
        [
            InlineKeyboardButton("Arrays", callback_data=str(ARRAYS_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores e Expressões", callback_data=str(OPER_EXP_PYTHON))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_PYTHON)),
        ],
        [
            InlineKeyboardButton("Voltar", callback_data=str(RETURN_LING_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Python selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return FOURTH


# Opções de linguagens
def return_linguagens(update: Update, _: CallbackContext) -> int:
    """Send message on `/start`."""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("JavaScript", callback_data=str(ONE)),
            InlineKeyboardButton("Java", callback_data=str(TWO))
        ],
        [
            InlineKeyboardButton("Python", callback_data=str(THREE)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Escolha a Linguagem relacionada a sua duvida:", reply_markup=reply_markup
    )
    return FIRST


# Funcoes no javascript
def func_js(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Declarar Função", url="https://api.telegram.org"),
            InlineKeyboardButton("Arrow Function", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC JavaScript", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JS))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Funções em JavaScript. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return FIFTH


# Funcoes no java
def func_java(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Declarar Funções", url="https://api.telegram.org"),
            InlineKeyboardButton("Função Main", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC Java", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JAVA))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Funções em Java. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SIXTH


# Funcoes no python
def func_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Declarar Função", url="https://api.telegram.org"),
            InlineKeyboardButton("Python é bom", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Funções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH



# Arrays no javascript
def array_js(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Arrays", url="https://api.telegram.org"),
            InlineKeyboardButton("Manipulando arrays", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC JavaScript", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JS))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Arrays em JavaScript. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return FIFTH


# Arrays no java
def array_java(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Arrays", url="https://api.telegram.org"),
            InlineKeyboardButton("Manipulando arrays", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC Java", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JAVA))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Arrays em Java. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SIXTH


# Arrays no python
def array_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Arrays", url="https://api.telegram.org"),
            InlineKeyboardButton("Dicionarios", url="https://api.telegram.org"),
            InlineKeyboardButton("Tuplas", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Arrays em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


# Operadores e Expressoes no javascript
def oper_exp_js(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Operadores Logicos", url="https://api.telegram.org"),
            InlineKeyboardButton("Expressoes", url="https://api.telegram.org")
        ],
        [
            InlineKeyboardButton("Mais coisas", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC JavaScript", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JS))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores e Expressões em JavaScript. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return FIFTH


# Operadores e Expressoes no java
def oper_exp_java(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Operadores Logicos", url="https://api.telegram.org"),
            InlineKeyboardButton("Expressoes", url="https://api.telegram.org")
        ],
        [
            InlineKeyboardButton("Mais coisas", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC Java", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JAVA))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores e Expressões em Java. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SIXTH


# Operadores e Expressoes no python
def oper_exp_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Operadores Logicos", url="https://api.telegram.org"),
            InlineKeyboardButton("Expressoes", url="https://api.telegram.org")
        ],
        [
            InlineKeyboardButton("Mais coisas", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores e Expressões em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


# Estrutura de controle javascript
def est_controle_js(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF/ELSE", url="https://api.telegram.org"),
            InlineKeyboardButton("FOR", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("WHILE", url="https://api.telegram.org"),
            InlineKeyboardButton("SWITCH", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC JavaScript", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JS))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do JavaScript. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return FIFTH


# Estrutura de controle java
def est_controle_java(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF/ELSE", url="https://api.telegram.org"),
            InlineKeyboardButton("FOR", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("WHILE", url="https://api.telegram.org"),
            InlineKeyboardButton("SWITCH", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC Java", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_JAVA))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Java. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SIXTH


# Estrutura de controle python
def est_controle_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF/ELSE", url="https://api.telegram.org"),
            InlineKeyboardButton("FOR", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("WHILE", url="https://api.telegram.org"),
            InlineKeyboardButton("SWITCH", url="https://api.telegram.org"),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


# Escolhas do JavaScript
def return_js(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_JS)),
        ],
        [
            InlineKeyboardButton("Arrays", callback_data=str(ARRAYS_JS))
        ],
        [
            InlineKeyboardButton("Operadores e Expressões", callback_data=str(OPER_EXP_JS))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_JS))
        ],
        [
            InlineKeyboardButton("Voltar", callback_data=str(RETURN_LING_JS))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="JavaSciprt selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return SECOND



# Escolhas do Java
def return_java(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_JAVA)),
        ],
        [
            InlineKeyboardButton("Arrays", callback_data=str(ARRAYS_JAVA))
        ],
        [
            InlineKeyboardButton("Operadores e Expressões", callback_data=str(OPER_EXP_JAVA))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_JAVA))
        ],
        [
            InlineKeyboardButton("Voltar", callback_data=str(RETURN_LING_JAVA))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Java selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return THIRD


# Escolhas do Python
def return_python(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Funções", callback_data=str(FUNCAO_PYTHON)),
        ],
        [
            InlineKeyboardButton("Arrays", callback_data=str(ARRAYS_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores e Expressões", callback_data=str(OPER_EXP_PYTHON))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_PYTHON)),
        ],
        [
            InlineKeyboardButton("Voltar", callback_data=str(RETURN_LING_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Python selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return FOURTH


def end(update: Update, _: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    # Carrega o dotenv
    dotenv.load_dotenv(dotenv.find_dotenv())

    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('linguagens', linguagens)],
        states={
            FIRST: [
                CallbackQueryHandler(javascript, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(java, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(python, pattern='^' + str(THREE) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(return_linguagens, pattern='^' + str(RETURN_LING_JS) + '$'),
                CallbackQueryHandler(func_js, pattern='^' + str(FUNCAO_JS) + '$'),
                CallbackQueryHandler(array_js, pattern='^' + str(ARRAYS_JS) + '$'),
                CallbackQueryHandler(oper_exp_js, pattern='^' + str(OPER_EXP_JS) + '$'),
                CallbackQueryHandler(est_controle_js, pattern='^' + str(CONTROLE_JS) + '$'),
            ],
            THIRD: [
                CallbackQueryHandler(return_linguagens, pattern='^' + str(RETURN_LING_JAVA) + '$'),
                CallbackQueryHandler(func_java, pattern='^' + str(FUNCAO_JAVA) + '$'),                
                CallbackQueryHandler(array_java, pattern='^' + str(ARRAYS_JAVA) + '$'),
                CallbackQueryHandler(oper_exp_java, pattern='^' + str(OPER_EXP_JAVA) + '$'),
                CallbackQueryHandler(est_controle_java, pattern='^' + str(CONTROLE_JAVA) + '$'),
            ],
            FOURTH: [
                CallbackQueryHandler(return_linguagens, pattern='^' + str(RETURN_LING_PYTHON) + '$'),
                CallbackQueryHandler(func_python, pattern='^' + str(FUNCAO_PYTHON) + '$'),
                CallbackQueryHandler(array_python, pattern='^' + str(ARRAYS_PYTHON) + '$'),
                CallbackQueryHandler(oper_exp_python, pattern='^' + str(OPER_EXP_PYTHON) + '$'),
                CallbackQueryHandler(est_controle_python, pattern='^' + str(CONTROLE_PYTHON) + '$'),
            ],
            FIFTH: [
                CallbackQueryHandler(return_js, pattern='^' + str(VOLTA_JS) + '$'),
            ],
            SIXTH: [
                CallbackQueryHandler(return_java, pattern='^' + str(VOLTA_JAVA) + '$'),
            ],
            SEVENTH: [
                CallbackQueryHandler(return_python, pattern='^' + str(VOLTA_PYTHON) + '$'),
            ],
        },
        fallbacks=[CommandHandler('linguagens', linguagens)],
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