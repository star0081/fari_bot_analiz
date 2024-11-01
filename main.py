import csv
car_info = []


with open("data.txt", encoding='utf-8') as file:
    data = file.read()


lines = data.split('\n')

for line in lines:
    parts = line.replace('.,', '').split(' ')

    status = parts[0]
    if status == "⛔️":
        status = "Sold"
    else:
        status = ("On sale"
                  "")
    make = parts[1]
    model = parts[2]

    if any(character.isdigit() for character in parts[3]):
        year = parts[3]
    else:
        model = parts[2] + ' ' + parts[3]
        year = parts[4]

    url = 'no url'
    for part in parts:
        if 'http' in part:
            url = part

    for part in parts:
        if '$' in part:
            price = part.replace('💰', '')
        if '-' in part:
            date = part.replace('💰', '')

    if make == 'tesla':
        model = parts[2] + ' ' + parts[3]
        year = parts[4]

    car_info.append({
        "status": status,
        "make": make,
        "model": model,
        "year": year,
        "url": url,
        "price": price,
        "date": date
    })

with open("cars.csv", "w", newline="", encoding=f'UTF-8') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Status", "Make", "Model", "Year", "Price", "Date", "Url/if exists"])
    for item in car_info:
        writer.writerow([item["status"], item["make"], item["model"], item["year"], item["price"], item["date"], item["url"]])
