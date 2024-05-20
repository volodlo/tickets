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
