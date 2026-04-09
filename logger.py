#Импортим библиотеки
import os
import pandas as pd
import datetime
import getpass
import uuid

#Пишем логгирование 
def logger(filename="logs.csv", username=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            now = datetime.datetime.now()
            log_data = {
                "id": [str(uuid.uuid4())],
                "pc_username": [username if username else getpass.getuser()],
                "function_name": [func.__name__], 
                "Date": [now.strftime("%d.%m.%Y")],
                "Time": [now.strftime("%H:%M:%S")]
            }
               #Создаём Датафрэйм
            df = pd.DataFrame(log_data)
            write_header = not os.path.isfile(filename)
            df.to_csv(filename, mode='a', index=False, header=write_header)
            return result
        return wrapper
    return decorator

#Функции
@logger(username="Даник")
def square(x):
    return x * x

@logger(username="Андрюха")
def hello(name):
    return f"Привет, {name}!"

@logger(username="Александр Владимирович")
def max_2(a, b):
    return a if a > b else b