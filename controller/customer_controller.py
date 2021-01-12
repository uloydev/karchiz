from flask_classful import FlaskView, route
from flask import render_template, render_template, request, session, flash, redirect, url_for
from model import EventModel, CategoryModel

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
        event_model = EventModel()
        category_model = CategoryModel()
        current_category = request.args.get('category')
        if current_category and current_category != 'all':
            current_category = int(current_category)
            events = event_model.get_category(int(current_category))
        else:
            events = event_model.get_all()
            current_category = 'all'
        categories = category_model.get_all()
        return render_template("events.html", 
            events=events,
            categories=categories, 
            current_category=current_category)