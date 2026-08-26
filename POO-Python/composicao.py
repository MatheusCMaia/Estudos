class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao =descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists:list[Playlist] = []

    def postar(self, video):
        if video in self.videos:
            print('Esse vídeo já foi postado!')
            return
        self.videos.append(video)

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

    def informacao(self):
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

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.videos:list[Videos] = []

    def adicionar_video(self,video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print(f'Esse vídeo {video} já está na playlist')
    def remover_video(self,video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print(f'Esse vídeo {video} não está na playlist')
    def informacoes_videos(self):
        for video in self.videos:
            video.informacao()

canal_matheus = Canal('Matheuszinho', 'Descrição do meu canal é', 10000)
canal_guanabara = Canal('Curso em vídeo', 'Paixão por ensinar', 250000)
canal_netflix = CanalEmpresarial('Netflix','Filmes/Séries',500000)
#canal_netflix.adicionar_membro_equipe('Matheus')
#canal_netflix.adicionar_membro_equipe('Lucas')
#canal_netflix.adicionar_membro_equipe('Lucas')
#canal_netflix.remover_membro_equipe('Vinicius')
#print(f'Membros atuais: {canal_netflix.equipe}')
video_poo = Videos('Python Objetos', 'Aprenda POO')
video_ensinando = Videos('Ensinando algo', 'Te ensinando alguma coisa')
video_poo.informacao()
video_poo.informacao()
canal_matheus.postar(video_poo)
canal_matheus.postar(video_ensinando)
print(canal_matheus.videos)