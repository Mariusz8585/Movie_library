import random

class MovieLibrary:

    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " (" + str(self.year) + ")"


class SeriesLibrary:
    def __init__(self, title, year, genre, plays, episode, season):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays
        self.episode = episode
        self.season = season

    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " S" + str(self.season) + "E" + str(self.episode)

class Library:
    def __init__(self,lista):
        self.lista = lista

    def get_movies(self):
        lista = []
        for item in self.lista:
            if type(item) == MovieLibrary:
                lista.append(item)
        return sorted(lista, key=lambda item: item.title)


    def get_series(self):
        lista = []
        for item in self.lista:
            if type(item) == SeriesLibrary:
                lista.append(item)
        return sorted(lista, key=lambda item: item.title)

    def search(self, title):
        lista = []
        for item in self.lista:
            if title in item.title:
                lista.append(item)
        return lista

    def generate_views(self):
        i = random.randint(0,len(self.lista)-1)
        for _ in range(random.randint(1, 100)):
            self.lista[i].play()

    def generate(self):
        for _ in range(10):
            self.generate_views()

    def top_titles(self):
        return sorted(self.lista, key=lambda item: item.plays)[:10]
