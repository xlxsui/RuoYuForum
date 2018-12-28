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
    return render_template('forum/movie.html', id=id)
