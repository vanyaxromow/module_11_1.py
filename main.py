import requests
from PIL import Image
import matplotlib.pyplot as plt


def get_image(x: str):  # ф-ция принимает url-адрес картинки и сохраняет ее в файл image.png
    response = requests.get(x)  # отправляем get-запрос
    with open('image.jpeg', 'wb') as file:  # используем флаг wb
        file.write(response.content)  # сохраняем данные с помощью атрибута content


def resize_image():  # ф-ция изменяем размер ранее сохраненной картинки
    image_path = './image.jpeg'  # указываем путь картинки - текущая директория
    img = Image.open(image_path)  # открываем картинку
    new_image = img.resize((800, 600))  # меняем размер
    new_image.save('new_image.jpeg')  # сохраняем измененную картинку


def reformat_image():  # ф-ция создает черно-белое изображение и сохраняет в формете png
    image_path = './new_image.jpeg'  # указываем путь в текущей директории
    image = Image.open(image_path)  # открываем изображение
    grayscale = image.convert('L')  # конвертируем в черно-белое
    grayscale.show()  # выводим на экран
    grayscale.save('gray_image.png')  # сохраняем в png


def get_up_population(x, y):  # ф-ция выводи график распределения численности населения
    # земли с использованием библиотеки matplotlib
    plt.pie(x, labels=y, autopct='%1.1f%%')
    plt.title("Распределение численности населения по материкам")  # указываем заголовок
    plt.show()


vals = [4_778_004_486, 1_480_770_525, 745_602_875, 658_891_517, 382_902_742, 45_562_787]
labels = ["Азия", "Африка", "Европа", "Латинская Америка", "Северная Америка",
          'Океания']

# get_image(input('Введите url-адрес картинки: ')) # ф-ция сохраняет изображение из ссылки
# resize_image() # ф-ция меняет размер изображения
# reformat_image() # ф-ция меняет формат
# get_up_popuation(vals, labels)  # ф-ция выводит график на экран
