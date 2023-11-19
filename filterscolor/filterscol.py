from PIL import Image, ImageFilter
import os


class RedFilter():

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                r = min(255, int(r * 8))
                img.putpixel((x, y), (r, g, b))
        return img

class InverseFilter():

    def apply_to_image_2(self, img: Image.Image) -> Image.Image:
        img = img.convert("L")
        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))
                new_pixel = 255 - pixel
                img.putpixel((x, y), new_pixel)
        return img


class EdgesFilter():

    def apply_to_image_1(self, img: Image.Image) -> Image.Image:
        img = img.filter(ImageFilter.FIND_EDGES)
        img = img.convert("L")
        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                new_pixel = 255 - pixel
                img.putpixel((x, y), new_pixel)
        return img


filter_name = [
    "Красный фильтр.",
    "Контурный фильтр.",
    "Чёрно-белая инверсия",
    "Выход",

]

filter_description = {
    "Красный фильтр.": "Делает изображение более красным.",
    "Контурный фильтр.": "Обесцвечивает всё изображение, кроме контура.",
    "Чёрно-белая инверсия": "Инвертирует изображение"}

filters = [
    RedFilter(),
    EdgesFilter(),
    InverseFilter(),
]
print("Добро пожаловать в консольный фоторедактор.")

is_finished = False
while not is_finished:

    path = input("Введите путь к файлу: ")

    while not os.path.exists(path):
        path = input("Файл не найден. Попробуйте ещё раз: ")

    img = Image.open(path).convert("RGB")

    print("Меню фильтров:")
    for i in range(len(filter_name)):
        print(f"{i + 1} - {filter_name[i]}")

    choice = input("Выберите фильтр (введите номер): ")

    while int(choice) <= 0 or int(choice) >= len(filter_name) + 1:
        answer = input("Некорректный ввод. Попробуйте ещё раз: ")

    if choice == "1" or choice == "2" or choice == "3":
        print(filter_description[filter_name[int(choice) - 1]])

        question = input("Применить фильтр к картинке? (Да/Нет) ")

        while question.lower() != "да" and question.lower() != "нет":
            question = input("Некорректный ввод. Попробуйте ещё раз: ")

        if question.lower() == "да":
            filt = filters[int(choice) - 1]
            if isinstance(filt, EdgesFilter):
                img = filt.apply_to_image_1(img)
            elif isinstance(filt, RedFilter):
                img = filt.apply_to_image(img)
            else:
                img = filt.apply_to_image_2(img)

            sav_path = input("Куда сохранить: ")

            img.save(sav_path)

            answer = input("Ещё раз? (Да/Нет): ")

            while answer.lower() != "да" and answer.lower() != "нет":
                answer = input("Некорректный ввод. Попробуйте ещё раз: ")

            if answer.lower() == "нет":
                is_finished = True


    elif choice == "4":
        print("До свидания!")
        is_finished = True

    else:
        print("Команда введена некорректно. Попробуйте заново.")
