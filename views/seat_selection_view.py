from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMessageBox, QGridLayout
from db import get_db_connection
from views.payment_view import PaymentView


class SeatSelectionView(QWidget):
    def __init__(self, user_id, route_id):
        super().__init__()
        self.user_id = user_id
        self.route_id = route_id

        self.setWindowTitle("Выбор мест")
        self.layout = QVBoxLayout()

        self.seat_grid = QGridLayout()
        self.seat_buttons = {}

        self.load_seats()

        self.layout.addLayout(self.seat_grid)
        self.setLayout(self.layout)

    def load_seats(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT transport_type FROM routes WHERE id = ?", (self.route_id,))
        transport_type = c.fetchone()[0]

        c.execute("SELECT seat FROM tickets WHERE route_id = ?", (self.route_id,))
        booked_seats = [row[0] for row in c.fetchall()]
        conn.close()

        if transport_type == 'bus':
            seat_layout = [
                ["1A", "1B", "", "", "1C", "1D"],
                ["2A", "2B", "", "", "2C", "2D"],
                ["3A", "3B", "", "", "3C", "3D"],
                ["4A", "4B", "", "", "4C", "4D"],
                ["5A", "5B", "", "", "5C", "5D"],
                ["6A", "6B", "", "", "6C", "6D"],
                ["7A", "7B", "", "", "7C", "7D"],
                ["8A", "8B", "", "", "8C", "8D"],
                ["9A", "9B", "", "", "9C", "9D"],
                ["10A", "10B", "", "", "10C", "10D"],
                ["11A", "11B", "", "", "11C", "11D"],
                ["12A", "12B", "", "", "12C", "12D"],
                ["13A", "13B", "", "", "13C", "13D"]
            ]
        elif transport_type == 'train':
            seat_layout = [
                ["1A", "1B", "1C", "1D"],
                ["2A", "2B", "2C", "2D"],
                ["3A", "3B", "3C", "3D"],
                ["4A", "4B", "4C", "4D"],
                ["5A", "5B", "5C", "5D"],
                ["6A", "6B", "6C", "6D"],
                ["7A", "7B", "7C", "7D"],
                ["8A", "8B", "8C", "8D"],
                ["9A", "9B", "9C", "9D"],
                ["10A", "10B", "10C", "10D"]
            ]
        elif transport_type == 'flight':
            seat_layout = [
                ["1A", "1B", "1C", "1D", "1E", "1F"],
                ["2A", "2B", "2C", "2D", "2E", "2F"],
                ["3A", "3B", "3C", "3D", "3E", "3F"],
                ["4A", "4B", "4C", "4D", "4E", "4F"],
                ["5A", "5B", "5C", "5D", "5E", "5F"],
                ["6A", "6B", "6C", "6D", "6E", "6F"],
                ["7A", "7B", "7C", "7D", "7E", "7F"],
                ["8A", "8B", "8C", "8D", "8E", "8F"],
                ["9A", "9B", "9C", "9D", "9E", "9F"],
                ["10A", "10B", "10C", "10D", "10E", "10F"],
                ["11A", "11B", "11C", "11D", "11E", "11F"],
                ["12A", "12B", "12C", "12D", "12E", "12F"],
                ["13A", "13B", "13C", "13D", "13E", "13F"],
                ["14A", "14B", "14C", "14D", "14E", "14F"],
                ["15A", "15B", "15C", "15D", "15E", "15F"]
            ]
        elif transport_type == 'water':
            seat_layout = [
                ["1A", "1B", "1C", "1D", "1E"],
                ["2A", "2B", "2C", "2D", "2E"],
                ["3A", "3B", "3C", "3D", "3E"],
                ["4A", "4B", "4C", "4D", "4E"],
                ["5A", "5B", "5C", "5D", "5E"],
                ["6A", "6B", "6C", "6D", "6E"],
                ["7A", "7B", "7C", "7D", "7E"],
                ["8A", "8B", "8C", "8D", "8E"],
                ["9A", "9B", "9C", "9D", "9E"],
                ["10A", "10B", "10C", "10D", "10E"]
            ]

        for row, seat_row in enumerate(seat_layout):
            for col, seat in enumerate(seat_row):
                if seat:
                    button = QPushButton(seat)
                    if seat in booked_seats:
                        button.setEnabled(False)
                        button.setStyleSheet("background-color: red")
                    else:
                        button.clicked.connect(lambda _, s=seat: self.book_seat(s))
                    self.seat_grid.addWidget(button, row, col)
                    self.seat_buttons[seat] = button

    def book_seat(self, seat):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO tickets (user_id, route_id, seat, status) VALUES (?, ?, ?, ?)",
                  (self.user_id, self.route_id, seat, 'Забронирован'))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Успех", f"Место {seat} забронировано")
        self.seat_buttons[seat].setEnabled(False)
        self.seat_buttons[seat].setStyleSheet("background-color: red")

        self.payment_view = PaymentView(self.user_id, self.route_id, seat)
        self.payment_view.show()
