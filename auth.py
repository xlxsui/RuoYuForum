import functools, pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash
from dbconfig import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view


@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['nikeName']
        password = request.form['password']
        password1 = request.form['password1']
        email = request.form['email']
        error = None

        # 打开数据库连接
        db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cur = db.cursor()

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not password1:
            error = 'Password is required.'
        elif password != password1:
            error = 'Password mismatch！'
        elif not email:
            error = 'Email is required.'

        if cur.execute('select * from users where email = %s', (email,)) > 0:
            error = 'User is existed.'

        if error is None:
            cur.execute(
                'insert into users (nick_name,pw,email) values (%s,%s,%s)',
                (username, generate_password_hash(password), email)
            )
            db.commit()
            # disconnect mysql
            db.close()
            return redirect(url_for('auth.login'))
        flash(error)

    return render_template('auth/signUp.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        global pw_hash

        error = None
        # 打开数据库连接
        db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
        cur = db.cursor()
        cur.execute(
            'SELECT * FROM users WHERE email = %s', (email,)
        )
        user = cur.fetchone()
        db.close()
        if user is not None:
            pw_hash = user[3]

        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(pw_hash, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['email'] = user[1]  # the second column
            return redirect(url_for('index'))
        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# 已经登陆
@bp.before_app_request
def load_logged_in_user():
    if 'email' not in session:
        g.user = None
    else:
        # 打开数据库连接
        db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
        cur = db.cursor()
        cur.execute(
            'select * from users where email = %s', session['email']
        )
        g.user = cur.fetchone()
        db.close()
