from flask import Flask, render_template
from models.dbscripts import connection
from models.form import SignupForm


app = Flask(__name__)
app.secret_key = 'rhsdrabsr453756yvw35u'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        return f'Thank you for signing up, {signup_form.username.data}'
    return render_template('views/form.html', signup_form=signup_form)


if __name__ == '__main__':
    app.run(debug=True)
