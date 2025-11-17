from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()





'''
What is a factory in Python?
A factory is any callable (function or class) that creates and returns objects. 
It's a design pattern, not a language feature.

sessionmaker is a special Session factory (a callable) in SQLAlchemy.
{We will see what is Session in a bit.}
Since its a Session factory, we call it to get Session objects.

When we call SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False),
it returns a configured Session factory object (built from the Session class), and we store that in SessionLocal.
Later, when we call db = SessionLocal(), it creates a new Session object (db).



Session class kya hai?
Session is SQLAlchemy ka core class for database interaction:
    • query karna
    • data insert / update / delete
    • transactions commit / rollback
    • session close karna

Ye sab Session object se hota hai,
aur woh Session object hum main.py me banayenge: db = SessionLocal()
Aur phir isi db object ko apne API endpoints me use karke database se interact karenge.
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


'''
1. databse
2. models
3. schemas
4. crud
5. main
'''