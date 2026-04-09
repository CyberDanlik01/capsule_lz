#ВАРИАНТ - 1
#Импортим библиотеки
import pandas as pd
import matplotlib.pyplot as plt

class SteamStats:
    
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

        #Рисуем график:
    def show_stats(self):
        stats = self.df.dropna(subset=['country'])['country'].value_counts().head(4) / 10000 
        stats.plot(kind='bar', figsize=(8, 4), color='Red')
        plt.title('Количество игроков STEAM')
        plt.xlabel('Страна')
        plt.ylabel('Количество человек (в сотнях тысяч)')
        plt.xticks(rotation=0) 
        plt.tight_layout()
        plt.show()
