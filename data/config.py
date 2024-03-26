from environs import Env

# Используем библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
DB_NAME_WORDS = env.str("DB_NAME_WORDS") # Имя DB
DB_NAME_AUTHORS = env.str("DB_NAME_AUTHORS") # Имя DB
