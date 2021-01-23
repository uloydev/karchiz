from flask_classful import FlaskView, route
from flask import render_template, request, session, flash, redirect, url_for
from model import UserModel
# from middleware import Middleware

class AuthController(FlaskView):
    @route('/login', methods=['GET', 'POST'])
    def login_page(self) -> str:
        """Fungsi login_page digunakan untuk menampilkan halaman login.

        Returns:
            str: html text
        """
        # cek jika user sudah login maka redirect ke home page
        if session.get('username'):
            flash("Kamu sudah login", 'error')
            return redirect(url_for("CustomerController:home_0"))
        # cek jika request POST
        if request.method == 'POST':
            user_model = UserModel()
            # cek jika berhasil login maka redirect ke home page
            if user_model.check_login(**request.form):
                session['username'] = request.form.get('username')
                return redirect(url_for("CustomerController:home_0"))
            # jika gagal login maka kembali ke halaman login
            else:
                flash('Username Dan Password Salah', 'error')
        return render_template("login.html")

    @route('/register', methods=['GET', 'POST'])
    def register_page(self):
        """Fungsi register_page digunakan untuk menampilkan halaman register.

        Returns:
            str: html text
        """
        # cek jika user sudah login maka redirect ke home page
        if session.get('username'):
            flash("Kamu sudah login", 'error')
            return redirect(url_for("CustomerController:home_0"))
        # cek jika request POST
        if request.method == 'POST':
            user_model = UserModel()
            # cek jika berhasil input user maka redirect ke login page
            if user_model.insert(request.form):
                flash("registrasi sukses, silahkan Login!", 'success')
                return redirect(url_for("AuthController:login_page"))
            # jika gagal login maka kembali ke halaman register
            else:
                flash('Registrasi Gagal!', 'error')
        return render_template("register.html")

    @route('/logout')
    def logout(self) -> str:
        """Fungsi logout digunakan untuk keluar dari akun.

        Returns:
            str: html text
        """
        # membersihkan sesi user dan kembali ke halaman login
        session.clear()
        flash('Sukses logout akun', 'success')
        return redirect(url_for('AuthController:login_page'))