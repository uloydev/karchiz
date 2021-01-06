from flask_classful import FlaskView, route
from flask import render_template

class AuthController(FlaskView):
    @route('/login')
    def login_page(self):
        return render_template("login.html")

    @route('/register')
    def register_page(self):
        return render_template("register.html")