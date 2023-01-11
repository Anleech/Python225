def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap
    return wrapper

class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действие со фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_anwer = input("Выберите вариант действия: ")
        return user_anwer

    @add_title("Добавление фильма")
    def add_user_article(self):
        dict_article ={
            "название фильма": None,
            "жанр": None,
            "режисер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры":None
        }
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} фильма:')
        return dict_article

    @add_title("Каталог фильмов")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}.{article}")

    @add_title("Ввод названия определенного фильма")
    def get_user_article(self):
        user_article = input("Введите название фильма:")
        return user_article

    @add_title("Просмотр определенного фильма: ")
    def show_single_articles(self, article):
        for key in article:
            print(f"{key} фильма - {article[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Статьи с названием {user_title} не существует")

    @add_title("Удаление фильма ")
    def remove_single_articles(self,article):
        print(f"Статья {article} - была удалена")