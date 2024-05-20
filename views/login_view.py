import sqlite3
from PyQt5.QtWebEngineWidgets import QWebEngineView

def load(browser: QWebEngineView):
    browser.page().runJavaScript('''
        document.getElementById("login-form").addEventListener("submit", function(event) {
            event.preventDefault();
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;
            pywebview.api.login(username, password).then(handleLoginResponse);
        });

        function handleLoginResponse(response) {
            if (response.success) {
                window.location.href = "/";
            } else {
                alert("Неверное имя пользователя или пароль");
            }
        }
    ''')

def login(username, password):
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    return {'success': bool(user)}
