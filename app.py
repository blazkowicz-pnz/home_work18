from flask import Flask
from config import Config
from setup_db import db
from flask_restx import Api
from views.movie import ns_movie
from views.genre import ns_genre
from views.director import ns_director



def create_app(config:Config) ->Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    register_extension(app)
    return app


def register_extension(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(ns_movie)
    api.add_namespace(ns_genre)
    api.add_namespace(ns_director)
    # load_data(app, db)


# def load_data(app, db):
#     with app.app_context():
#         m1 = Movie(id=25, title="Mad Monkey", description="cool film", trailer="000", year=1900, rating=3.1, genre_id=3, director_id=3)
#         g1 = Genre(id=22, name="Спорт")
#         d1 = Director(id=23, name="Виталик")
#         with db.session.begin():
#             db.session.add(m1)
#             db.session.add(g1)
#             db.session.add(d1)
#             db.session.commit()


app_config = Config()
app = create_app(app_config)
if __name__ == "__main__":
    app.run()


# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

# from flask import Flask
# from flask_restx import Api
#
# from config import Config
# from models import Review, Book
# from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
# def create_app(config_object):
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     register_extensions(app)
#     return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
# def register_extensions(app):
#     db.init_app(app)
#     api = Api(app)
#     api.add_namespace(...)
#     create_data(app, db)
#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)
