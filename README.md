# discord.py Crash Bot

Установите библиотеку discord.py

Чтобы бот работал нужно ввести свой дискорд ID на 17 строчке и токен вашего бота в конце.

Добавьте на нужный сервер, поместите роль бота выше всех остальных, у бота должны быть права администратора.

На этом сервере у вас должен быть открыт ЛС, чтобы бот мог вам писать.

При запуске бота его статус будет оффлайн, но он будет работать.

Для запуска пропишите .start "ваш текст"

Это команда удалится, после этого запустится краш, что будет сделано:
1. Удалятся все эмодзи.
2. Удалятся все стикеры.
3. Удалятся все роли.
4. Удалятся все каналы.
5. Сервер переименуется в "ваш текст".
6. Создадутся 200 каналов и ролей с названием "ваш текст".
7. В каждый канал отправится сообщение: @everyone "ваш текст"
8. Всех пользователей забанит.
