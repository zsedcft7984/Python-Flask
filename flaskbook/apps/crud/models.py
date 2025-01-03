from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

#db.Model을 상혹한 User 클래스를 작성한다
class User(db.Model):
    #테이블 명을 지정한다
    __tablename__ = "users"
    #칼럼을 정의한다
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column (db.String, index = True)
    email = db.Column(db.String, unique = True , index = True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )

    #사용자가 password 속성을 조회하려하면, 에러를 발생시킬레  일종의 getter
    #비밀번호를 설정하기 위한 프로퍼티
    @property
    def password(self):
        raise ArithmeticError("읽어 들일 수 없음")
    '''
    사용자가 password 라는 속성명을 갱신하려고 할때,
    나는 그 값을 받아서 암호화 (generater_password_hash)를
    한 차례 수행한 다음 password_hash 속성에 이를 저장
    '''


    #비밀번호를 서정하기 위해 setter함수로 해시화 한 비밀번호를 설정(사용) 한다
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)