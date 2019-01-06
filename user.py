import pymysql, os
from dbconfig import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.utils import secure_filename
from auth import login_required

bp = Blueprint('user', __name__)

# 上传头像相关
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# 个人页面
@bp.route('/user/<int:id>')
@login_required
def personal_page(id):
    return render_template('forum/personalpage.html')


@bp.route('/user/personal_page_content')
@login_required
def personal_page_content():
    return render_template('user/personalpagecontent.html')


# 资料编辑
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

        # deal with avatar
        # check if the form has the file part
        if 'avatar' not in request.files:
            flash('No file part')
        avatar = request.files['avatar']
        # if user does not select file, browser also
        # submit an empty part without filename
        if avatar.filename == '':
            flash('No selected file')

        if avatar and allowed_file(avatar.filename):
            filename = secure_filename(avatar.filename)
            filename = str(g.user[0]) + '.' + filename.rsplit('.', 1)[1].lower()
            avatar.save(os.path.join('''./static/img/avatar''', filename))
            cur.execute('''
                        update users set avatar_url=%s where id = %s
                        ''', ('img/avatar/' + filename, g.user[0])
                        )
            db.commit()

        # 更新g.user
        cur.execute('''
                    select * from users where id = %s
                ''', (g.user[0])
                    )
        g.user = cur.fetchone()
        db.close()
        return render_template('user/personalpagecontent.html')

    return render_template('user/edit.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
