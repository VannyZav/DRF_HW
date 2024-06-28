# Сервис склада

#### Сервис представляет собой интерфейс для поставщиков и потребителей.<br/>Поставщики могут поставлять товар, увеличивая его количество, а потребители могут забирать товар, уменьшая его количество

### для развертывание проекта выполните следующие команды:
1. склонируйте репозиторий к себе на компьютер или скачайте проект zip файлом.<br/>
   git clone https://github.com/VannyZav/DRF_HW.git
2. создайте виртуальное окружение:<br/>
   python -m venv myenv<br/>
   py -m venv myenv   # введите на Windows, если первый вариант не сработал<br/>
   source myenv/bin/activate  # для Linux и macOS<br/>
   myenv\Scripts\activate     # для Windows<br/>
   где myenv — это название вашего виртуального окружения.<br/>
3. установите зависимости pip install -r requirements.txt
4. в консоли зайдите в папку проекта и оттуда запустите приложение командой:<br/>
5. python manage.py migrate (если выдало ошибку, возможно перед этой командой нужно выполнить python manage.py makemigrations) 
6. в консоли зайдите в папку проекта и оттуда запустите приложение командой:<br/>
- python manage.py runserver 

### инструкция к API сервису и ограничения по типу пользователя:
1. Зарегистрироваться(доступно всем типам пользователям):<br/>
   - http://127.0.0.1:8000/ApiUser/
   - использовать метод POST
   - по таким полям:
   -{
   -    "username": "CharField",
   -    "email": "EmailField",
   -    "password": "CharField",
   -    "user_type": "CharField"
   -}
2. Получить список пользователей(доступно только администратору):<br/>
   - http://127.0.0.1:8000/ApiUser/
   - использовать метод GET
   - вернутся такие поля:
   -{
   -    "id": Integer,
   -    "username": "CharField",
   -    "email": "EmailField",
   -    "user_type": "CharField"
   -}

3. Получить, изменить, частично изменить, удалить определенного пользователя(доступно администратору или авторизованному владельцу данных):<br/>
- http://127.0.0.1:8000/ApiUser/<id>/
- использовать метод GET, PUT, PATCH, DELETE
- использовать такие поля:
   -{
   -    "username": "CharField",
   -    "email": "EmailField",
   -    "password": "CharField",
   -    "user_type": "CharField"
   -}

4. Зарегистрировать склад(доступно только администратору):
   - http://127.0.0.1:8000/WareHouse/
   - использовать метод POST
   - с такими полями:
   -{
   -   "name": "CharField"
   -}

5. Получить список складов(доступно всем):
   - http://127.0.0.1:8000/WareHouse/
   - использовать метод GET
   - вернутся поля:
   -{
   -    "id": Integer,
   -    "name": "CharField"
   -}

6. Получить определенный склад(доступно всем):
   - http://127.0.0.1:8000/WareHouse/<id>
   - использовать метод GET
   - вернутся поля:
   -{
   -    "id": Integer,
   -    "name": "CharField",
   -}

7. Изменить, частично изменить, удалить определенный склад(доступно только администратору):
   - http://127.0.0.1:8000/WareHouse/<id>
   - использовать методы PUT, PATCH, DELETE
   - поля:
   -{
   -    "name": "CharField"
   -}

8. Зарегистрировать продукт(доступно только администратору):
   - http://127.0.0.1:8000/product/
   - использовать метод POST
   - с такими полями:
   -{
   -    "count": PositiveInteger,
   -    "name": "CharField",
   -    "warehouse": Integer,
   -}

9. Получить список продуктов(доступно всем):
   - http://127.0.0.1:8000/product/
   - использовать метод GET
   - вернутся поля:
   -{
        "id": Integer,
        "count": PositiveInteger,
        "name": "CharField",
        "warehouse": Integer
   -}

10. Получить определенный продукт(доступно всем):
    - http://127.0.0.1:8000/product/<id>
    - использовать метод GET
   - вернутся поля:
   -{
        "id": Integer,
        "count": PositiveInteger,
        "name": "CharField",
        "warehouse": Integer
   -}

11. Изменить, частично изменить определенный продукт(доступно администратору, поставщику и потребителю):




   
