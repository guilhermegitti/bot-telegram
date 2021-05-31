import unicodedata
import re

class resposta():

    def __init__(self, user_message):
        self.user_message = user_message

    def get_answer(self):
        self._trata_user_message()

        # for i in self.user_message.split():
        #     if i in

    def _trata_user_message(self):
        self.user_message = self.user_message.lower()
        self.user_message = self._remover_acentos(self.user_message)

    def _remover_acentos(self, palavra) -> str:

        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', palavra)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)