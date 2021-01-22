from application import db
from application.models import User


def init_db():
    
    # Empty Database
    db.reflect()
    db.drop_all()
    db.session.commit()
    db.session.rollback()
    db.create_all()

    # Create New Table Entries 
    u = User(id=5, user="Harrison", university1="The University of Bristol MSc in Computer Science", 
    university2="King's College London BSc in Neuroscience First Class Degree", age=26, skill1="Python", 
    skill2="Java", skill3="Bash", fact="I am a huge history fan and enjoy learning new tech skills!", 
    bio="I founded this company to pass on an essential skillset to the next generation. Programming truly changed my life! Maybe it will change yours.", 
    interests="I love the outdoors. Catch me outside when I'm not glued to my computer.")

    u2 = User(id=2, user="Sam", university1="The University of Brighton BSc in Physics", 
    university2="", age=26, skill1="Python", skill2="Java", 
    skill3="Bash", fact="I'm currently on a worldwide trip having randomly bumped into Harrison in Nicaragua! I'm in New Zealand right now! I'm stuck here as of Coronavirus!", 
    bio="I've been developing now for 5 years. I have loved every moment of it and look forward to teaching the next generation!", interests="DJ and music enthusiast.")
    
    u3 = User(id=3, user="Michael", university1="Imperial College London MEng in Mathematics and Computer Science", 
    university2="", age=21, skill1="Java", skill2="Python", 
    skill3="C", fact="I love the cold weather! I’d preference a ski trip over a holiday on the beach any day.", 
    bio="I believe the world is advancing in computing, everyone should learn to code so what a great time to start learning!", 
    interests="Video games, mathematics and when I finally leave the house, I enjoy hiking and exploring new places.")    
    
    u4 = User(id=4, user="Malina", university1="The University of Manchester in BSc in Computer Science", 
    university2="", age=21, skill1="Java", skill2="Python", 
    skill3="OOP", fact="I used to participate in competitive mathematics when I was young. Now I have a pretty nice collection of medals.", 
    bio="Programming is a great skill to have. Why not start right now?", 
    interests="Playing guitar, practicing yoga and travelling are some of my hobbies.")  

    # Add New Table Entries 
    db.session.add(u)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)

    # Push New Table Entries 
    db.session.commit()


if __name__=="__main__":
    init_db()