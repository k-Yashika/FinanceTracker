from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import RegistrationForm, LoginForm, TransactionForm
from app.models import User, Transaction
from flask_login import login_user, current_user, logout_user, login_required
import pandas as pd
import plotly.express as px

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account ahs been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() 
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/dashboard")
@login_required
def dashboard():
    form = TransactionForm()
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', title='Dashboard', transactions=transactions, form=form)

@app.route("/transaction/new", methods=['GET', 'POST'])
@login_required
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(amount=form.amount.data, category=form.category.data, date=form.date.data, user_id=current_user.id)
        db.session.add(transaction)
        db.session.commit()
        flash('Your transaction has been added!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_transaction.html', title='New Transaction', form=form)

@app.route('/visualize')
@login_required
def visualize():
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    if transactions:
        df = pd.DataFrame([(t.amount, t.category, t.date) for t in transactions], columns=['Amount', 'Category', 'Date'])
        fig = px.bar(df, x='Date', y='Amount', color ='Category', title='Spending Over Time')
        graph = fig.to_html(full_html=False)
        return render_template('visualize.html', graph=graph)
    else:
        flash('No transactions to visualize', 'warning')
        return redirect(url_for('dashboard'))

