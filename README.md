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
Обязательные переменные:
- `NASA_TOKEN` - токен выглядит например: `N0bFH5PNh4cx6Dc7RBssCDJf7Z6Jgi1KCacg8792`. См. документацию https://api.nasa.gov/
- `TELEGRAM_TOKEN` - токен выглядит например: `958423683:AAEAtJ5Lde5YYfkjergber`. См. документацию https://core.telegram.org/bots/faq#how-do-i-create-a-bot
- `TELEGRAM_CHAT_ID` - выглядит например: `-1001901234567` См. https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

Необязательные переменные:
- `TELEGRAM_PUBLICATION_DELAY` - задержка между публикацией постов, указывается в секундах тип данных `int`. Значение по умолчанию 14400.
- `NASA_IMAGES_COUNT` указывается количество скачиваемых фото NASA, тип данных `int`. Значение по умолчанию 30.
- `NASA_EPIC_IMAGES_COUNT` указывается количество скачиваемых фото NASA EPIC, тип данных `int`. Значение по умолчанию 10.


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Применение
Скрипты работают из консольной утилиты.

Для запуска скриптов: ``` fetch_epic_nasa_image.py, fetch_nasa_image.py```:

```
\publishing_space_in_telegram> python fetch_epic_nasa_image.py
\publishing_space_in_telegram> python fetch_nasa_image.py
```
Для запуска скрипта 
``` fetch_spacex_images.py```: отправьте параметры `-h` помощь.

```
\publishing_space_in_telegram> python fetch_spacex_images.py -h
usage: fetch_spacex_images.py [-h] [id_launch]

Введите ID запуска, например 61eefaa89eb1064137a1bd73

positional arguments:
  id_launch   ID запуска

options:
  -h, --help  show this help message and exit

```

Для запуска скрипта ``` publish_all_images_with_a_delay.py```, публикуемые изображения берутся из папки images:
```
.
└── publish_all_images_with_a_delay.py
└── images
```
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
Для запуска скрипта ``` posts_an_image.py```, публикуемое изображение берётся из папки images:
```
.
└── posts_an_image.py
└── images
```
``` posts_an_image.py```: отправьте параметры `-h` помощь.
```
\publishing_space_in_telegram>python posts_an_image.py -h

usage: posts_an_image.py [-h] [images_file_name]

Введите имя файла изображения из папки images

positional arguments:
  images_file_name  Имя файла картинки

options:
  -h, --help        show this help message and exit
```
### Цель проекта



Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).