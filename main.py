#Импортим
from logger import square, hello, max_2
from Steam import SteamStats

def main():
    print(f"Квадрат числа 100: {square(100)}")
    print(f"Привет: {hello('Даник')}")
    print(f"Наибольшее из чисел 33 и 69: {max_2(33, 69)}")
    print("Логи записаны в соответствующие файлы")
    print("Нарисуем статистику STEAM...")

    SteamStats('steam_players.csv').show_stats()

if __name__ == "__main__":
    main()

