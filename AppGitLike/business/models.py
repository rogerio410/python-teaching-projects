class Repositorio:

    def __init__(self, nome):
        self.nome = nome
        self.remotes = []
        self.arquivos = []

    def novo_arquivo(self, nome):
        pass

    def remover_arquivo(self, nome):
        pass


class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.linhas = []
        self.tracked = False

    def add_linha(self, linha=''):
        pass

    def remove_linha(self, index=None):
        pass


class Commit:
    pass


class Mudanca:
    pass


class StageArea:
    pass


class Remote:
    pass

