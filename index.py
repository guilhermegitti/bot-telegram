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
FIRST, SECOND, THIRD, FOURTH = range(4)
# Callback data
ONE, TWO, THREE, FOUR = range(4)
# End
END = range(1)
# Handlers das linguagens
JS, FUNCAO_JS, CONTROLE_JS = range(3)
PYTHON, FUNCAO_PYTHON, CONTROLE_PYTHON = range(3)
JAVA, FUNCAO_JAVA, CONTROLE_JAVA = range(3)

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
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_JS))
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
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_JAVA))
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
            InlineKeyboardButton("Estruturas de Controle (IF/ELSE/FOR/WHILE/SWITCH)", callback_data=str(CONTROLE_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Python selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return FOURTH


# Referente a funcoes do JavaScript
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
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Funções em JavaScript. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return END


# Referente a funcoes do Java
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
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Funções em Java. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return END


# Referente a funcoes do python
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
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Funções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return END


# Referente ao IF/ELSE do JavaScript
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
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do JavaScript. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return END


# Referente ao IF/ELSE do Java
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
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Java. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return END


# Referente ao IF/ELSE do Python
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
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se prefir, veja a documentação.", reply_markup=reply_markup)
    return END


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
                CallbackQueryHandler(func_js, pattern='^' + str(FUNCAO_JS) + '$'),
                CallbackQueryHandler(est_controle_js, pattern='^' + str(CONTROLE_JS) + '$'),
            ],
            THIRD: [
                CallbackQueryHandler(func_java, pattern='^' + str(FUNCAO_JAVA) + '$'),                
                CallbackQueryHandler(est_controle_java, pattern='^' + str(CONTROLE_JAVA) + '$'),
            ],
            FOURTH: [
                CallbackQueryHandler(func_python, pattern='^' + str(FUNCAO_PYTHON) + '$'),
                CallbackQueryHandler(est_controle_python, pattern='^' + str(CONTROLE_PYTHON) + '$'),
            ],
            END: [
                CallbackQueryHandler(end, pattern='^' + str() + '$'),
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