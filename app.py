from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Uploads folder
uploads_dir = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# =====================
# FAVORITES TABLE (FIX)
# =====================
favorites = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('property_id', db.Integer, db.ForeignKey('property.id'))
)

# =====================
# MODELS
# =====================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    properties = db.relationship('Property', backref='owner', lazy=True)

    favorites = db.relationship(
        'Property',
        secondary=favorites,
        backref='favorited_by'
    )

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    price = db.Column(db.Integer)
    location = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    message = db.Column(db.Text)

# =====================
# LOGIN
# =====================

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# =====================
# ROUTES
# =====================

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("view_properties"))  # FIXED
    return render_template("login.html")

@app.route("/properties")
@login_required
def view_properties():
    properties = Property.query.all()
    return render_template("view_properties.html", properties=properties)

@app.route("/add-property", methods=["GET", "POST"])
@login_required
def add_property():
    if request.method == "POST":
        prop = Property(
            title=request.form["title"],
            price=request.form["price"],
            location=request.form["location"],
            user_id=current_user.id
        )
        db.session.add(prop)
        db.session.commit()
        return redirect(url_for("view_properties"))
    return render_template("add_property.html")

@app.route("/toggle-favorite/<int:property_id>", methods=["POST"])
@login_required
def toggle_favorite(property_id):
    prop = Property.query.get_or_404(property_id)
    if prop in current_user.favorites:
        current_user.favorites.remove(prop)
    else:
        current_user.favorites.append(prop)
    db.session.commit()
    return redirect(url_for("view_properties"))

@app.route("/favorites")
@login_required
def favorites_page():
    return render_template("favorites.html", properties=current_user.favorites)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# =====================
# MAIN
# =====================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=False)
