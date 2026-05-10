with open("task3/en-ru.txt","r",encoding="utf-8") as file:
    reader = file.readlines()

    ru_en_dict = {}

    for line in reader:
        line = line.replace("\n","")
        line = line.split(" - ")

        eng = line[0]
        rus = line[1].split(", ")

        for word in rus:
            ru_en_dict.setdefault(word, [])
            ru_en_dict[word].append(eng)

    keys = sorted(ru_en_dict.keys())

with open("task3/ru-en.txt","w",encoding="utf-8") as file:
    for key in keys:
        file.write(f"{key} - {", ".join(ru_en_dict[key])}\n")
