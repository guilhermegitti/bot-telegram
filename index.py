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
VOLTA_PYTHON, VOLTA_ARRAY, VOLTA_EST_CONTROLE, LISTA_PYTHON, DIC_PYTHON, TUPLA_PYTHON, IF_PYTHON, FOR_PYTHON = range(8)


# Função de incio do bot
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Bem vindos ao nosso bot que tem como meta explicar de forma fácil temas da linguagem Python. Digite /python e faça bom uso!")


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
            InlineKeyboardButton("Coleções (Lista/Tuplas/Dicionario)", callback_data=str(ARRAYS_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Logicos e Expressões", callback_data=str(OPER_EXP_PYTHON))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE)", callback_data=str(CONTROLE_PYTHON)),
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
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Funções em Python...""", reply_markup=reply_markup)
    return SEVENTH


def classe_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Classes em Python...", reply_markup=reply_markup)
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
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
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
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_ARRAY)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Listas em Python...""", reply_markup=reply_markup)
    return SEVENTH


def dic_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/dicionarios/    "),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_ARRAY)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Dicionarios em Python...""", reply_markup=reply_markup)
    return SEVENTH


def tupla_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/tuplas/"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_ARRAY)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""Tupla em Python...""", reply_markup=reply_markup)
    return SEVENTH


def oper_exp_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.w3schools.com/python/python_operators.asp"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores Logicos e Expressoes...", reply_markup=reply_markup)
    return SEVENTH


def est_controle_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF/ELSE", callback_data=str(IF_PYTHON)),
        ],
        [
            InlineKeyboardButton("FOR/WHILE", callback_data=str(FOR_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
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
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_EST_CONTROLE)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""IF/ELSE em Python...""", reply_markup=reply_markup)
    return SEVENTH


def for_while_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://algoritmosempython.com.br/cursos/programacao-python/fluxo-controle/"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_EST_CONTROLE)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="""FOR/WHILE em Python...""", reply_markup=reply_markup)
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
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Coleções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


def return_controle_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("IF/ELSE", callback_data=str(IF_PYTHON)),
            InlineKeyboardButton("FOR/WHILE", callback_data=str(FOR_PYTHON)),
        ],
        [
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
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
            InlineKeyboardButton("Coleções (Lista/Tuplas/Dicionario)", callback_data=str(ARRAYS_PYTHON)),
        ],
        [
            InlineKeyboardButton("Operadores Logicos e Expressões", callback_data=str(OPER_EXP_PYTHON))
        ],
        [
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE)", callback_data=str(CONTROLE_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
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
        entry_points=[CommandHandler('python', python)],
        states={
            FOURTH: [
                CallbackQueryHandler(func_python, pattern='^' + str(FUNCAO_PYTHON) + '$'),
                CallbackQueryHandler(colecoes_python, pattern='^' + str(ARRAYS_PYTHON) + '$'),
                CallbackQueryHandler(classe_python, pattern='^' + str(CLASS_PYTHON) + '$'),
                CallbackQueryHandler(oper_exp_python, pattern='^' + str(OPER_EXP_PYTHON) + '$'),
                CallbackQueryHandler(est_controle_python, pattern='^' + str(CONTROLE_PYTHON) + '$'),
            ],
            SEVENTH: [
                CallbackQueryHandler(return_python, pattern='^' + str(VOLTA_PYTHON) + '$'),
                CallbackQueryHandler(return_colecoes_python, pattern='^' + str(VOLTA_ARRAY) + '$'),
                CallbackQueryHandler(return_controle_python, pattern='^' + str(VOLTA_EST_CONTROLE) + '$'),
                CallbackQueryHandler(lista_python, pattern='^' + str(LISTA_PYTHON) + '$'),
                CallbackQueryHandler(dic_python, pattern='^' + str(DIC_PYTHON) + '$'),
                CallbackQueryHandler(tupla_python, pattern='^' + str(TUPLA_PYTHON) + '$'),
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