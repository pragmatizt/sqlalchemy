# sqlalchemy
Exploring relationship between sqlite3, sqlalchemy, and .py notebook

# TERMINAL
### After adding a new tower, check on terminal:
- go to your directory
- python db.py
- sqlite3 celltower.db
- select * from tower;
- now see new results.

### To check on existing data within database:
- uncomment the result = [t.towername for t in session.query(Tower).all()] list comprehension
- if you haven't already, comment out the new tower additions, session.add, and session.commits
- run python db.py 
- type result.  Now you should see list of towernames

# WARNING
- If new values are already in DB, it will cause an error.
