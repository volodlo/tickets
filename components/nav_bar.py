from PyQt5.QtWidgets import QMenuBar, QAction

class NavBar(QMenuBar):
    def __init__(self, switch_view, logged_in):
        super().__init__()

        self.switch_view = switch_view

        self.home_action = QAction("Главная", self)
        self.home_action.triggered.connect(lambda: self.switch_view("home"))
        self.addAction(self.home_action)

        if logged_in:
            self.bus_booking_action = QAction("Автобусные билеты", self)
            self.bus_booking_action.triggered.connect(lambda: self.switch_view("bus_booking"))
            self.addAction(self.bus_booking_action)

            self.train_booking_action = QAction("Железнодорожные билеты", self)
            self.train_booking_action.triggered.connect(lambda: self.switch_view("train_booking"))
            self.addAction(self.train_booking_action)

            self.flight_booking_action = QAction("Авиабилеты", self)
            self.flight_booking_action.triggered.connect(lambda: self.switch_view("flight_booking"))
            self.addAction(self.flight_booking_action)

            self.water_booking_action = QAction("Водные билеты", self)
            self.water_booking_action.triggered.connect(lambda: self.switch_view("water_booking"))
            self.addAction(self.water_booking_action)

            self.my_tickets_action = QAction("Мои билеты", self)
            self.my_tickets_action.triggered.connect(lambda: self.switch_view("tickets"))
            self.addAction(self.my_tickets_action)

            self.logout_action = QAction("Выйти", self)
            self.logout_action.triggered.connect(lambda: self.switch_view("logout"))
            self.addAction(self.logout_action)
        else:
            self.login_action = QAction("Войти", self)
            self.login_action.triggered.connect(lambda: self.switch_view("login"))
            self.addAction(self.login_action)

            self.register_action = QAction("Регистрация", self)
            self.register_action.triggered.connect(lambda: self.switch_view("register"))
            self.addAction(self.register_action)
