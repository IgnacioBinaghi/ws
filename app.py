from flask import Flask, render_template, request, redirect, url_for, flash
from ppio.push import push_to_db, push_to_db_repeat
from encryption import *
from send_newsubemail import *
from get_user_data import availability
import time

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/',  methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        keyword_1 = request.form.get("keyword_1")
        keyword_2 = request.form.get("keyword_2")
        keyword_3 = request.form.get("keyword_3")
        keyword_4 = request.form.get("keyword_4")
        keyword_5 = request.form.get("keyword_5")

        user_template = {
              "_id" : "1",
              "email": encrypt(email),
              "name" : name,
              "keyword1": keyword_1,
              "keyword2":keyword_2,
              "keyword3": keyword_3,
              "keyword4": keyword_4,
              "keyword5": keyword_5
        }

        if (availability(email)):
            push_to_db_repeat(user_template)
            send_dupesubemail("Your Account Has Been Updated", email)
        else:
            push_to_db(user_template)
            send_newsubemail("Thank You for joining wsAlpha!", email)
        return redirect(url_for('joined'))
    return render_template('index.html')

@app.route('/joined', methods=['GET', 'POST'])
def joined():
    return render_template('joined.html')


if __name__ == "__main__":
    app.run(debug=False)