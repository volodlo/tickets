Документация проекта "Система бронирования билетов"
Описание проекта
Проект представляет собой систему бронирования билетов на различные виды транспорта (автобусы, поезда, самолеты и водный транспорт) с возможностью регистрации и авторизации пользователей. Приложение написано на Python с использованием PyQt5 и SQLite для хранения данных.

Структура проекта
arduino
Копировать код
Tickets/
├── main.py
├── templates/
│   ├── bus_booking.html
│   ├── train_booking.html
│   ├── flight_booking.html
│   ├── water_booking.html
│   ├── tickets.html
│   ├── login.html
│   └── register.html
└── views/
    ├── bus_booking_view.py
    ├── train_booking_view.py
    ├── flight_booking_view.py
    ├── water_booking_view.py
    ├── tickets_view.py
    ├── login_view.py
    └── register_view.py
main.py
Файл main.py содержит основной код для запуска приложения. Он включает в себя инициализацию базы данных, создание главного окна приложения и загрузку HTML-шаблонов.

Основные компоненты
MainWindow: Основное окно приложения.
init_db(): Функция для инициализации базы данных и заполнения её демонстрационными данными.
Обработчики для загрузки страниц и обработки URL-адресов.
Шаблоны HTML
Шаблоны HTML находятся в директории templates и содержат страницы для бронирования билетов, регистрации, авторизации и просмотра текущих билетов.

bus_booking.html: Страница для бронирования автобусных билетов.
train_booking.html: Страница для бронирования железнодорожных билетов.
flight_booking.html: Страница для бронирования авиабилетов.
water_booking.html: Страница для бронирования билетов на водный транспорт.
tickets.html: Страница для просмотра текущих билетов.
login.html: Страница для авторизации.
register.html: Страница для регистрации.
Виды (views)
В директории views находятся файлы с обработчиками для каждой из страниц. Каждый файл содержит функции для загрузки соответствующих страниц и взаимодействия с базой данных.

bus_booking_view.py
Файл bus_booking_view.py содержит функции для обработки бронирования автобусных билетов.

python
Копировать код
import json
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("bus-booking-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var origin = document.getElementById("origin").value;
            var destination = document.getElementById("destination").value;
            var date = document.getElementById("date").value;
            pywebview.api.busBooking(origin, destination, date).then(updateRoutes);
        });

        function updateRoutes(routes) {
            var routesUl = document.getElementById("routes-list");
            routesUl.innerHTML = "";
            routes.forEach(function(route) {
                var li = document.createElement("li");
                li.className = "list-group-item";
                li.innerHTML = "ID: " + route.id + ", " + route.origin + " в " + route.destination + " на " + route.date + ", Цена: " + route.price + " руб.";
                routesUl.appendChild(li);
            });
        }
    ''')

def busBooking(origin, destination, date):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT id, origin, destination, date, price FROM routes WHERE transport_type = 'bus' AND origin LIKE ? AND destination LIKE ? AND date LIKE ?",
              (f"%{origin}%", f"%{destination}%", f"%{date}%"))
    routes = c.fetchall()
    conn.close()

    routes_list = []
    for route in routes:
        routes_list.append({
            'id': route[0],
            'origin': route[1],
            'destination': route[2],
            'date': route[3],
            'price': route[4]
        })

    return json.dumps(routes_list)
train_booking_view.py
Файл train_booking_view.py содержит функции для обработки бронирования железнодорожных билетов.

python
Копировать код
import json
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("train-booking-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var origin = document.getElementById("origin").value;
            var destination = document.getElementById("destination").value;
            var date = document.getElementById("date").value;
            pywebview.api.trainBooking(origin, destination, date).then(updateRoutes);
        });

        function updateRoutes(routes) {
            var routesUl = document.getElementById("routes-list");
            routesUl.innerHTML = "";
            routes.forEach(function(route) {
                var li = document.createElement("li");
                li.className = "list-group-item";
                li.innerHTML = "ID: " + route.id + ", " + route.origin + " в " + route.destination + " на " + route.date + ", Цена: " + route.price + " руб.";
                routesUl.appendChild(li);
            });
        }
    ''')

def trainBooking(origin, destination, date):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT id, origin, destination, date, price FROM routes WHERE transport_type = 'train' AND origin LIKE ? AND destination LIKE ? AND date LIKE ?",
              (f"%{origin}%", f"%{destination}%", f"%{date}%"))
    routes = c.fetchall()
    conn.close()

    routes_list = []
    for route in routes:
        routes_list.append({
            'id': route[0],
            'origin': route[1],
            'destination': route[2],
            'date': route[3],
            'price': route[4]
        })

    return json.dumps(routes_list)
flight_booking_view.py
Файл flight_booking_view.py содержит функции для обработки бронирования авиабилетов.

python
Копировать код
import json
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("flight-booking-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var origin = document.getElementById("origin").value;
            var destination = document.getElementById("destination").value;
            var date = document.getElementById("date").value;
            pywebview.api.flightBooking(origin, destination, date).then(updateRoutes);
        });

        function updateRoutes(routes) {
            var routesUl = document.getElementById("routes-list");
            routesUl.innerHTML = "";
            routes.forEach(function(route) {
                var li = document.createElement("li");
                li.className = "list-group-item";
                li.innerHTML = "ID: " + route.id + ", " + route.origin + " в " + route.destination + " на " + route.date + ", Цена: " + route.price + " руб.";
                routesUl.appendChild(li);
            });
        }
    ''')

def flightBooking(origin, destination, date):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT id, origin, destination, date, price FROM routes WHERE transport_type = 'flight' AND origin LIKE ? AND destination LIKE ? AND date LIKE ?",
              (f"%{origin}%", f"%{destination}%", f"%{date}%"))
    routes = c.fetchall()
    conn.close()

    routes_list = []
    for route in routes:
        routes_list.append({
            'id': route[0],
            'origin': route[1],
            'destination': route[2],
            'date': route[3],
            'price': route[4]
        })

    return json.dumps(routes_list)
water_booking_view.py
Файл water_booking_view.py содержит функции для обработки бронирования билетов на водный транспорт.

python
Копировать код
import json
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("water-booking-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var origin = document.getElementById("origin").value;
            var date = document.getElementById("date").value;
            pywebview.api.waterBooking(origin, date).then(updateRoutes);
        });

        function updateRoutes(routes) {
            var routesUl = document.getElementById("routes-list");
            routesUl.innerHTML = "";
            routes.forEach(function(route) {
                var li = document.createElement("li");
                li.className = "list-group-item";
                li.innerHTML = "ID: " + route.id + ", Экскурсия: " + route.origin + " на " + route.date + ", Цена: " + route.price + " руб.";
                routesUl.appendChild(li);
            });
        }
    ''')

def waterBooking(origin, date):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT id, origin, date, price FROM routes WHERE transport_type = 'water' AND origin LIKE ? AND date LIKE ?",
              (f"%{origin}%", f"%{date}%"))
    routes = c.fetchall()
    conn.close()

    routes_list = []
    for route in routes:
        routes_list.append({
            'id': route[0],
            'origin': route[1],
            'date': route[2],
            'price': route[3]
        })

    return json.dumps(routes_list)
tickets_view.py
Файл tickets_view.py содержит функции для отображения списка текущих билетов пользователя.

python
Копировать код
import json
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        function loadTickets() {
            pywebview.api.loadTickets().then(updateTickets);
        }

        function updateTickets(tickets) {
            var ticketsUl = document.getElementById("tickets-list");
            ticketsUl.innerHTML = "";
            tickets.forEach(function(ticket) {
                var li = document.createElement("li");
                li.className = "list-group-item";
                li.innerHTML = "ID: " + ticket.id + ", " + ticket.origin + " в " + ticket.destination + " на " + ticket.date + ", Место: " + ticket.seat + ", Статус: " + ticket.status;
                ticketsUl.appendChild(li);
            });
        }

        loadTickets();
    ''')

def loadTickets():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''
        SELECT t.id, r.origin, r.destination, r.date, t.seat, t.status
        FROM tickets t
        JOIN routes r ON t.route_id = r.id
    ''')
    tickets = c.fetchall()
    conn.close()

    tickets_list = []
    for ticket in tickets:
        tickets_list.append({
            'id': ticket[0],
            'origin': ticket[1],
            'destination': ticket[2],
            'date': ticket[3],
            'seat': ticket[4],
            'status': ticket[5]
        })

    return json.dumps(tickets_list)
login_view.py
Файл login_view.py содержит функции для обработки авторизации пользователей.

python
Копировать код
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("login-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;
            pywebview.api.login(username, password).then(handleLoginResponse);
        });

        function handleLoginResponse(response) {
            if (response.success) {
                window.location.href = "/";
            } else {
                alert("Неверное имя пользователя или пароль");
            }
        }
    ''')

def login(username, password):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    return {'success': bool(user)}
register_view.py
Файл register_view.py содержит функции для обработки регистрации новых пользователей.

python
Копировать код
import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("register-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;
            pywebview.api.register(username, password).then(handleRegisterResponse);
        });

        function handleRegisterResponse(response) {
            if (response.success) {
                window.location.href = "/login";
            } else {
                alert("Пользователь с таким именем уже существует");
            }
        }
    ''')

def register(username, password):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        response = {'success': True}
    except sqlite3.IntegrityError:
        response = {'success': False}
    finally:
        conn.close()

    return response
