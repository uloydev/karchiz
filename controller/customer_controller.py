from flask_classful import FlaskView, route
from flask import render_template, render_template, request, session, flash, redirect, url_for

class CustomerController(FlaskView):

    @route('/')
    @route('/home')
    def home(self):
        if not session.get('username'):
            flash('Kamu Belum Login!')
            return redirect(url_for("AuthController:login_page"))
        return render_template("home.html")

    @route('/profile')
    def profile(self):
        if not session.get('username'):
            flash('Kamu Belum Login!')
            return redirect(url_for("AuthController:login_page"))
        return render_template("profile.html")

    @route('/orders')
    def orders(self):
        if not session.get('username'):
            flash('Kamu Belum Login!')
            return redirect(url_for("AuthController:login_page"))
        return render_template("orders.html")

    @route('/events')
    def events(self):
        if not session.get('username'):
            flash('Kamu Belum Login!')
            return redirect(url_for("AuthController:login_page"))
        return render_template("events.html")