import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object('config.DevelopmentConfig')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    engine = db.create_engine(f'{app.config["SQLALCHEMY_DATABASE_URI"]}', {})

    with engine.connect():
        db.create_all(app=app)

    @app.route('/')
    def sanity():
        return 'sanity check', 200

    from . import jobs
    app.register_blueprint(jobs.bp)

    from priority_queue_web_api.exceptions import ApiValidationException, ApiUnprocessableException
    app.register_error_handler(ApiValidationException, 422)
    app.register_error_handler(ApiUnprocessableException, 422)
        
    return app
