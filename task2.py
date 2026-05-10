import json

with open("task2/products.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    try:
        count = int(input("Сколько товаров хотите создать:"))
    except ValueError:
        print("Введите числа")
        exit()

    for i in range(count):
        print("Создайте продукт")
        name = input("Имя:")

        try:
            price = int(input("Цена:"))
            weight = int(input("Вес:"))
        except ValueError:
            print("Введите числа")
            continue

        available = input("Наличие(y/n):")

        available = available.lower() != 'n'

        product = {
            "name": name,
            "price": price,
            "available": available,
            "weight": weight
        }

        data["products"].append(product)

with open("task2/products.json","w",encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)


with open("task2/products.json", "r", encoding="utf-8") as file:
    data = json.load(file)

    for product in data["products"]:
        print(f"Название: {product["name"]}")
        print(f"Цена: {product["price"]}")
        print(f"Вес: {product["weight"]}")
        if product["available"]:
            print("В наличии\n")
        else:
            print("Нет в наличии!\n")