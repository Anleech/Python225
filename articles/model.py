class Article:
    def __init__(self, title, autor, pages, discription):
        self.tilte = title
        self.autor = autor
        self.pages = pages
        self.discription = discription

    def __str__(self):
        return f"{self.tilte}({self.autor})"

class ArticleModel:
    def __init__(self):
        self.articles = {}


    def get_all_articles(self):
        return self.articles.values()


    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.tilte] = article

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.tilte,
            "автор": article.autor,
            "количество знаков": article.pages,
            "описание": article.discription
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

