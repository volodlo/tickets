from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from db import get_db_connection

class BookingView(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

        layout = QVBoxLayout()

        self.destination_label = QLabel("Destination")
        self.destination_entry = QLineEdit()
        layout.addWidget(self.destination_label)
        layout.addWidget(self.destination_entry)

        self.date_label = QLabel("Date")
        self.date_entry = QLineEdit()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_entry)

        self.price_label = QLabel("Price")
        self.price_entry = QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_entry)

        self.book_button = QPushButton("Book Ticket")
        self.book_button.clicked.connect(self.book_ticket)
        layout.addWidget(self.book_button)

        self.setLayout(layout)

    def book_ticket(self):
        destination = self.destination_entry.text()
        date = self.date_entry.text()
        price = self.price_entry.text()

        if destination and date and price:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute("INSERT INTO tickets (user_id, destination, date, price) VALUES (?, ?, ?, ?)",
                      (self.user_id, destination, date, price))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Ticket booked successfully")
        else:
            QMessageBox.critical(self, "Error", "Please fill all fields")
