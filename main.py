import os.path


def ispresent(path_to_file: str) -> bool:
    return os.path.isfile(path_to_file)


def count_appearance(path_to_file: str, word=None, *args, **kwargs) -> str:
    if not ispresent(path_to_file):
        return 'такого файла не существует'
    
    with open(path_to_file, 'r', encoding='utf-8') as f:
        appearance_cnt = f.read().count(word)
    
    return appearance_cnt if appearance_cnt else 'не встретилось'