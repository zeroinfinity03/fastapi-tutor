from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


Base = declarative_base()





# Sessionmaker se aap database session bana kar queries execute kar sakte ho!
# har ek session me hum operations karte hain DB pe jaise ki add, update, delete, query etc.
# database ka koi bhi operation happens within a particular session. 



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

# Declarative_base: Python classes se hi table define kar sakte ho.







