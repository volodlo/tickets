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
