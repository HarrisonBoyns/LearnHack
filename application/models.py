from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), index=True, unique=False)
    university1 = db.Column(db.String(64), index=True, unique=False)
    university2 = db.Column(db.String(64), index=True, unique=False)
    age = db.Column(db.String(64), index=True, unique=False)
    skill1 = db.Column(db.String(64), index=True, unique=False)
    skill2 = db.Column(db.String(64), index=True, unique=False)
    skill3 = db.Column(db.String(64), index=True, unique=False)
    fact = db.Column(db.String(64), index=True, unique=False)
    bio = db.Column(db.String(64), index=True, unique=False)
    interests = db.Column(db.String(64), index=True, unique=False)

    def __init__(self, id, user, university1, university2, age, skill1, skill2, skill3, fact, bio, interests):
        
            self.id = id
            self.user = user
            self.university1 = university1
            self.university2 = university2
            self.age = age
            self.skill1 = skill1
            self.skill2 = skill2
            self.skill3 = skill3
            self.fact = fact
            self.bio = bio
            self.interests = interests


    def __repr__(self):
        return '<User {}>'.format(self.user)  
