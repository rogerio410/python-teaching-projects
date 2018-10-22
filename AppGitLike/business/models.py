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

    def buscar_arquivo(self, nome_arquivo: str):
        for arquivo in self.arquivos:
            if arquivo.nome == nome_arquivo:
                return arquivo
        return None

    # Git Commands and features
    def add(self, nome_arquivo: str):
        for arquivo in self.arquivos:
            if arquivo.nome == nome_arquivo:
                arquivo.add()

    # Propriedades
    def tracked_files(self):
        return list(filter(lambda x: x.tracked, self.arquivos))

    def untracked_files(self):
        return list(filter(lambda x: not x.tracked, self.arquivos))

    def unstaged_changes(self):
        lista_mudancas = []
        for a in self.tracked_files():
            for m in a.unstaged_mudancas():
                lista_mudancas.append(m)
        return lista_mudancas

    def staged_changes(self):
        lista_mudancas = []
        for a in self.tracked_files():
            for m in a.staged_mudancas():
                lista_mudancas.append(m)
        return lista_mudancas


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
            self.mudancas.append(Mudanca(self, 'New file', staged=True))

    def add_linha(self):
        if self.tracked:
            self.mudancas.append(Mudanca(self, 'New Line'))

    def remove_linha(self):
        if self.tracked:
            self.mudancas.append(Mudanca(self, 'Removed line'))

    # propriedades
    def unstaged_mudancas(self):
        return list(filter(lambda x: not x.staged, self.mudancas))

    def staged_mudancas(self):
        return list(filter(lambda x: x.staged, self.mudancas))


class Commit:
    pass


class Mudanca:

    def __init__(self, arquivo, tipo, staged=False):
        self.tipo = tipo
        self.added = False
        self.staged = staged
        self.arquivo = arquivo

    def mark_as_added(self):
        self.added = True

    def marks_as_staged(self):
        self.staged = True


class StageArea:
    pass


class Remote:
    pass

