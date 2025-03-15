# Выполнить запрос и получить текущие координаты МКС и состав экипажа
# вывести результаты в понятном для человека виде
# сайт с информацией http://api.open-notify.org

import requests 


url = 'http://api.open-notify.org/iss-now.json'
data = requests.get(url)
dt = data.json()
print(dt['iss_position']['longitude'])
print(dt['iss_position']['latitude'])
url = 'http://api.open-notify.org/astros.json'
data = requests.get(url)
dt = data#.json()['people']
# names = [n['name'] for n in dt ]
# print(len(names))
# for name in names:
#     print(name)


