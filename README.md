# AI-Helper
This is an AI assistant designed to free you from daily routine tasks and make your life easier. For instance, you no longer need to manually track your weekly water intake or calculate the average—or even write code to compute these figures; simply ask the assistant to do it for you. And that is just a fraction of what this AI helper can do.

## Руководство по запуску:

1. Создайте файл ```.env``` в корневой папке проекта
2. Перейдите на сайт [API для разработчиков](https://developers.sber.ru/docs/ru/gigachat/individuals-quickstart)
3. Зарегистрируйтесь на сайте. Для физлиц, то есть некоммерческого использрвания подходит тариф **freemium** - на год у вас будет **бесплатный** доступ к API
4. Создайте проект в личном кабинете
5. Получите **AUTHORIZATION KEY** - он один, сохраните его!
6. В созданном в корне проекта фафле создайте переменную **AUTHORIZATION_KEY** и сохраните в неё ваш ключ
7. Найдите и скопируйте путь к таблице, с которой ИИ агент должен взаимодействовать
8. В файле .env сохраните путь в переменную **PATH_TO_FILE**
9. Все предварительные действия готовы. Запускайте main.py и пользуйтесь с удовольствием