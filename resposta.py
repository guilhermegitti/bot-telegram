import unicodedata
import re
import json

class Resposta():

    def __init__(self, user_message):
        self.user_message = user_message
        with open('entidades.json', encoding='utf-8') as json_file:
            self.entidades = json.load(json_file, )
        with open('respostas.json', encoding='utf-8') as json_file:
            self.respostas = json.load(json_file, )

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

    def _remover_acentos(self, palavra) -> str:
        aux = ''
        if '+' in palavra:
            aux += ' + '
        if '-' in palavra:
            aux += ' - '
        if '*' in palavra:
            aux += ' * '
        if '/' in palavra:
            aux += ' / '

        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', palavra)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento) + aux