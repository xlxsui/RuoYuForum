import pymysql
from dbconfig import *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from auth import login_required

bp = Blueprint('movie', __name__)


@bp.route('/movie/<int:id>')
def movie(id):
    db = pymysql.connect("localhost", DBUser, DBPassword, DBName)
    cur = db.cursor()
    cur.execute(
        'SELECT *'
        ' FROM movie'
        ' where movie_id=%s', (id,)
    )
    movie = cur.fetchone()
    db.close()
    return render_template('forum/movie.html', movie=movie)
