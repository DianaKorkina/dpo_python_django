# Практическая работа 17. Экспорт и импорт данных

# Практика 

## Видео 1. Форматы данных XML, JSON, YAML

- [JSON — Wikipedia](https://en.wikipedia.org/wiki/JSON)
    
- [Введение в REST API — RESTful веб-сервисы](https://habr.com/ru/articles/483202/) 
    
- [XML — Wikipedia](https://en.wikipedia.org/wiki/XML)
    
- [Различия REST и SOAP / Хабр](https://habr.com/ru/articles/483204/)
    
- [YAML.org](https://yaml.org/)
    
- [YAML — Википедия](https://ru.wikipedia.org/wiki/YAML)
    

## Видео 2. Импорт данных

- [Fixtures | Django documentation](https://docs.djangoproject.com/en/4.2/topics/db/fixtures/)
    
- [CSV File Reading and Writing — Python 3.11.3 documentation](https://docs.python.org/3/library/csv.html)
    
- [Модуль CSV — чтение и запись CSV-файлов | Python 3 для начинающих и чайников](https://pythonworld.ru/moduli/modul-csv.html)
    
- [Many-to-many relationships | Django documentation](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/)
    

## Видео 3. Файлы в DRF

- [Viewsets — Django REST framework](https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)
    
- [TextIOWrapper | io — Core tools for working with streams — Python 3.11.3 documentation](https://docs.python.org/3/library/io.html#io.TextIOWrapper)
    

## Видео 4. Лента новостей

- [RSS — Википедия](https://ru.wikipedia.org/wiki/RSS)
    
- [The syndication feed framework | Django documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/syndication/)
    

## Видео 5. Карта сайта

- [Site map — Wikipedia](https://en.wikipedia.org/wiki/Site_map)
    
- [The sitemap framework | Django documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/)
    

  

Практическая работа

# Цель практической работы

Реализовать в проекте RSS, sitemap, а также интегрировать в Django-админку новые кнопки и добавить поддержку импорта файлов.

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория практической работы.

  

- Объявите метод get_absolute_url в модели Product.
    
- Создайте sitemap в проекте:
    

- объявите новый класс ShopSitemap в приложении shopapp;
    
- добавьте /sitemap.xml в urlpatterns в корневом файле urls.py;
    
- в настройках в INSTALLED_APPS добавьте приложение 'django.contrib.sitemaps'.
    

- В shopapp.views объявите новый класс LatestProductsFeed:
    

- подключите его к адресу products/latest/feed/.
    

- Сделайте импорт информации по заказам из файла (CSV, JSON, XML на выбор) через админку:
    

- объявите шаблон с формой для загрузки файла, например admin/csv_form.html;
    
- объявите шаблон для добавления кнопки на страницу в админке для перехода к странице для загрузки файла для импорта заказов, например shopapp/orders_changelist.html;
    
- объявите класс формы для загрузки файла в shopapp/forms.py;
    
- укажите новый шаблон в админке в классе OrderAdmin в shopapp/admin.py;
    
- объявите метод import_csv на классе OrderAdmin:
    

- для обработки запросов на получение страницы для загрузки файла — верните шаблон с формой;
    
- обработки запроса с передачей файла с данными для импорта. Прочитайте файл и создайте новые заказы, привяжите товары к заказам. Перенаправьте пользователя обратно к списку;
    

- переопределите метод get_urls, добавьте к urls новый адрес, укажите ранее объявленную view-функцию, добавьте имя для url.
    

# Что оценивается

- Метод get_absolute_url объявлен на модели Product.
    
- В проекте добавлен sitemap:
    

- в настройках в INSTALLED_APPS добавлено приложение 'django.contrib.sitemaps';
    
- доступен по адресу /sitemap.xml;
    
- содержит информацию о доступных статьях.
    

- Объявлен класс LatestProductsFeed:
    

- подключён к адресу products/latest/feed/.
    

- Сделан импорт информации по заказам из файла (CSV, JSON, XML на выбор) через админку:
    

- объявлен шаблон с формой для загрузки файла, например admin/csv_form.html;
    
- объявлен шаблон для добавления кнопки на страницу в админке для перехода к странице для загрузки файла для импорта заказов, например shopapp/orders_changelist.html;
    
- объявлен класс формы для загрузки файла в shopapp/forms.py, на классе есть поле типа FileField;
    
- указан новый шаблон в админке в классе OrderAdmin в shopapp/admin.py, в поле change_list_template;
    
- объявлен метод import_csv на классе OrderAdmin:
    

- для обработки запросов на получение страницы для загрузки файла — оттуда должен возвращаться шаблон с формой для загрузки файла;
    
- обработки запроса с передачей файла с данными для импорта. Прочитан файл, созданы новые заказы, товары привязаны к заказам. После этого пользователь перенаправляется на уровень выше;
    

- объявлен метод get_urls, к urls добавлен новый адрес (на ранее объявленную view функцию), указано имя для url.
    

# Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.
