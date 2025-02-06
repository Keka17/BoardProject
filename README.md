# BoardProject
Итоговый проект 20.7 (PJ-03)
Реализован запрашиваемый функционал:
1) Регистрация по email с подтверждающим кодом
2) Зарегестрированный пользователь может создавать/редактировать свои объявления
3) Объявление состоит из заголовка, текста и прочего контента (реализовано через ckeditor5)
4) Функционал откликов (подробнее можно прочесть в закрепленной новости ;) )
5) При создании объявление обязательно указать одну категорию (оставила возможность множественного выбора, просто закомментировала этот момент в форме)
6) Рассылка о новостях по почте (через сигналы)

Добавила отсебятины:
1) Расширила возможности личного кабинета: аватарка, биография, возможность удалить аккаунт
2) Также автор объявления помимо редактирования может удалить его
3) Страничка со всеми новостям/с конкретной; новости создает ТОЛЬКО АДМИН через админку
4) Добавила связь с поддержкой посредством гугл-формы
5) Ресет пароля по ссылке
6) Просмотр профиля пользователя с инфой о нем и его объявлениях
7) Локализация времени
8) Статические странички с сообщениями об успешной отправке письма и тд

Пара комментариев:
• Периодически случаются проблемы с рассылкой (smtplib.SMTPServerDisconnected), поэтому надо тестить по своим данным. Пробовала и через яндекс, и через рамблер (по дефолту стоит гугл) - все тщетно. Плюс ко всемy, у меня этот функционал работает только с VPN. Данные о сервере у меня в формате .env, не стала загружать сюда.
• В шаблон работы с откликами добавила AJAX-запросы, чтобы не перезагружать всю страницу (после принятия/отклонения отклика)
• Поле video из модели объявления не входит в ckeditor, является просто FileField
