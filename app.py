from flask import Flask, render_template, flash, redirect, url_for
from models.dbscripts import connection
from models.form import SignupForm


app = Flask(__name__)
app.secret_key = 'rhsdrabsr453756yvw35u'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Thanks for signing up, {form.username.data}!', 'Success')
        return redirect(url_for('home'))
    return render_template('views/form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
