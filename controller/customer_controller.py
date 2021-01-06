from flask_classful import FlaskView, route
from flask import render_template

class CustomerController(FlaskView):
    @route('/')
    @route('/home')
    def index(self):
        return render_template("home.html")

    @route('/profile')
    def profile(self):
        return render_template("profile.html")

    @route('/orders')
    def orders(self):
        return render_template("orders.html")

    @route('/events')
    def events(self):
        return render_template("events.html")