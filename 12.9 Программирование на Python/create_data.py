import random
from datetime import datetime, timedelta

products = ["яблоки", "груши", "сливы", "печенье", "конфеты Рот-Фронт"]
dates = [datetime(2024, 6, 16) + timedelta(days=i) for i in range(10)]

data = []
for _ in range(50):
    product = random.choice(products)
    amount1 = random.randint(5, 25)
    amount2 = random.randint(10, 30)
    date = random.choice(dates).strftime("%Y-%m-%d")
    data.append(f"{product}, {amount1}, {amount2}, {date}")

# Запись данных в текстовый файл
with open("data.txt", "w", encoding="utf-8") as file:
    for entry in data:
        file.write(entry + "\n")

print("Данные успешно записаны в файл data.txt")
