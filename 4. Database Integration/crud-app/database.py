from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()





'''
A factory in Python is simply a function (ya callable) that creates and returns objects.
It’s a design pattern, not a language feature.

sessionmaker is a special factory in SQLAlchemy – yeh ek configured Session class/factory banata hai.
Yahan sessionmaker(...) se jo configured Session class/factory milti hai,
usko hum SessionLocal naam ke variable me store kar rahe hain.

Session kya hai?
Session is SQLAlchemy’s core class for database interaction:
    • query karna
    • data insert / update / delete
    • transactions commit / rollback
    • session close karna

Ye sab Session object se hota hai,
aur woh Session object hum main.py me banayenge: db = SessionLocal()
'''


'''
autoflush = False
Matlab: Jo bhi changes karte ho (add/update), sirf session ki memory mein rehte hain.
Jab tak aap manually flush() ya commit() nahi karte, database ko SQL nahi bheja jata.

autoflush = True
Matlab: Jaise hi aap query run karte ho, pending changes pehle auto-flush ho jate hain
(INSERT/UPDATE SQL DB ko chala diya jata hai), lekin permanent tab bhi commit() par hi hoga.

autocommit = False
Matlab: Changes tab tak database mein permanently save nahi hote jab tak aap manually commit() nahi karte.

autocommit = True
Matlab: Jaise hi aap koi change karte ho, wo automatically commit ho jata hai
(ye modern SQLAlchemy me generally avoid kiya jata hai).
'''


'''

declarative_base ek function hai jo call hone par dynamic tareeke se ek nayi base class banata hai
aur usko return karta hai, taaki hum Python classes ke through hi database tables define kar saken.
is returned base class ko hum Base naam dete hain, aur models.py me aise inherit karte hain:

eg:
class Employee(Base):
    __tablename__ = "employees"
    ...


'''