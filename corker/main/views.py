from flask import render_template
from . import bp


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')
