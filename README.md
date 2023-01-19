# Описание
____
Данный телеграм бот предназначен для ведения личных расходов. 
Запись данных будет происходить в Google таблицу, доступ к боту и данным будет только у вас.
Перед началом работы с ботом, вам нужно будет выполнить несколько подготовительных шагов описанных ниже.

## Шаг №1. Создание бота в Телеграме.
1. Перейдите в диалог с инструментом для разработки чатов — https://telegram.me/BotFather.
2. Нажмите кнопку «Start» или введите в диалоге команду /start.
3. Далее введите команду /newbot, чтобы сделать новый бот.
4. Укажите название — как будет отображаться чат в списке контактов.
5. Последнее — системное имя: это то, что будет ником после знака @.

Название может быть любым: нестрашно, если оно будет дублировать уже существующие. 
Но системное имя обязательно должно быть уникальным. 
Если имя уже занято, вы увидите подсказку: «Sorry, this username is already taken. Please try something different».

После успешного создания вы получите токен. Сохраните его, он понадобится для дальнейшей интеграции. 
Если вы закрыли окно и нужно снова найти токен, напишите в диалоге команду /token. 

Подробнее можно узнать пройдя по ссылке: https://sendpulse.com/ru/knowledge-base/chatbot/telegram/create-telegram-chatbot

## Шаг №2. Создание Google Table.
1. Войдите в свой Google Account
2. Перейдите по ссылке: https://docs.google.com/spreadsheets/d/1dq9hVxhARG7Q-Ij78fEijACe0sLc58sHLMmf6dTJ-Lg/edit#gid=0
3. Сделайте копию таблицы себе на Google account: Файл -> Создать копию -> Скопировать
4. Зайдите в своем аккаунте в скопированную вами таблицу
5. Перейдите на второй лист - "Sheet2"
6. В колонках А1, В1, С1, D1, E1 измените "url_table" на url своей таблицы, как показано на скриншоте, и нажмите "открыть доступ"

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/1f6aff05-4815-4ba9-b96e-51d843e43bea.jpeg?raw=true)

## Шаг №3. Настройка Google API
1. Заходим в <a href="https://console.developers.google.com/apis/dashboard" target="_blank" rel="nofollow noopener">консоль настройки Google API</a> и создаем проект

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_1.jpg?raw=true)

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_2.jpg?raw=true)

2. В меню "Credentials" нажимаем "Create credentials", затем выбираем "Service account"

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_3.jpg?raw=true)

3. Вписываем имя для сервисного аккаунта

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_4.jpg?raw=true)

4. Ставим доступ для нашего проекта, нажимаем "DONE"

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_5.jpg?raw=true)

5. Заходим на сервисный аккаунт

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_6.jpg?raw=true)

6. Нажимаем "Keys" -> "ADD KEY" -> "Create new key"

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_7.jpg?raw=true)

7. Выбираем формат "JSON", у скачанного файла меняем имя на более понятное для вас и запоминаем путь к нему
8. Открываем сохраненный файл в виде блокнота, копируем "client_email"
9. Заходим в Google Table и добавляем в "Настройки доступа" скопированный "client_email", с атрибутом "Редактор"

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_9.jpg?raw=true)

10. Включаем доступ API для проекта. Заходим в <a href="https://console.developers.google.com/apis/dashboard" target="_blank" rel="nofollow noopener">консоль настройки Google API</a>. Проверяем что выбран проект, который мы создали и нажимаем на "ENABLE APIS AND SERVICES"

![](https://github.com/Shone-Kristas/tgbot_for_expenses/blob/master/images/API_10.jpg?raw=true)

11. В поле поиска "Search for APIs and Services", находим "Google Drive API" и "Google Sheets API" активируем их

12. Остается только внести свои данные в код:
    * Вместо "my_token" - в кавычках, внести токен полученный при создании телеграм бота из Шаг№1
    * Вместо "my_googlesheet_id" - в кавычках, внести url скопированной таблицы из Шаг№2 п.6
    * Вместо '/home/nize/Загрузки/проги/tgbot_Расходы/my_acc.json' - прописать путь к вашему json файлу из Шаг№3 п.7
    * Удалить строку "from keys import my_token, my_googlesheet_id"

```
from keys import my_token, my_googlesheet_id

bot_token = my_token
googlesheet_id = my_googlesheet_id
bot = telebot.TeleBot(bot_token)
gc = gspread.service_account(filename='/home/nize/Загрузки/проги/tgbot_Расходы/my_acc.json')
```



