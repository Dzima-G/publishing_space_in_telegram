# Космический Телеграм

Опубликовывает фото космоса

### Как установить

#### Переменные окружения:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

```
.
├── .env
└── fetch_epic_nasa_image.py
└── fetch_nasa_image.py
└── fetch_spacex_images.py
└── helper_scripts.py
└── posts_an_image.py
└── publish_all_images_with_a_delay.py
```
Необходимы следующие переменные:
- `NASA_TOKEN` - токен выглядит например: `N0bFH5PNh4cx6Dc7RBssCDJf7Z6Jgi1KCacg8792`. См. документацию https://api.nasa.gov/
- `TELEGRAM_TOKEN` - токен выглядит например: `958423683:AAEAtJ5Lde5YYfkjergber`. См. документацию https://core.telegram.org/bots/faq#how-do-i-create-a-bot
- `PUBLICATION_DELAY_TELEGRAM` - задержка между публикацией постов, указывается в секундах тип данных `int`.


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Применение
Скрипты работают из консольной утилиты.

Для запуска скриптов: ``` fetch_epic_nasa_image.py, fetch_nasa_image.py, fetch_spacex_images.py```:

```
\publishing_space_in_telegram> fetch_epic_nasa_image.py
\publishing_space_in_telegram> fetch_nasa_image.py
\publishing_space_in_telegram> fetch_spacex_images.py
```
Для запуска скриптов: 

``` publish_all_images_with_a_delay.py```: отправьте параметры `-h` помощь.

```
\publishing_space_in_telegram> python publish_all_images_with_a_delay.py -h
usage: publish_all_images_with_a_delay.py [-h] [publication_delay]

Введите время задержки между публикациями в секундах:

positional arguments:
  publication_delay  Время задержки между публикациями в секундах

options:
  -h, --help         show this help message and exit  
```

``` posts_an_image.py```: отправьте параметры `-h` помощь.
```
\publishing_space_in_telegram> posts_an_image.py -h

usage: posts_an_image.py [-h] [images_file_name]

Введите название файла изображения

positional arguments:
  images_file_name  Введите название файла картинки из папки images

options:
  -h, --help        show this help message and exit
```
### Цель проекта



Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).