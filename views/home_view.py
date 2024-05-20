from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        welcome_label = QLabel("Welcome to the Ticket Booking System")
        layout.addWidget(welcome_label)

        self.setLayout(layout)
