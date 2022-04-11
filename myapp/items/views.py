from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Item
from myapp.items.forms import ItemForm

items = Blueprint('items', __name__)

@items.route('/create', methods=['GET', 'POST'])
@login_required
def create_item():
  form = ItemForm()
  if form.validate_on_submit():
    item = Item(itemName=form.itemName.data, itemDescription=form.itemDescription.data, price=form.price.data, condition=form.condition.data, size=form.size.data, contactInfo=form.contactInfo.data, category=form.category.data)
    db.session.add(item)
    db.session.commit()
    flash('ITEM CREATED') 
    print('Item was created')
    return redirect(url_for('core.index'))
  return render_template('create_item.html', form=form)