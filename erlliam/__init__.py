from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from .views import test
    app.register_blueprint(test.bp, url_prefix='/')

    @app.errorhandler(404)
    def page_not_found(error):
        return error

    return app


