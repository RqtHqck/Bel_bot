from funcs.db_work.db_process import readDbWords
from data import config

def takeWord():
    field_tuple = readDbWords(config.DB_NAME_WORDS)
    rus = field_tuple[1]
    bel = field_tuple[2]
    translator = [rus, bel]
    return translator