# Автоматизация тестирования Stellar Burgers

Проект автоматизации UI-тестирования веб-приложения **Stellar Burgers** с использованием Selenium WebDriver и pytest.

Тесты запускаются в двух браузерах:

- Google Chrome
- Mozilla Firefox

## Технологии

- Python
- Selenium WebDriver
- pytest
- Allure
- Requests

## Структура проекта

```text
Task_3/
├── api/                    # API-клиенты
├── locators/              # Локаторы элементов страниц
├── pages/                 # Page Object классы
├── tests/                 # Автотесты
├── utils/                 # Вспомогательные модули
├── conftest.py            # Фикстуры pytest
├── pytest.ini             # Конфигурация pytest
├── requirements.txt       # Зависимости проекта
└── Zadanie.txt            # Задание
```

## Установка

Установить зависимости:

`python -m pip install -r requirements.txt`

## Запуск тестов

Запустить все тесты:

`python -m pytest`