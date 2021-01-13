import os
from flask_classful import FlaskView, route
from flask import render_template, render_template, request, session, flash, redirect, url_for
from werkzeug.utils import secure_filename
from model import EventModel, CategoryModel, TicketModel, UserModel, OrderModel


class CustomerController(FlaskView):

    @route('/')
    @route('/home')
    def home(self):
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))
        return render_template("home.html")

    @route('/profile', methods=['GET', 'POST'])
    def profile(self):
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))
        
        user_model = UserModel()
        if request.method == 'POST':
            form = request.form.to_dict()
            avatar = request.files['avatar']
            if avatar:
                filename = secure_filename(avatar.filename)
                avatar.save(os.path.join('./frontend/assets/uploads', filename))
                form['avatar'] = filename
            if user_model.update(form, form['id']):
                flash("Berhasil update data user!", 'success')
            else:
                flash('Gagal update data user!', 'error')
        
        current_user = user_model.get_current_user()
        print(current_user)
        return render_template("profile.html", current_user=current_user)

    @route('/orders')
    def orders(self):
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))

        order_model = OrderModel()
        ticket_model = TicketModel()
        orders = order_model.get_user_orders()
        orders = ticket_model.get_order_ticket(orders)
        return render_template("orders.html", orders=orders)

    @route('/events')
    def events(self):
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))
        event_model = EventModel()
        category_model = CategoryModel()
        ticket_model = TicketModel()
        current_category = request.args.get('category')
        if current_category and current_category != 'all':
            current_category = int(current_category)
            events = event_model.get_category(int(current_category))
        else:
            events = event_model.get_all()
            current_category = 'all'
        events = ticket_model.get_event_tickets(events)
        categories = category_model.get_all()
        return render_template("events.html", 
            events=events,
            categories=categories, 
            current_category=current_category)