import string


def clear_punctuation(content: str):
    """
    Удаляет знаки препинания в строке
    """
    punctuation = string.punctuation
    for i in punctuation:
        if i in content:
            content = content.replace(i, '')
    return content
