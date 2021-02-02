from application import application, mail
from flask import render_template, url_for, request,redirect, flash
from flask_mail import Message
from application.forms import EmailClass
from application.decorators import asynchronous
from application.models import User

@asynchronous
def send_async_email(application, msg):

    with application.app_context():
        mail.send(msg)
 
@application.route("/contact", methods=["GET", "POST"])
def contact():
    
    form = EmailClass()

    if form.validate_on_submit():

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["number"]
        text_body = request.form["msg"]

        msg = Message(subject="Lesson", sender="LearnHackTutoring@gmail.com", recipients=["LearnHackTutoring@gmail.com"])
        msg.body = text_body + "You have received a new mail from {name}.\n\n{number}\n\n<{email}>".format(phone, email, name)
 
        send_async_email(application, msg)

        flash("The email was recieved! We will respond ASAP!")
        return render_template("index.html")
    return render_template("contact.html", form=form)   

@application.route("/hackers/<user>", methods=["GET"])
def user(user):
    user = User.query.filter_by(user=user).first()
    return render_template("user.html", user=user.user, bio=user.bio, university1=user.university1, university2=user.university2, skill1=user.skill1, skills2=user.skill2, skills3=user.skill3, fact=user.fact, interests=user.interests)   

@application.route("/faq", methods=["GET"])
def questions():

    return render_template("studentQuestion.html")   

@application.route("/learnhack/sitemap", methods=["GET"])
def sitemap():

    return render_template("sitemap.html")  

@application.route("/hackerfaq", methods=["GET"])
def hackerfaq():

    return render_template("hackerQuestion.html")  

@application.route("/about", methods=["GET"])
def about():
    return render_template("about.html")   

@application.route("/career", methods=["GET"])
def career():

    return render_template("career.html")   

@application.route("/hackers", methods=["GET"])
def hackers():
    users = User.query.all()
    return render_template("hackers.html", users=users) 

@application.route("/", methods=["GET"])
@application.route("/home", methods=["GET"])
def homeHype():

    return render_template("index.html") 

@application.route("/", methods=["GET"])
@application.route("/admin", methods=["GET"])
def admin():

    return render_template("admin.html") 

@application.route("/costs", methods=["GET"])
def cost():

    return render_template("costs.html") 


@application.errorhandler(404)
def fileNotFound(e):

    return (render_template("404.html"), 404)

@application.errorhandler(404)
def serverError(e):
    
    return (render_template("505.html"), 505)