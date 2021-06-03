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
    MessageHandler,
    Filters,
)
import pickle

import botoes
import show_answer
from resposta import Resposta
from constants import (
    FOURTH,
    SEVENTH,
    PYTHON,
    FUNCAO_PYTHON,
    CLASS_PYTHON,
    CONTROLE_PYTHON,
    ARRAYS_PYTHON,
    OPER_EXP_PYTHON,
    VOLTA_PYTHON,
    VOLTA_ARRAY,
    VOLTA_EST_CONTROLE,
    VOLTA_OPER,
    LISTA_PYTHON,
    DIC_PYTHON,
    TUPLA_PYTHON,
    IF_PYTHON,
    FOR_PYTHON,
    TRY_PYTHON,
    COMP_PYTHON,
    LOG_PYTHON,
    IDENT_PYTHON,
    ARIT_PYTHON,
    PYTHON
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

class ChatBot():

    def __init__(self):
        modelo = open('bag_of_words_modelo', 'rb')
        self.model = pickle.load(modelo)
        modelo.close()

    def echo(self, update: Update, _: CallbackContext) -> None:
        """Echo the user message."""
        print(update.message.text)
        resposta_obj = Resposta(update.message.text)
        update.message.reply_text(resposta_obj.predict_bag_of_words(self.model))


    def main(self) -> None:
        # Carrega o dotenv
        dotenv.load_dotenv(dotenv.find_dotenv())

        # Create the Updater and pass it your bot's token.
        updater = Updater(os.getenv("TOKEN"))

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        # Setup conversation handler with the states
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('python', botoes.python)],
            states={
                FOURTH: [
                    CallbackQueryHandler(show_answer.python_caracteristicas, pattern='^' + str(PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.func_python, pattern='^' + str(FUNCAO_PYTHON) + '$'),
                    CallbackQueryHandler(botoes.colecoes_python, pattern='^' + str(ARRAYS_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.classe_python, pattern='^' + str(CLASS_PYTHON) + '$'),
                    CallbackQueryHandler(botoes.oper_exp_python, pattern='^' + str(OPER_EXP_PYTHON) + '$'),
                    CallbackQueryHandler(botoes.est_controle_python, pattern='^' + str(CONTROLE_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.try_except_python, pattern='^' + str(TRY_PYTHON) + '$'),
                ],
                SEVENTH: [
                    CallbackQueryHandler(botoes.return_python, pattern='^' + str(VOLTA_PYTHON) + '$'),
                    CallbackQueryHandler(botoes.return_colecoes_python, pattern='^' + str(VOLTA_ARRAY) + '$'),
                    CallbackQueryHandler(botoes.return_oper_python, pattern='^' + str(VOLTA_OPER) + '$'),
                    CallbackQueryHandler(botoes.return_controle_python, pattern='^' + str(VOLTA_EST_CONTROLE) + '$'),
                    CallbackQueryHandler(show_answer.lista_python, pattern='^' + str(LISTA_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.dic_python, pattern='^' + str(DIC_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.tupla_python, pattern='^' + str(TUPLA_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.opr_comp_python, pattern='^' + str(COMP_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.opr_log_python, pattern='^' + str(LOG_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.opr_identi_python, pattern='^' + str(IDENT_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.opr_arit_python, pattern='^' + str(ARIT_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.if_else_python, pattern='^' + str(IF_PYTHON) + '$'),
                    CallbackQueryHandler(show_answer.for_while_python, pattern='^' + str(FOR_PYTHON) + '$'),
                ],
            },
            fallbacks=[CommandHandler('python', botoes.python)],
        )

        updater.dispatcher.add_handler(CommandHandler('start', show_answer.start))

        # Add ConversationHandler to dispatcher that will be used for handling updates
        dispatcher.add_handler(conv_handler)

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()

if __name__ == '__main__':
    ChatBot().main()
    