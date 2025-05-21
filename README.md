# Telegram Courses Bot

Telegram бот для выбора курсов, представленных буквами латинского алфавита.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Niakris1986/zombie_courses_bot.git
cd zombie_courses_bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройка конфигурации:
   - Скопируйте файл `src/config.example.py` в `src/config.py`
   - Откройте `src/config.py` и замените `YOUR_BOT_TOKEN_HERE` на ваш токен бота, полученный от @BotFather

## Запуск

```bash
python bot.py
```

## Использование

1. Найдите бота в Telegram
2. Отправьте команду `/start`
3. Выберите курс из меню

## Функциональность

- Приветствие пользователя
- Отображение меню курсов (A-Z)
- Обработка выбора курса
- Обработка ошибок и логирование

## Структура проекта

```
zombie_courses_bot/
├── src/
│   ├── config.py         # Конфигурация бота (не включен в репозиторий)
│   └── config.example.py # Пример конфигурации
├── bot.py               # Основной код бота
├── requirements.txt     # Зависимости проекта
└── README.md           # Документация
``` 