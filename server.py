import pymysql
from flask import Flask, render_template
from config import Config
from model import UserModel
from controller import *


class Server:
    def __init__(self):
        self.app = Flask("__main__", static_url_path="/assets", template_folder="frontend/html", static_folder="frontend/assets")
        
        config = Config().get()
        self.mysql = pymysql.connect(**config)

        

    def run(self):
        CustomerController.register(self.app, route_base='/')
        AuthController.register(self.app, route_base='/')
        self.app.run()
