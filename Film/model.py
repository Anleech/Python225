class Film:
    def __init__(self, title, genre, autor, year, duration, atelier, actors):
        self.tilte = title
        self.autor = autor
        self.year = year
        self.genre = genre
        self.duration = duration
        self.atelier = atelier
        self.actors = actors

    def __str__(self):
        return f"{self.tilte}({self.autor})"

class FilmModel:
    def __init__(self):
        self.articles = {}


    def get_all_articles(self):
        return self.articles.values()


    def add_article(self, dict_article):
        article = Film(*dict_article.values())
        self.articles[article.tilte] = article

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название фильма": article.tilte,
            "жанр": article.genre,
            "режисер": article.autor,
            "год выпуска": article.year,
            "длительность": article.duration,
            "студия": article.atelier,
            "актеры":article.actors
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

