from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
# Declarative_base: Python classes se hi table define kar sakte ho.
# Base ek common parent class hai – isse inherit karke hum apne ORM models / tables define karte hain.






'''
A factory in Python is simply a function (ya callable) that creates and returns objects. It’s a design pattern, not a language feature.

# sessionmaker is a special factory in SQLAlchemy – it creates a { configured Session class } for us.
# Yahan sessionmaker(...) se jo configured Session class/factory milti hai, usko hum SessionLocal naam de rahe hain.

Session kya hai?
Session is SQLAlchemy’s core class for database interaction:
	•	query karna
	•	data insert / update / delete
	•	transactions commit / rollback
	•	session close karna

Ye sab Session object se hota hai and we will make that object in main.py like: db = SessionLocal()

'''




'''
autoflush = False
Matlab: Jo bhi changes karte ho (add/update), sirf memory mein rehte hain, database mein nahi jate.
Jab tak aap manually flush() ya commit() nahi karte, database mein kuch nahi hota.
autoflush = True
Matlab: Jaise hi aap query run karte ho, changes database mein reflect ho jate hain (temporary), lekin save nahi hote.
Changes dikhte hain, par permanent nahi hote jab tak commit() nahi karte.
autocommit = False
Matlab: Changes tab tak database mein permanently save nahi hote jab tak aap manually commit() nahi karte.
autocommit = True
Matlab: Jaise hi aap koi change karte ho, wo automatically save (commit) ho jata hai.
'''









