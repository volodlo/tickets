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
