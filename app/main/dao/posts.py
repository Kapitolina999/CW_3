import json

from functions import clear_punctuation


class Posts:
    def __init__(self, path):
        """
        :param path: путь до json файла
        """
        self.path = path

    def load_post(self):
        """
        Загружает данные из json файла
        """
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data

    def get_post_all(self):
        """
        :return: все посты
        """
        all_post = self.load_post()
        return all_post

    def get_posts_by_user(self, username: str):
        """
        Возвращает посты пользователя
        :param username: имя пользователя
        :return: list
        """
        all_post = self.load_post()
        return [i for i in all_post if username.lower() == i['poster_name'].lower()]

    def search_for_posts(self, query: str):
        """
        Поиск постов по ключевому слову
        :param query: слово
        :return:
        """
        all_post = self.load_post()
        return [i for i in all_post if query.lower() in clear_punctuation(i['content']).lower().split()]

    def get_post_by_pk(self, pk: int):
        """
        Получение поста по ключу
        """
        all_post = self.load_post()
        for i in all_post:
            if pk == i['pk']:
                return i

    def get_post_by_tag(self, tag: str):
        """
        Получение постов по тегу
        """
        all_post = self.load_post()
        return [i for i in all_post if i['content'].count(f"#{tag}")]
