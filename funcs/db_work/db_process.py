import sqlite3
import re

# Создаём db
def create_bd(DB_NAME):
        with sqlite3.connect(DB_NAME) as sql_connection:
            # Создали бд-запрос на создание таблицы courses сост. из 4-ёх колонок
            sql_request = """CREATE TABLE Words (
            ID INT PRIMARY KEY,
            Word VARCHAR(255) NOT NULL,
            Translation VARCHAR(255) NOT NULL,
            Used BOOLEAN DEFAULT FALSE
            );"""
            # Выполняем этот(sql_request) созданный запрос
            sql_connection.execute(sql_request)

# Separate db
my_dict = {}
def separate_data(my_dict):
    with open ('words.txt', 'r', encoding='utf-8') as data:

        for line in data:

            separated_line = re.split(' — |-|_| ', line.strip())
            bel = separated_line[0]
            rus = separated_line[-1]

            my_dict[rus] = bel

            
    keys_dict = my_dict.keys()
    values_dict = my_dict.values()
    return (keys_dict, values_dict)

# Fill db
def fill_bd(DB_NAME, key_val):
    with sqlite3.connect(DB_NAME) as sql_connection:

        sql_request = "INSERT INTO Words VALUES(?, ?, ?, ?)"
        word_id = 0
        for a,b in zip(key_val[0], key_val[1]):
            sql_connection.execute(sql_request, (word_id, a, b, False))
            word_id += 1

        # Комитим изменения
        sql_connection.commit()


# Read db
def readDbWords(DB_NAME, TABLE_NAME='Words', COLUMN_NAME='Used', VAL=1):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE {COLUMN_NAME} IS NOT 1 ORDER BY RANDOM() LIMIT 1")
            row = cursor.fetchone()
            if row:
                id = row[0]  # assuming 'id' is the first column
                cursor.execute(f"UPDATE {TABLE_NAME} SET {COLUMN_NAME} = ? WHERE id = ?", (VAL, id))
                conn.commit()
                return row
            else:
                return False
            
        
    except Exception as e:
        print(f'f"An error occurred when func "readDbWords" was: {e}')

    finally:
        conn.close()


def readDbAuthors(DB_NAME, TABLE_NAME, onePoleReadingMode=0):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Если onePoleReadingMode не равно 0, получаем данные только для этого id
        if onePoleReadingMode != 0:
            cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id=?", (onePoleReadingMode,))
            row = cursor.fetchone()
            return list(row[1:])  # возвращаем все данные из этого поля, кроме id

        # Иначе получаем все данные из таблицы
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cursor.fetchall()

        # Создаем словарь, где ключ - первое поле, а значение - список из остальных полей
        data_dict = {}
        for row in rows:
            key = row[0]
            values = list(row[1:])
            data_dict[key] = values

        return data_dict

    except Exception as e:
        print(f'An error occurred when func "readDbAuthors" was: {e}')

    finally:
        conn.close()




            