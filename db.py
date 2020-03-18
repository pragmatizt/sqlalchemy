from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create our engine, link it to our database
engine = create_engine("sqlite:///celltower.db")
# from pdb import set_trace; set_trace() # This is a debugger.
# Above checks it -- this was our output on terminal:
# Engine(sqlite:///celltower.db)


session = sessionmaker(bind=engine)()

Base = declarative_base()

# Define the tower table in sqllite
class Tower(Base):
    __tablename__ = "tower"  

    towername = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, towername, password):
        self.towername = towername
        self.password = password

# =====================================
# tower = Tower('zoom_video_tower', 'password123')

# session.add(tower)

# session.commit()
# =====================================

# Let's say we want to get usernames of all users in database.
result = [t.towername for t in session.query(Tower).all()]
from pdb import set_trace; set_trace()  # debugger
