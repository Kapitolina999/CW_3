import json


class Bookmark:
    def __init__(self, path: str):
        """
        :param path: путь до json файла
        """
        self.path = path

    def load_bookmarks(self):
        """
        Загружает данные из json файла
        """
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def get_all_bookmarks(self):
        """
        :return: все закладки
        """
        bookmarks = self.load_bookmarks()
        return bookmarks

    def add_bookmark(self, post):
        """
        Добавляет пост в закладки
        """
        bookmarks = self.load_bookmarks()
        for i in bookmarks:
            if post['pk'] == i['pk']:
                raise ValueError("Пост уже добавлен")

        bookmarks.append(post)
        with open(self.path, 'w', encoding='UTF-8') as file:
            json.dump(bookmarks, file, indent=4, ensure_ascii=False)

    def remove_bookmark(self, pk: int):
        """
        Удаляет пост
        """
        bookmarks = self.load_bookmarks()
        data = list(filter(lambda x: x['pk'] != pk, bookmarks))
        with open(self.path, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
