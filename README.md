 
**Итоговый проект модуля "Бэкенд разработка на Django"**
  
BoardProject — это веб-приложение на Django для размещения объявлений и взаимодействия пользователей через систему откликов.  

**Основной функционал**:  
• Регистрация по email с подтверждающим кодом  
• Создание и редактирование объявлений зарегистрированными пользователями  
• Объявления состоят из заголовка, текста и дополнительного контента (реализовано через CKEditor 5)  
• Функционал откликов, позволяющий пользователям оставлять отзывы на объявления  
• Выбор категории при создании объявления (по умолчанию одна, но можно легко изменить на множественный выбор)  
• Рассылка новостей по почте через Django Signals  

**Дополнительные возможности**:  
• Личный кабинет с расширенными возможностями (аватарка, биография, удаление аккаунта)  
• Автор объявления может редактировать и удалять его 
• Новости: страница со всеми новостями и отдельной новостью (создает только админ через Django Admin)  
• Связь с поддержкой через Google-форму  
• Сброс пароля по ссылке  
• Профиль пользователя с информацией о нем и его объявлениях  
• Локализация времени 
• Статические страницы с сообщениями (например, успешная отправка письма)  

Особенности и комментарии  
• Проблемы с рассылкой писем: иногда возникает ошибка `smtplib.SMTPServerDisconnected`. Для тестирования рекомендуется использовать свои SMTP-данные. Функционал почтовой рассылки работает корректно только с VPN. Конфигурация SMTP хранится в файле формата .env.

• AJAX-запросы для работы с откликами: реализованы для обработки принятия/отклонения откликов без перезагрузки страницы.  
 
 **Технологии**  
• Backend: Django, Django ORM, Django Signals  
• Frontend: Bootstrap, CKEditor 5, JavaScript (AJAX)  
• База данных: PostgreSQL / SQLite  
• Аутентификация: Django Authentication  
• Отправка email: `smtplib`, `django.core.mail`  

**Установка и запуск**  
Клонирование репозитория  
git clone https://github.com/your-username/BoardProject.git
cd BoardProject

Создание виртуального окружения и установка зависимостей  
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt

Настройка переменных окружения  
Создайте файл `.env` в корневой папке и добавьте в него SMTP-настройки и параметры базы данных:  
EMAIL_HOST_USER='почта для рассылки'
EMAIL_HOST_PASSWORD='пароль от почтового клиента'****

Применение миграций и запуск сервера  
python manage.py migrate
python manage.py createsuperuser  # Создание суперпользователя
python manage.py runserver

Приложение будет доступно по адресу: **http://127.0.0.1:8000/**

Контакты: **vihalfblood@gmail.com**


