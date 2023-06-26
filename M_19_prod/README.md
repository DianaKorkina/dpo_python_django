# Практическая работа 19. Деплой и командная разработка

# Практика

## Видео 1. Развёртывание сайта на сервере

- «[Разница между VPS-хостингом и облачным хостингом. Какой выбрать?](https://oblakoteka.ru/about/v_mire_it/raznica-mezhdu-vpshostingom-i-oblachnym/)»
    

## Видео 2. Подготовка Python-проекта к развёртыванию

  

В настройках используйте DJANGO_DEBUG=1 вместо DJANGO_DEBUG=0, чтобы избежать проблем со статикой.

- «[Анализ производительности WSGI-серверов](https://habr.com/ru/articles/428047/)»
    
- [Ways to set environment variables in Compose. Docker Documentation](https://docs.docker.com/compose/environment-variables/set-environment-variables/)
    
- [Start containers automatically. Docker Documentation](https://docs.docker.com/config/containers/start-containers-automatically/)
    
- [Logging. Django documentation](https://docs.djangoproject.com/en/4.2/topics/logging/)
    
- [What is .env? How to Set up and run a .env file in Node? Codementor](https://www.codementor.io/@parthibakumarmurugesan/what-is-env-how-to-set-up-and-run-a-env-file-in-node-1pnyxw9yxj)
    
- [OpenSSL rand](https://www.openssl.org/docs/man1.1.1/man1/rand.html)
    

  

## Видео 3. Совместимость кода и миграций при командной разработке

- [Git merge conflicts. Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
    
- [Django Migrations and How to Manage Conflicts](https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/)
    
- «[Постановка проблемы обратной совместимости](https://habr.com/ru/articles/534238/)»
    

## Видео 4. Контроль зависимостей

- [Pipenv](https://pipenv.pypa.io/en/latest/)
    
- [Poetry](https://python-poetry.org/)
    
- [Integrating Python Poetry with Docker](https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker)
    
- [Document docker poetry best practices](https://github.com/orgs/python-poetry/discussions/1879)
    
- «[Стенд для нагрузочного тестирования: от DEV до PROD](https://habr.com/ru/companies/rtlabs/articles/577580/)»
    

  
  

# Цели практической работы

- Научиться работать с SSH.
    
- Опубликовать проект приложения.
    

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория c практической работой.

  

- Примените Pipenv или Poetry для управления зависимостями в проекте.
    
- Соберите Docker-образ с приложением. Установите зависимости с помощью инструмента для их контроля. Убедитесь, что внутри Docker-образа система контроля зависимостей не создаёт новое виртуальное окружение (Docker-образ сам по себе виртуальное окружение — не в Python-понимании, но по общему принципу).
    
- Настройте использование SSH.
    
- Опубликуйте код приложения в удобном репозитории. Хорошим вариантом будет GitHub, так как там обычно хранят проекты и портфолио.
    
- Настройте виртуальную машину для публикации (например, на Timeweb - инструкцию вы найдете ниже).
    
- Опубликуйте приложение на виртуальной машине при помощи Docker и Docker Compose, укажите политику restart: always, чтобы при неожиданном падении приложение перезапустилось автоматически.
    
- Чтобы статика работала, запустите приложение с флагом DJANGO_DEBUG=1. Хоть это и запуск в production, но без этого статику нужно настраивать отдельно.
    

# Что оценивается

- Применена система контроля зависимостей Pipenv или Poetry.
    
- Приложение собрано в Docker-образ, где зависимости устанавливаются при помощи одного из инструментов контроля, но не создаётся виртуальное окружение (автоматическое создание виртуального окружения нужно отключить в конфигурации инструмента для управления зависимостью).
    
- Код размещён в публичном репозитории.
    
- Приложение запущено на публичном сервере.
    

# Как отправить работу на проверку

В поле ниже напишите «Сделано» и прикрепите ссылку на публичный репозиторий и ссылку на ваше приложение на публичном сервере.
