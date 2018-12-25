import pymysql
from dbconfig import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort
from auth import login_required

bp = Blueprint('forum', __name__)


@bp.route('/')
def index():
    # connect mysql
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    )
    posts = cur.fetchall()
    db.close()
    return render_template('forum/Main.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # connect mysql
            db = pymysql.connect("localhost", "root", "154202", "jin")
            cur = db.cursor()
            cur.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('forum.index'))

    return render_template('forum/create.html')


def get_post(id, check_author=True):
    # connect mysql
    db = pymysql.connect("localhost", "root", "154202", "jin")
    cur = db.cursor()
    post = cur.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # connect mysql
            db = pymysql.connect("localhost", "root", "154202", "jin")
            cur = db.cursor()
            cur.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('forum.index'))

    return render_template('forum/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    # connect mysql
    db = pymysql.connect("localhost", "root", "154202", "jin")
    cur = db.cursor()
    cur.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('forum.index'))
