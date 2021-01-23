import os
from datetime import datetime
from flask_classful import FlaskView, route
from flask import render_template, render_template, request, session, flash, redirect, url_for
from werkzeug.utils import secure_filename
from model import EventModel, CategoryModel, TicketModel, UserModel, OrderModel


class CustomerController(FlaskView):

    @route('/')
    @route('/home')
    def home(self) -> str:
        """Fungsi home digunakan untuk menampilkan halaman home.

        Returns:
            str: html text
        """
        # inisiasi model yang diperlukan
        event_model = EventModel()
        ticket_model = TicketModel()
        order_model = OrderModel()

        # cek jika user belum login maka redirect ke halaman login
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))

        # mengambil semua data events dari database
        events = event_model.get_all()
        # parsing events agar menjadi list dari object Event dan diambil tiga event terbaru
        events = event_model.parseList(events)
        if len(events) > 3:
            events = events[-3:]
        # mengambil data ticket dari semua events
        events = ticket_model.get_event_tickets(events)

        # parsing orders agar menjadi list dari object Order dan diambil dua order terbaru
        orders = order_model.get_user_orders()
        if len(orders) > 2:
            orders = orders[-2:]
        # mengambil data ticket dari semua orders
        orders = ticket_model.get_order_ticket(orders)
        return render_template("home.html", events = events, orders=orders)

    @route('/profile', methods=['GET', 'POST'])
    def profile(self) -> str:
        """Fungsi profile digunakan untuk menampilkan halaman profile.

        Returns:
            str: html text
        """
        # inisiasi model yang diperlukan
        user_model = UserModel()

        # cek jika user belum login maka redirect ke halaman login
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))
        
        # cek jika request POST
        if request.method == 'POST':
            # mengambil data dari input user menjadi dictionary
            form = request.form.to_dict()
            # handle upload file avatar user
            avatar = request.files['avatar']
            if avatar:
                filename = secure_filename(avatar.filename)
                avatar.save(os.path.join('./frontend/assets/uploads', filename))
                form['avatar'] = filename
            
            # cek jika update user berhasil
            if user_model.update(form, form['id']):
                flash("Berhasil update data user!", 'success')
            else:
                flash('Gagal update data user!', 'error')
        
        # mengambil data user yang sedang login
        current_user = user_model.get_current_user()
        return render_template("profile.html", current_user=current_user)

    @route('/orders')
    def orders(self):
        """Fungsi orders digunakan untuk menampilkan halaman orders.

        Returns:
            str: html text
        """
        # inisiasi model yang diperlukan
        order_model = OrderModel()
        ticket_model = TicketModel()

        # cek jika user belum login maka redirect ke halaman login
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))

        # mengambil semua data order yang dimiliki user yang sedang login
        orders = order_model.get_user_orders()
        # mengambil data tiket dari order yang dimiliki user yang sedang login
        orders = ticket_model.get_order_ticket(orders)
        return render_template("orders.html", orders=orders)

    @route('/events')
    def events(self):
        """Fungsi events digunakan untuk menampilkan halaman events.

        Returns:
            str: html text
        """
        # inisiasi model yang diperlukan
        event_model = EventModel()
        category_model = CategoryModel()
        ticket_model = TicketModel()
        
        # cek jika user belum login maka redirect ke halaman login
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))
        current_category = request.args.get('category')

        # cek jika kategori yng dipilih tidak kosong dan bukan 'all'
        if current_category and current_category != 'all':
            # mengambil semua events sesuai kategori yang dipilih
            current_category = int(current_category)
            events = event_model.get_category(int(current_category))
        else:
            # mengambil semua events dari database
            events = event_model.get_all()
            current_category = 'all'
        
        # parsing events agar menjadi list dari object Event
        events = event_model.parseList(events)
        # mengambil data ticket dari semua events
        events = ticket_model.get_event_tickets(events)
        # mengambil semua data category di database
        categories = category_model.get_all()
        # parsing categories agar menjadi list dari object Category
        categories = category_model.parseList(categories)
        return render_template("events.html", 
            events=events,
            categories=categories, 
            current_category=current_category)

    @route('/place-order', methods=['POST'])
    def place_order(self):
        """Fungsi place_order digunakan untuk input order ke database.

        Returns:
            str: html text
        """
        # inisiasi model yang diperlukan
        user_model = UserModel()
        order_model = OrderModel()
        user = user_model.get_current_user()

        # cek jika user belum login maka redirect ke halaman login
        if not session.get('username'):
            flash('Kamu Belum Login!', 'error')
            return redirect(url_for("AuthController:login_page"))

        # mengambil data dari input user menjadi dictionary
        form = request.form.to_dict()
        form['user_id'] = user.get_id()
        form['order_time'] = datetime.now().strftime('%Y-%m-%d %X')

        # cek jika berhasil melakukan order
        if order_model.insert(form):
            flash("Berhasil order event!", 'success')
        else:
            flash("Gagal order event!", 'error')
        return redirect(url_for('CustomerController:orders'))
            
