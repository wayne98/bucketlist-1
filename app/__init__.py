# from flask_api import FlaskAPI
# from flask_sqlalchemy import SQLAlchemy

# # local import
# from config import app_config

# # initialize sql-alchemy
# db = SQLAlchemy()

# #This function wraps the creation of a new Flask object,
# #and returns it after it's loaded up with configuration settings 
# def create_app(config_name):
#     app = FlaskAPI(__name__, instance_relative_config=True)
#     app.config.from_object(app_config[config_name])
#     app.config.from_pyfile('config.py')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)

#     return app