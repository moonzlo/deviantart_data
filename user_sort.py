# Задача: открыть файл, и посчитать сколько вхождений какой страны есть, собрать данные в виде словаря.



def user_location():
    country = {}
    with open('/home/moonz/PycharmProjects/BeautifulSoup/user_locatin.txt', 'r') as users:

        data = users.readlines()
        for i in data:
            loc = i.replace('\n', '')
            if loc not in country.keys():
                country.update({loc:1})
            else:
                num = int(country.get(loc))
                num += 1
                country.update({loc:num})

        return country


data = user_location()
sort = sorted(data, key=data.get, reverse=True)  # Сортируем по значению.


# Подготоив данные для графика.
data_names = []
data_values = []

for i in sort:
    data_names.append(i)
    data_values.append(data.get(i))

print(data_names)
print(data_values)