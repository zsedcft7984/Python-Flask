from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy를 인스턴스 화한다
db = SQLAlchemy()

#create_app 함수를 작성한다
def create_app():
    #플라스크 인스턴스 생성
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "7984",
        SQLALCHEMY_DATABASE_URI ="sqlite:///"
        +str(Path(Path(__file__).parent.parent, 'local.sqlite')),
        SQLALCHEMY_TRACK_MODIFICATIIONS=False
    )
    #SQLAlchemy와 앱을 연계 한다
    db.init_app(app)
    #Migrate(app, db)
    Migrate(app, db)
    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views

    #register_blueprint를 사용햐 views의 crud를 앱에 등록한다
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
