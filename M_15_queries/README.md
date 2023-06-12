# Практическая работа 15. Эффективная работа с базой данных в Django

# Практика 

## Видео 1. Эффективное взаимодействие с базой данных

- [Проектирование базы данных. Лучшие практики](https://habr.com/ru/company/otus/blog/471016/).
    
- [Три аспекта оптимизации (БД и ПО)](https://habr.com/ru/post/349910/).
    
- [QuerySet API reference, Django documentation](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#select-related).
    

## Видео 2. Проблема N + 1

- [Проблема выбора N + 1 в объектно-реляционном сопоставлении (ORM)](https://intellect.icu/problema-vybora-n-1-o-v-obektno-relyatsionnogo-sopostavleniya-orm-8653).
    
- [QuerySet API reference, Django documentation](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#select-related).
    

## Видео 3. Транзакции в базах данных

- [Что такое транзакция («Хабр»)](https://habr.com/ru/post/537594/).
    
- [Что такое транзакция базы данных? AppMaster](https://appmaster.io/ru/blog/chto-takoe-tranzaktsiia-bazy-dannykh).
    
- [Database transactions, Django documentation](https://docs.djangoproject.com/en/4.1/topics/db/transactions/).
    

## Видео 4. Приёмы оптимизации скорости и количества запросов

- [QuerySet API reference, Django documentation, values](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#values).
    
- [QuerySet API reference, Django documentation, bulk-create](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create).
    

## Видео 5. Агрегации и аннотации

- [Aggregation, Django documentation](https://docs.djangoproject.com/en/4.1/topics/db/aggregation/).
    
- [Annotation, Django documentation](https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#joins-and-aggregates). 
    
- [Django Annotations: steroids to your Querysets by Gautam Rajeev Singh, Medium](https://medium.com/@singhgautam7/django-annotations-steroids-to-your-querysets-766231f0823a).
    

  

Практическая работа

# Цель практической работы

Научиться создавать интерактивную Swagger-документацию для своего проекта в Django Rest Framework.

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория практической работы.

  

- Создайте новое приложение BlogApp в своём Django-проекте: 
    

- Выполните команду python manage.py startapp blogapp в терминале.
    
- Добавьте приложение в INSTALLED_APPS.
    

- Объявите новые модели в blogapp/models.py:
    
- Модель Author представляет автора статьи. Она имеет два поля:
    

- name — имя автора. Это поле типа CharField, которое может содержать до 100 символов.
    
- bio — биография автора. Это поле типа TextField, которое может содержать текстовую информацию произвольной длины.
    

  

- Модель Category представляет категорию статьи. Она имеет одно поле:
    

- name — название категории. Это поле типа CharField. Укажите ограничение по длине. Например, 40 символов.
    

  

- Модель Tag представляет тэг, который можно назначить статье. Она имеет одно поле:
    

- name — название тэга. Это поле типа CharField. Укажите ограничение по длине. Например, 20 символов.
    

  

- Модель Article представляет статью. Она имеет следующие поля:
    

- title — заголовок статьи. Это поле типа CharField. Укажите ограничение по длине. Например, 200 символов.
    
- content — содержимое статьи. Это поле типа TextField, которое может содержать текстовую информацию произвольной длины.
    
- pub_date — дата публикации статьи. Это поле типа DateTimeField.
    
- author — автор статьи. Это поле типа ForeignKey, которое ссылается на модель Author и указывает, что каждая статья принадлежит одному автору. Параметр on_delete=models.CASCADE означает, что при удалении автора из базы данных все его статьи также будут удалены.
    
- category — категория статьи. Это поле типа ForeignKey, которое ссылается на модель Category и указывает, что каждая статья принадлежит одной категории. Параметр on_delete=models.CASCADE означает, что при удалении категории из базы данных все статьи в этой категории также будут удалены.
    
- tags — тэги статьи. Это поле типа ManyToManyField, которое ссылается на модель Tag и позволяет назначать несколько тэгов для каждой статьи. При использовании этого поля Django автоматически создаст связующую таблицу в базе данных. Связующая таблица будет содержать записи о том, какие тэги назначены для какой статьи.
    

  

- Выполните миграции:
    

- Создайте миграции командой python manage.py makemigrations.
    
- Проверьте миграции.
    
- Примените миграции командой python manage.py migrate.
    

- Создайте Class Based View для отображения списка статей. Воспользуйтесь generic-классом ListView. 
    
- Создайте шаблон blogapp/templates/blogapp/article_list.html и отобразите информацию на странице:
    

- Используйте цикл for, чтобы пройти по списку статей. Для каждой статьи отобразите:
    

- заголовок статьи;
    
- дату публикации;
    
- имя автора, который написал статью;
    
- название категории, к которой относится статья;
    
- список тегов, привязанных к статье.
    

- Оптимизируйте запросы к базе данных. Укажите в queryset-параметры:
    

- Для подгрузки всех связанных сущностей используйте методы select_related и prefetch_related.
    
- Используйте метод defer для исключения из подгрузки неиспользуемых полей, например, поле content.
    

# Что оценивается

- Создано и установлено приложение blogapp.
    
- Созданы модели Author, Category, Tag, Article, выполнены миграции.
    
- Создан ArticlesListView на основе ListView.
    
- Создан шаблон article_list.html, в нём отображены все статьи со всеми связанными сущностями (автор, категория, теги).
    
- Использованы методы select_related и prefetch_related для подгрузки автора статьи, категории, тэгов.
    
- Использован метод defer для исключения из запроса свойств, которые не используются на странице.
    

# Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.
