from db import db_session
from models import User

my_user = User.query.first()
my_user.salary = 2000000
db_session.commit()
