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
