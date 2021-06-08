import unicodedata
import re
import json
import pickle
import nltk
from nltk.tokenize import word_tokenize

from constants import COLUNAS


class Resposta():

    def __init__(self, user_message):
        self.user_message = user_message

        with open('entidades.json', encoding='utf-8') as json_file:
            self.entidades = json.load(json_file, )

        with open('respostas.json', encoding='utf-8') as json_file:
            self.respostas = json.load(json_file, )

        self.colunas = COLUNAS

    def get_answer(self):
        self._trata_user_message()
        for i in self.user_message.split():
            for key, value in self.entidades.items():
                if i in value:
                    return self.respostas[key]

        return 'Resposta não encontrada. Pode dizer de outra forma?'

    def _trata_user_message(self):
        self.user_message = self.user_message.lower()
        self.user_message = self._remover_acentos(self.user_message)

    def remover_acentos(self, palavra) -> str:
        aux = ''
        if '+' in palavra:
            aux += ' + '
        if '-' in palavra:
            aux += ' - '
        if '*' in palavra:
            aux += ' * '
        if '/' in palavra:
            aux += ' / '

        palavra.replace(',', ' ')
        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', palavra).encode(
            'ASCII', 'ignore').decode('ASCII')
        palavraSemAcento = u"".join(
            [c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento) + aux

    def predict_bag_of_words(self, model):

        self.user_message = self.user_message.lower()

        self.user_message = [item for item in word_tokenize(self.user_message)]

        mensagem_cliente_filtrada = []
        for i in self.user_message:
            mensagem_cliente_filtrada.append(self.remover_acentos(i))

        try:
            while True:
                mensagem_cliente_filtrada.remove('')
        except ValueError:
            pass

        stemmer = nltk.stem.RSLPStemmer()
        mensagem_cliente_com_funcao_stemmer = []
        for i in mensagem_cliente_filtrada:
            mensagem_cliente_com_funcao_stemmer.append(stemmer.stem(i))
        mensagem_cliente_com_funcao_stemmer

        dict_colunas = {}

        for i in self.colunas:
            dict_colunas[i] = 0

        for i in mensagem_cliente_com_funcao_stemmer:
            if i in dict_colunas.keys():
                dict_colunas[i] += 1
        array = list(dict_colunas.values())

        entrada = [array]

        response = self.respostas[model.predict(entrada)[0]]

        return response
