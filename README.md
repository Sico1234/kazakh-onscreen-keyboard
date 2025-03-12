# Kazakh On-Screen Keyboard 🇰🇿

Виртуальная клавиатура для казахских букв. Простое и удобное приложение для Windows. Позволяет печатать казахские символы ә, і, ң, ғ, ү, ұ, қ, ө, һ прямо с экрана.

## ⚙️ Функционал

✅ Ввод казахских букв  
✅ Переключение регистра: Shift и Caps Lock  
✅ Кнопки Backspace и Enter  
✅ Легкий и удобный интерфейс  
✅ Работает поверх всех окон  
✅ Быстрая сборка в .exe файл для Windows  

## 🖥️ Как запустить на Windows

1. Установить Python 3.x с сайта: https://www.python.org/downloads/  
2. Скачать код из этого репозитория или клонировать:
   ```bash
   git clone https://github.com/ТВОЙ_НИК/kazakh-onscreen-keyboard.git
   ```
3. Установить зависимости:
   ```bash
   pip install pyautogui
   ```
4. Запустить приложение:
   ```bash
   python kazakh_keyboard.py
   ```

## 🛠️ Как собрать .exe для Windows

1. Установить pyinstaller:
   ```bash
   pip install pyinstaller
   ```
2. Выполнить сборку:
   ```bash
   pyinstaller --onefile --noconsole kazakh_keyboard.py
   ```
3. Готовый .exe файл будет находиться в папке dist

## 📦 Структура проекта

```
kazakh-onscreen-keyboard/
├── kazakh_keyboard.py
├── README.md
├── LICENSE
└── .gitignore
```

## 📋 Лицензия

Проект распространяется под MIT License.  
Можешь свободно использовать, копировать и распространять этот код в своих целях.  

Автор: Серикбай  
Год: 2025

## 🚀 Планы по улучшению

- Добавить выбор темы (тёмная / светлая)  
- Возможность закреплять окно поверх всех окон  
- Настройка размеров кнопок  
- Добавить дополнительные символы и раскладки  

## 🔗 Полезные ссылки

- Python для Windows: https://www.python.org/downloads/windows/  
- PyInstaller: https://pyinstaller.org/en/stable/  

