from enum import Enum

# Токент бота
TOKEN = '5889577871:AAEQXcaoSqW-g4dVb95mzD-eUno4fuAy8wI'

# Файл базы данных Vedis
db_file = 'db.vdb'

# Ключ записи в БД для текущего состояния
CURRENT_STATE = 'CURRENT_STATE'

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_FIRST_NUM = "STATE_FIRST_NUM"
    STATE_SECOND_NUM = "STATE_SECOND_NUM"
    STATE_COUNTING = 'STATE_COUNTING'