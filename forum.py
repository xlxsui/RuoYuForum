import pymysql
from dbconfig import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from auth import login_required

bp = Blueprint('forum', __name__)


# 首页
@bp.route('/')
def index():
    return render_template('forum/Main.html')


@bp.route('/homepage')
def homepage():
    # connect mysql
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute(
        'SELECT *'
        ' FROM post'
        ' ORDER BY Createtime DESC'
    )
    posts = cur.fetchmany(5)
    # 帖子的作者们
    authors = []
    for post in posts:
        cur.execute(
            'SELECT *'
            ' FROM users'
            ' where id = %s', (post[4],)
        )
        authors.append(cur.fetchone())
    db.close()
    # 帖子个数
    length = len(posts)
    return render_template('forum/homepage.html', posts=posts, authors=authors, length=length)


# 广场
@bp.route('/square')
def square():
    return render_template('forum/square.html')


@bp.route('/squarecontent')
def squarecontent():
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute(
        'SELECT *'
        ' FROM post'
        ' ORDER BY Createtime DESC'
    )
    posts = cur.fetchall()
    # 帖子的作者们
    authors = []
    for post in posts:
        cur.execute(
            'SELECT *'
            ' FROM users'
            ' where id = %s', (post[4],)
        )
        authors.append(cur.fetchone())
    db.close()
    # 帖子个数
    length = len(posts)

    return render_template('forum/squarecontent.html', posts=posts, authors=authors, length=length)


# 热映
@bp.route('/hot')
def hot():
    return render_template('forum/hot.html')


@bp.route('/hotcontent')
def hotcontent():
    return render_template('forum/hotcontent.html')


# 即将上映
@bp.route('/show')
def show():
    return render_template('forum/show.html')


@bp.route('/showcontent')
def showcontent():
    return render_template('forum/showcontent.html')
