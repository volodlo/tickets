from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from db import get_db_connection

class PaymentView(QWidget):
    def __init__(self, user_id, route_id, seat):
        super().__init__()
        self.user_id = user_id
        self.route_id = route_id
        self.seat = seat

        self.setWindowTitle("Оплата")
        layout = QVBoxLayout()

        self.amount_label = QLabel(f"Сумма к оплате: {self.get_price()} руб.")
        layout.addWidget(self.amount_label)

        self.card_number_label = QLabel("Номер карты")
        self.card_number_entry = QLineEdit()
        layout.addWidget(self.card_number_label)
        layout.addWidget(self.card_number_entry)

        self.expiry_date_label = QLabel("Срок действия (ММ/ГГ)")
        self.expiry_date_entry = QLineEdit()
        layout.addWidget(self.expiry_date_label)
        layout.addWidget(self.expiry_date_entry)

        self.cvv_label = QLabel("CVV")
        self.cvv_entry = QLineEdit()
        layout.addWidget(self.cvv_label)
        layout.addWidget(self.cvv_entry)

        self.pay_button = QPushButton("Оплатить")
        self.pay_button.clicked.connect(self.process_payment)
        layout.addWidget(self.pay_button)

        self.setLayout(layout)

    def get_price(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT price FROM routes WHERE id = ?", (self.route_id,))
        price = c.fetchone()[0]
        conn.close()
        return price

    def process_payment(self):
        card_number = self.card_number_entry.text()
        expiry_date = self.expiry_date_entry.text()
        cvv = self.cvv_entry.text()

        # Эмуляция успешной оплаты
        if card_number and expiry_date and cvv:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute("UPDATE tickets SET status = 'Куплен' WHERE user_id = ? AND route_id = ? AND seat = ?",
                      (self.user_id, self.route_id, self.seat))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Успех", "Оплата прошла успешно, билет куплен.")
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Пожалуйста, заполните все данные для оплаты.")
