from CCI import Historian

db = Historian.db()
db.open() # 연결
if not db.login('',''):
    db.login('', '')

