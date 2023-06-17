# Практическая работа 16. Логирование и профилирование

# Практика 

## Видео 1. Зачем нужно логирование

## Видео 2. Логирование в Django

- [Logging | Django documentation](https://docs.djangoproject.com/en/4.2/topics/logging/)
    
- [Logging HOWTO — Python 3.11.3 documentation](https://docs.python.org/3/howto/logging.html)
    

## Видео 3. Зачем нужно профилирование

- [Optimize your code using profilers | PyCharm Documentation](https://www.jetbrains.com/help/pycharm/profiler.html)
    
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
    

## Видео 4. Docker

- [Docker](https://www.docker.com/)
    
- [Docker Hub](https://hub.docker.com/)
    

## Видео 5. Логи в Grafana Loki

- [Grafana | Query, visualize, alerting observability platform](https://grafana.com/grafana/)
    
- [Grafana Loki OSS | Log aggregation system](https://grafana.com/oss/loki/)
    
- [https://github.com/grafana/loki/tree/main/production](https://github.com/grafana/loki/tree/main/production)
    

## Видео 6. Sentry

- [Sentry](https://sentry.io/)
    
- [Django | Sentry Documentation](https://docs.sentry.io/platforms/python/guides/django/)
    

  

Практическая работа

# Цель практической работы

Научиться интегрировать Django Debug Toolbar, собирать приложение в Docker, подключать приложение к Sentry.

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория с практической работой.

  

- В файле settings.py объявите настройки для логирования в консоль:
    

- укажите формат;
    
- укажите обработчик.
    

- Установите [Installation — Django Debug Toolbar 4.0.0 documentation](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html).
    
- Соберите приложение в Docker-образ, зависимости должны быть установлены до копирования всех файлов проекта внутрь образа.
    
- Подготовьте docker compose файл, в нём:
    

- объявите секцию build и пропишите Dockerfile для сборки;
    
- укажите команду для запуска приложения;
    
- выполните проброс портов.
    

- Настройте сбор логов из Docker-контейнера в Grafana Loki:
    

- установите Docker driver для Grafana Loki: [Docker driver | Grafana Loki documentation](https://grafana.com/docs/loki/latest/clients/docker-driver/);
    
- объявите сервисы Grafana и Loki в docker compose;
    
- подключите драйвер Loki в logging для сервиса вашего приложения;
    
- настройте подключение Loki к Grafana через веб-интерфейс и убедитесь, что логи приложения можно посмотреть через Grafana.
    

- Установите пакет Sentry SDK [Django | Sentry Documentation](https://docs.sentry.io/platforms/python/guides/django/) и подключите в настройках приложения.
    

# Что оценивается

- В файле settings.py объявлен LOGGING, там указаны:
    

- настройки форматирования;
    
- параметры обработки.
    

- Инструмент Django Debug Toolbar установлен:
    

- добавлен в INSTALLED_APPS;
    
- Middleware 'debug_toolbar.middleware.DebugToolbarMiddleware' добавлен в список MIDDLEWARE;
    
- добавлен адрес '__debug__/' в urls;
    
- объявлен список INTERNAL_IPS.
    

- Приложение собрано в Docker-образ:
    

- зависимости устанавливаются до копирования файлов приложения;
    
- в список INTERNAL_IPS добавлен внутренний адрес для Docker-сети.
    

- Сервисы Grafana и Loki объявлены в docker compose.
    
- Логи для сервиса приложения собираются через драйвер Loki.
    
- Установлены зависимости для Sentry SDK и выполнена инициализация в файле settings.py.
    

# Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.
