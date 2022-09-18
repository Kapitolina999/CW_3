import json


class Comments:
    def __init__(self, path: str):
        """
        :param path: путь до json файла
        """
        self.path = path

    def load_comments(self):
        """
        Функция загрузки данных из comments.json
        """
        with open(self.path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data

    def get_all_comments(self):
        """
        Получение листа со словарями всех комментариев
        """
        comments = self.load_comments()
        return comments

    def get_comments_by_post_id(self, post_id: int):
        """
        Функция получения листа с комментариями по post_id
        """
        all_comments = self.load_comments()
        return list(filter(lambda x: x['post_id'] == post_id, all_comments))

