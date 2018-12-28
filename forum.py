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
    # connect mysql
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute(
        'SELECT *'
        ' FROM post'
        ' ORDER BY Createtime DESC'
    )
    posts = cur.fetchmany(7 + 10)
    db.close()
    return render_template('forum/Main.html', posts=posts)


@bp.route('/slideshow')
def slideshow():
    return render_template('forum/slideshow.html')


# 创建帖子
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # connect mysql
            db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
            cur = db.cursor()
            cur.execute(
                'INSERT INTO post (Title, Content, UserId)'
                ' VALUES (%s, %s, %s)',
                (title, content, g.user[0])
            )
            db.commit()
            return redirect(url_for('forum.index'))

    return render_template('forum/new.html')


# 编辑帖子
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # connect mysql
            db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
            cur = db.cursor()
            cur.execute(
                'UPDATE post SET Title = ?, Content = ?'
                ' WHERE Post_id = ?',
                (title, content, id)
            )
            db.commit()
            return redirect(url_for('forum.index'))

    return render_template('forum/update.html', post=post)


# 删除帖子
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    # connect mysql
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute('DELETE FROM post WHERE Post_id = ?', (id,))
    db.commit()
    return redirect(url_for('forum.index'))


# 广场
@bp.route('/square')
def square():
    return render_template('forum/square.html')


@bp.route('/squarecontent')
def squarecontent():
    return render_template('forum/squarecontent.html')


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


# 发帖
@bp.route('/post')
@login_required
def post():
    return render_template('forum/post.html')


@bp.route('/postcontent')
def postcontent():
    return render_template('forum/postcontent.html')


# 个人页面

def get_post(id, check_author=True):
    # connect mysql
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute(
        'SELECT *'
        ' FROM post p'
        ' WHERE p.Post_id = ?',
        (id,)
    )
    post = cur.fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post[4] != g.user[0]:
        abort(403)

    return post
