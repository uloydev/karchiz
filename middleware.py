from flask import session, redirect, url_for, flash

class Middleware:
    @classmethod
    def authenticated(cls, func):
        def inner(func):
            if not session.get('username'):
                flash('anda harus login untuk mengakses page ini')
                return redirect(url_for('AuthController:login_page'))
            func()
        return inner
                
