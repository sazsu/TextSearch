import os.path


def ispresent(path_to_file: str) -> bool:
    return os.path.isfile(path_to_file)


def count_appearance(path_to_file: str, word=None, letter_case=None, *args, **kwargs) -> str:
    if not ispresent(path_to_file):
        return 'такого файла не существует'
    
    with open(path_to_file, 'r', encoding='utf-8') as f:
        match letter_case:  # проверяем доп аргумент для регистра
            case None:
                appearance_cnt = f.read().count(word)
            case '-u':  # верхний регистр
                appearance_cnt = f.read().upper().count(word)
            case '-l':  # нижний регистр
                appearance_cnt = f.read().lower().count(word)
            case _:
                appearance_cnt = 'неверный аргумент letter_case'
    
    return appearance_cnt if appearance_cnt != 0 else 'не встретилось'