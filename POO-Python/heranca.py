class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao =descricao
        self.inscritos = inscritos
    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao,inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property
    def equipe(self):
        return self._equipe

    def adicionar_membro_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f'Esse membro {membro} já está na equipe!')

    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f'O membro {membro} não está na equipe!')

class Videos:
    def __init__(self,titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.visualizacoes = 0
        self.deslikes = 0
        self.likes = 0
        self.comentarios = []

    def assistir(self):
        self.visualizacoes += 1
    def curtir(self):
        self.likes += 1
    def deslike(self):
        self.deslikes += 1
    def comentar(self, comentario):
        self.comentarios.append(comentario)
    def informacao(self):
        print(f'''
Título: {self.titulo}
Descrição: {self.descricao}
Visualizações: {self.visualizacoes}
Likes: {self.likes}
Deslikes: {self.deslikes}
Comentários: {self.comentarios}\n''')

canal_matheus = Canal('Matheuszinho', 'Descrição do meu canal é', 10000)
canal_guanabara = Canal('Curso em vídeo', 'Paixão por ensinar', 250000)
canal_netflix = CanalEmpresarial('Netflix','Filmes/Séries',500000)
#canal_netflix.adicionar_membro_equipe('Matheus')
#canal_netflix.adicionar_membro_equipe('Lucas')
#canal_netflix.adicionar_membro_equipe('Lucas')
#canal_netflix.remover_membro_equipe('Vinicius')
#print(f'Membros atuais: {canal_netflix.equipe}')
video_poo = Videos('Python Objetos', 'Aprenda POO')
video_poo.assistir()
video_poo.informacao()
