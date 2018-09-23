from flask import Flask, render_template, request, session, redirect, url_for
#from models import db, User
from forms import SearchForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
#db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/search", methods=["GET", "POST"])
def signup():
  form = SearchForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('search.html', form=form)
    else:
      #newuser = User(form.category.data, form.last_name.data, form.email.data, form.password.data)
      #db.session.add(newuser)
      #db.session.commit()
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('search.html', form=form)

@app.route("/home", methods=["GET", "POST"])
def home():
  return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)