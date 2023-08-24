from database import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User: {self.name}"

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))

    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return f"Title Book: {self.title}"

class Rent(db.Model):
    __tablename__ = "rent"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_rent = db.Column(db.Date)

    # Object (join)
    user = db.relationship('User', foreign_keys=user_id)
    book = db.relationship('Book', foreign_keys=book_id)

    def __init__(self, user_id, book_id, date_rent):
        self.user_id = user_id
        self.book_id = book_id
        self.date_rent = date_rent

    def __repr__(self):
        return f"Rent {self.id} - {self.user.name} - {self.book.title}"
