from typing import List


class Repositorio:

    def __init__(self, nome):
        self.nome = nome
        self.remotes = []
        self.arquivos = []

    def novo_arquivo(self, nome):
        if nome in [a.nome for a in self.arquivos]:
            raise NameError('Já existe um arquivo com este nome.')

        arquivo = Arquivo(nome)
        self.arquivos.append(arquivo)

    def remover_arquivo(self, nome):
        pass

    # Git Commands
    def add(self, nome_arquivo: str):
        for arquivo in self.arquivos:
            if arquivo.nome == nome_arquivo:
                arquivo.add()

    # Propriedades
    def tracked_files(self):
        return list(filter(lambda x: x.tracked, self.arquivos))

    def untracked_files(self):
        return list(filter(lambda x: not x.tracked, self.arquivos))


class Arquivo:

    def __init__(self, nome):
        self.nome = nome
        self.linhas: List[str] = []
        self.mudancas: List[Mudanca] = []
        self.tracked = False

    def add(self):
        if self.tracked:
            for mudanca in self.mudancas:
                mudanca.marks_as_staged()
        else:
            self.tracked = True
            self.mudancas.append(Mudanca('New file', staged=True))

    def add_linha(self):
        if self.tracked:
            self.mudancas.append('New Line')

    def remove_linha(self):
        if self.tracked:
            self.mudancas.append('Removed Line')


class Commit:
    pass


class Mudanca:

    def __init__(self, tipo, staged=False):
        self.tipo = tipo
        self.added = False
        self.staged = staged

    def mark_as_added(self):
        self.added = True

    def marks_as_staged(self):
        self.staged = True


class StageArea:
    pass


class Remote:
    pass

