from flask import Flask, render_template
from controller import *


class Server:
    def __init__(self):
        secret_key = "secret_banget_ini_bro"
        self.app = Flask("__main__", static_url_path="/assets", template_folder="frontend/html", static_folder="frontend/assets")
        self.app.secret_key = secret_key

    def run(self):
        CustomerController.register(self.app, route_base='/')
        AuthController.register(self.app, route_base='/')
        self.app.run(debug=True)
