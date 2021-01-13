from flask_classful import FlaskView, route
from flask import render_template, request, session, flash, redirect, url_for
from model import UserModel
# from middleware import Middleware

class AuthController(FlaskView):
    @route('/login', methods=['GET', 'POST'])
    def login_page(self):
        if session.get('username'):
            flash("Kamu sudah login", 'error')
            return redirect(url_for("CustomerController:home_0"))
        if request.method == 'POST':
            user_model = UserModel()
            if user_model.check_login(**request.form):
                session['username'] = request.form.get('username')
                return redirect(url_for("CustomerController:home_0"))
            else:
                flash('Username Dan Password Salah', 'error')
        return render_template("login.html")

    @route('/register', methods=['GET', 'POST'])
    def register_page(self):
        if session.get('username'):
            flash("Kamu sudah login", 'error')
            return redirect(url_for("CustomerController:home_0"))
        if request.method == 'POST':
            user_model = UserModel()
            if user_model.insert(request.form):
                flash("registrasi sukses, silahkan Login!", 'success')
                return redirect(url_for("AuthController:login_page"))
            else:
                flash('Registrasi Gagal!', 'error')
        return render_template("register.html")

    @route('/logout')
    def logout(self):
        session.clear()
        flash('Sukses logout akun', 'success')
        return redirect(url_for('AuthController:login_page'))