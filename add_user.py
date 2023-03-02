from db import db_session
from models import User

first_user = User(name='Стас Петров', salary=1000000, email='petrov@example.com')
db_session.add(first_user)
db_session.commit()
