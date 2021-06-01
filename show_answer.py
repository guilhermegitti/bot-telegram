
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

import json

from constants import (
    SEVENTH,
    VOLTA_PYTHON,
    VOLTA_ARRAY,
    VOLTA_EST_CONTROLE,
    VOLTA_OPER,
)

with open('respostas.json', encoding='utf-8') as json_file:
    respostas = json.load(json_file, )


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
    query.edit_message_text(text=respostas['funcao'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['classe'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['lista'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['dict'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['tupla'], reply_markup=reply_markup)
    return SEVENTH


def opr_comp_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.devmedia.com.br/operadores-no-python/40693"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=respostas['operador_comparacao'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['operador_logico'], reply_markup=reply_markup)
    return SEVENTH


def opr_identi_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.devmedia.com.br/operadores-no-python/40693"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=respostas['operador_indentidade'], reply_markup=reply_markup)
    return SEVENTH


def opr_arit_python(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Referencia", url="https://www.devmedia.com.br/operadores-no-python/40693"),
            InlineKeyboardButton("DOC Python", url="https://docs.python.org/pt-br/3/tutorial/index.html"),
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_OPER)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=respostas['operador_aritmetico'], reply_markup=reply_markup)
    return SEVENTH


def python_caracteristicas(update: Update, _: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(VOLTA_PYTHON)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=respostas['python_caracteristicas'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['if_ense'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['for_while'], reply_markup=reply_markup)
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
    query.edit_message_text(text=respostas['try_except'], reply_markup=reply_markup)
    return SEVENTH


# Função de incio do bot
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Seja bem vindo ao PythonBot. Nosso compromisso é explicar para iniciantes, de forma fácil, alguns tópicos da liguagem Python. Digite /python aproveite o conteúdo!")
