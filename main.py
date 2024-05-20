import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from views import bus_booking_view, train_booking_view, flight_booking_view, water_booking_view, tickets_view, login_view, register_view


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Система бронирования билетов')
        self.showFullScreen()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.browser.urlChanged.connect(self.on_url_changed)

        self.load_page('index.html')

    def load_page(self, page):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates', page))
        if os.path.exists(file_path):
            local_url = QUrl.fromLocalFile(file_path)
            self.browser.setUrl(local_url)
        else:
            print(f"Ошибка: файл {file_path} не найден.")

    def on_url_changed(self, url):
        page = url.fileName()
        if page == "bus_booking.html":
            bus_booking_view.load(self.browser)
        elif page == "train_booking.html":
            train_booking_view.load(self.browser)
        elif page == "flight_booking.html":
            flight_booking_view.load(self.browser)
        elif page == "water_booking.html":
            water_booking_view.load(self.browser)
        elif page == "tickets.html":
            tickets_view.load(self.browser)
        elif page == "login.html":
            login_view.load(self.browser)
        elif page == "register.html":
            register_view.load(self.browser)


def init_db():
    import sqlite3
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS tickets (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 route_id INTEGER,
                 seat TEXT,
                 status TEXT,
                 FOREIGN KEY(user_id) REFERENCES users(id),
                 FOREIGN KEY(route_id) REFERENCES routes(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS routes (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 transport_type TEXT,
                 origin TEXT,
                 destination TEXT,
                 date TEXT,
                 price REAL)''')

    demo_routes = [
        ('bus', 'Москва', 'Санкт-Петербург', '2024-06-01', 3000.0),
        ('bus', 'Казань', 'Нижний Новгород', '2024-06-02', 2500.0),
        ('bus', 'Екатеринбург', 'Пермь', '2024-06-03', 2000.0),
        ('bus', 'Краснодар', 'Ростов-на-Дону', '2024-06-04', 1500.0),
        ('bus', 'Уфа', 'Самара', '2024-06-05', 1800.0),
        ('bus', 'Новосибирск', 'Омск', '2024-06-06', 2200.0),
        ('bus', 'Волгоград', 'Астрахань', '2024-06-07', 2400.0),
        ('bus', 'Иркутск', 'Красноярск', '2024-06-08', 2600.0),
        ('bus', 'Владивосток', 'Хабаровск', '2024-06-09', 2800.0),
        ('bus', 'Мурманск', 'Архангельск', '2024-06-10', 3000.0),
        ('train', 'Москва', 'Сочи', '2024-06-01', 4500.0),
        ('train', 'Санкт-Петербург', 'Калининград', '2024-06-02', 5000.0),
        ('train', 'Казань', 'Самара', '2024-06-03', 4700.0),
        ('train', 'Екатеринбург', 'Челябинск', '2024-06-04', 4800.0),
        ('train', 'Новосибирск', 'Томск', '2024-06-05', 4900.0),
        ('train', 'Красноярск', 'Иркутск', '2024-06-06', 5100.0),
        ('train', 'Владивосток', 'Уссурийск', '2024-06-07', 5300.0),
        ('train', 'Мурманск', 'Петрозаводск', '2024-06-08', 5500.0),
        ('train', 'Саратов', 'Волгоград', '2024-06-09', 5700.0),
        ('train', 'Ростов-на-Дону', 'Краснодар', '2024-06-10', 5900.0),
        ('flight', 'Москва', 'Новосибирск', '2024-06-01', 15000.0),
        ('flight', 'Санкт-Петербург', 'Екатеринбург', '2024-06-02', 16000.0),
        ('flight', 'Казань', 'Уфа', '2024-06-03', 17000.0),
        ('flight', 'Сочи', 'Ростов-на-Дону', '2024-06-04', 18000.0),
        ('flight', 'Владивосток', 'Хабаровск', '2024-06-05', 19000.0),
        ('flight', 'Краснодар', 'Санкт-Петербург', '2024-06-06', 20000.0),
        ('flight', 'Самара', 'Казань', '2024-06-07', 21000.0),
        ('flight', 'Иркутск', 'Красноярск', '2024-06-08', 22000.0),
        ('flight', 'Мурманск', 'Москва', '2024-06-09', 23000.0),
        ('flight', 'Волгоград', 'Саратов', '2024-06-10', 24000.0),
        ('water', 'Экскурсия по Москве-реке', '', '2024-06-01', 1000.0),
        ('water', 'Нева и Финский залив', '', '2024-06-02', 1200.0),
        ('water', 'Волга и Канал имени Москвы', '', '2024-06-03', 1400.0),
        ('water', 'Озеро Байкал', '', '2024-06-04', 1600.0),
        ('water', 'Кронштадт и форты', '', '2024-06-05', 1800.0),
        ('water', 'Петропавловская крепость', '', '2024-06-06', 2000.0),
        ('water', 'Валаам и Ладожское озеро', '', '2024-06-07', 2200.0),
        ('water', 'Кижи и Онежское озеро', '', '2024-06-08', 2400.0),
        ('water', 'Плес и Волга', '', '2024-06-09', 2600.0),
        ('water', 'Золотое кольцо России', '', '2024-06-10', 2800.0)
    ]

    c.executemany("INSERT INTO routes (transport_type, origin, destination, date, price) VALUES (?, ?, ?, ?, ?)", demo_routes)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
