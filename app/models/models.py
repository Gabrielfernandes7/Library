from database import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(1000))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User: {self.name}"

class Book(db.Model):
    __tablename__ = "book"
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))

    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return f"Title Book: {self.title}"
