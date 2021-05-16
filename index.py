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
FIRST, SECOND, THIRD = range(3)
# Callback data
ONE, TWO, THREE, FOUR = range(4)
# Languages
JS, PYTHON, JAVA = range(3)
# Estrutura
IF = range(1)

# Função de incio do bot
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Bem vindos ao nosso bot que tem como meta ajudar a duvidas simples de programação. Digite /linguagens e faça bom uso!")

# Opções de linguagens
def linguagens(update: Update, _: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation. Lastname is: %s", user.first_name, user.last_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("JavaScript", callback_data=str(JS)),
            InlineKeyboardButton("Java", callback_data=str(JAVA))],
            [
            InlineKeyboardButton("Python", callback_data=str(PYTHON)),
            ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Escolha a Linguagem relacionada a sua duvida:", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

# Escolhas do JavaScript
def javascript(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("FUNÇÕES", callback_data=str(ONE)),
            InlineKeyboardButton("IF/ELSE", callback_data=str(TWO))],
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
            InlineKeyboardButton("FUNÇÕES", callback_data=str(ONE)),
            InlineKeyboardButton("IF/ELSE", callback_data=str(TWO))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Java selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND


# Escolhas do Python
def python(update: Update, _: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("FUNÇÕES", callback_data=str(ONE)),
            InlineKeyboardButton("IF/ELSE", callback_data=str(IF)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Python selecionado. Em qual dessas partes da linguagem está a duvida?", reply_markup=reply_markup
    )
    return SECOND


# Referente ao IF/ELSE do JavaScript
def js_if(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Exemplificação em uso", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC JavaScript", url="https://api.telegram.org"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="No JavaScript o IF tem seguinte formação, por exemplo: IF argumento1 > argumento2:", reply_markup=reply_markup)
    return SECOND


# Referente ao IF/ELSE do Java
def java_if(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Exemplificação em uso", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC Java", url="https://api.telegram.org")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="No Java o IF tem seguinte formação, por exemplo: IF (argumento1 > argumento2)", reply_markup=reply_markup)
    return SECOND


# Referente ao IF/ELSE do Python
def python_if(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Exemplificação em uso", url="https://api.telegram.org"),
            InlineKeyboardButton("DOC Python", url="https://api.telegram.org"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="No Python o IF tem seguinte formação, por exemplo: IF argumento1 > argumento2:", reply_markup=reply_markup)
    return SECOND


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

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('linguagens', linguagens)],
        states={
            FIRST: [
                CallbackQueryHandler(javascript, pattern='^' + str(JS) + '$'), # retorna a parte do javascript
                CallbackQueryHandler(java, pattern='^' + str(JAVA) + '$'), # retorna a parte do java
                CallbackQueryHandler(python, pattern='^' + str(PYTHON) + '$'), # retorna a parte do python
            ],
            SECOND: [ # pegando o primeiro parametro, testando IF python
                CallbackQueryHandler(js_if, pattern='^' + str(TWO) + '$'), # retorna a parte de IF/ELSE do python
                CallbackQueryHandler(java_if, pattern='^' + str(TWO) + '$'), # retorna a parte de IF/ELSE do python
                CallbackQueryHandler(python_if, pattern='^' + str(IF) + '$'), # retorna a parte de IF/ELSE do python
                CallbackQueryHandler(end, pattern='^' + str(ONE) + '$'),
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