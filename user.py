import pymysql
from dbconfig import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from auth import login_required

bp = Blueprint('user', __name__)


@bp.route('/user/<int:id>')
@login_required
def personal_page(id):
    return render_template('forum/personalpage.html')


@bp.route('/user/personal_page_content')
@login_required
def personal_page_content():
    return render_template('user/personalpagecontent.html')


@bp.route('/user/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        nickname = request.form['nickname']
        signature = request.form['signature']
        db = pymysql.connect('localhost', DBUser, DBPassword, DBName)
        cur = db.cursor()
        cur.execute('''
            update users set nick_name=%s,signature = %s where id = %s
            ''', (nickname, signature, g.user[0])
                    )
        db.commit()
        cur.execute('''
            select * from users where id = %s
        ''', (g.user[0])
                    )
        g.user = cur.fetchone()
        db.close()

        return render_template('user/personalpagecontent.html')

    return render_template('user/edit.html')
