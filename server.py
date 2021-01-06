import pymysql
from flask import Flask, render_template
from config import Config
from model import UserModel


class Server:
    def __init__(self):
        self.app = Flask("__main__", static_url_path="/assets", template_folder="frontend/html", static_folder="frontend/assets")
        
        config = Config().get()
        self.mysql = pymysql.connect(**config)

        @self.app.route('/')
        @self.app.route('/home')
        def index():
            return render_template("home.html")

        @self.app.route('/login')
        def login():
            return render_template("login.html")

        @self.app.route('/register')
        def register():
            return render_template("register.html")

        @self.app.route('/profile')
        def profile():
            return render_template("profile.html")

        @self.app.route('/orders')
        def orders():
            return render_template("orders.html")

        @self.app.route('/events')
        def events():
            return render_template("events.html")

    def run(self):
        self.app.run()
