from flask import Flask, render_template
from controller import *


class Server:
    @staticmethod
    def run():
        app = Flask("__main__", static_url_path="/assets", template_folder="frontend/html", static_folder="frontend/assets")
        app.secret_key = "secret_banget_ini_bro"
        CustomerController.register(app, route_base='/')
        AuthController.register(app, route_base='/')
        app.run(debug=True)
