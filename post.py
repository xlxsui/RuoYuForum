import pymysql
from dbconfig import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from auth import login_required

bp = Blueprint('post', __name__)


@bp.route('/post_details/<int:id>', methods=['GET', 'POST'])
def post_details(id):
    # 先把帖子拿出来再说
    db = pymysql.connect('localhost', DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute('''
        select * from post where Post_id = %s
        ''', (id,))
    post = cur.fetchone()
    db.close()

    if request.method == 'POST':
        if g.user:
            # 处理新的回复
            comment = request.form['comment']
            # connect to database
            db = pymysql.connect('localhost', DBUser, DBPassword, DBName)
            cur = db.cursor()
            cur.execute('''
                insert into comment(user_id,author_id,Content,post_id) values (%s,%s,%s,%s)
                ''', (g.user[0], post[4], comment, id))
            db.commit()
            db.close()
            return redirect(url_for('post.post_details', id=id))
        else:
            return render_template('redirect_template.html', url=url_for('auth.login'))

    # comments
    db = pymysql.connect('localhost', DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute('''
        select * from comment where post_id=%s order by Creatime desc 
        ''', (id,))
    comments = cur.fetchall()

    # repliers
    repliers = []
    for comment in comments:
        cur.execute('''
            select * from users where id=%s
            ''', (comment[0]))
        repliers.append(cur.fetchone())

    comments_length = len(repliers)

    db.close()
    return render_template('post/post_details.html', post=post, comments=comments, repliers=repliers,
                           comments_length=comments_length)


# 发帖
@bp.route('/post')
@login_required
def post():
    return render_template('forum/post.html')


@bp.route('/postcontent', methods=['GET', 'POST'])
@login_required
def postcontent():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        db = pymysql.connect('localhost', DBUser, DBPassword, DBName)
        cur = db.cursor()
        cur.execute('''
        insert into post(Title,Content,UserId) values (%s,%s,%s)         
        ''', (title, content, g.user[0]))
        db.commit()
        db.close()
        return redirect(url_for('forum.squarecontent'))

    return render_template('forum/postcontent.html')
