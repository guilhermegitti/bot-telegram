from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

import logging

from constants import (
    FIRST,
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
    ARIT_PYTHON
)

logger = logging.getLogger(__name__)

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
    query.edit_message_text(text="Estruturas de Controle do Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se preferir, veja a documentação.", reply_markup=reply_markup)
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
    query.edit_message_text(text="Coleções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se preferir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH


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
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Operadores e Expressões", reply_markup=reply_markup)
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
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Estruturas de Controle do Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se preferir, veja a documentação.", reply_markup=reply_markup)
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
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Coleções em Python. Escolha o tópico da sua duvida e clique para ver um exemplo, ou se preferir, veja a documentação.", reply_markup=reply_markup)
    return SEVENTH