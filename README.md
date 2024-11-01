Этот скрипт предназначен для чтения текстового файла, содержащего информацию об автомобилях, структурирования данных и сохранения их в CSV файл.

Используемые библиотеки
csv: стандартная библиотека Python для работы с CSV файлами.


Пошаговое описание
Импорт библиотеки csv:

import csv
Импортируем библиотеку csv, чтобы работать с CSV файлами.

Создание пустого списка для хранения информации об автомобилях:
car_info = []

Чтение данных из текстового файла:
with open("data.txt", encoding='utf-8') as file:
    data = file.read()

Открываем файл data.txt в режиме чтения с кодировкой utf-8 и читаем его содержимое в переменную data.

Разделение текста на строки:
lines = data.split('\n')
Разделяем текст на строки с помощью функции split('\n'), чтобы затем обработать каждую строку отдельно.

Обработка каждой строки и извлечение данных:
for line in lines...

Каждая строка разбивается на части.

Извлекается статус машины (Sold или On sale).

Определяются марка (make), модель (model) и год выпуска (year).

Проверяется наличие URL и, если он найден, извлекается.

Определяются цена (price) и дата (date).

Все данные о машине добавляются в список car_info.

Запись данных в CSV файл:

with open("cars.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Status", "Make", "Model", "Year", "Price", "Date", "Url/if exists"])

    for item in car_info:
        writer.writerow([item["status"], item["make"], item["model"], item["year"], item["price"], item["date"], item["url"]])
Открывается CSV файл cars.csv в режиме записи.

Записывается строка заголовков.

Записываются строки данных из списка car_info.

Пример входных данных
Файл data.txt:

⛔️ peugeot 406 1997.,  3499$ : 2024-10-05
⛔️ nissan almera tino 2001.,  4999$ : 2024-10-04
✅ renault megane 2019 (https://cars.av.by/renault/megane/111222888)., 15399$ : 2024-10-04
⛔️ mazda 6 2005.,  5499$ : 2024-10-03
Выходные данные
Файл cars.csv (CSV, разделенный точкой с запятой):

Status;Make;Model;Year;Price;Date;Url/if exists
Sold;peugeot;406;1997;3499;2024-10-05;no url
Sold;nissan;almera tino;2001;4999;2024-10-04;no url
On sale;renault;megane;2019;15399;2024-10-04;https://cars.av.by/renault/megane/111222888
Sold;mazda;6;2005;5499;2024-10-03;no url
Этот скрипт позволяет структурировать и сохранить данные об автомобилях в удобном для анализа формате CSV.
