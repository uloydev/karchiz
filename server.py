from flask import Flask, render_template
from controller import *


class Server:
    @staticmethod
    def run():
        """Fungsi static run digunakan untuk menjalankan server web."""
        # inisiasi Flask framework app
        app = Flask("__main__", static_url_path="/assets", template_folder="frontend/html", static_folder="frontend/assets")
        # set secret key
        app.secret_key = "secret_banget_ini_bro"
        # register controllers
        CustomerController.register(app, route_base='/')
        AuthController.register(app, route_base='/')
        # run app
        app.run(debug=True)
