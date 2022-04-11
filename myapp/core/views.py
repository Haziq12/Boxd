# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Item 

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page=request.args.get('page', 1, type=int)
    items = Item.query.order_by(Item.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', items=items) 
    
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('info.html')