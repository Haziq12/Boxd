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

@items.route('/<int:item_id>')
def item(item_id):
  item = Item.query.get_or_404(item_id)
  return render_template('item.html', date=item.date, itemName=item.itemName, itemDescription=item.itemDescription, price=item.price, condition=item.condition, size=item.size, contactInfo=item.contactInfo, category=item.category)

@items.route('/<int:item_id>/update', methods=['GET', 'POST'])
@login_required
def update(item_id):
  item = Item.query.get_or_404(item_id)

  if item.author != current_user:
    abort(403)

  form = ItemForm()

  if form.validate_on_submit():
    item.itemName=form.itemName.data
    item.itemDescription=form.itemDescription.data
    item.price=form.price.data
    item.condition=form.condition.data
    item.size=form.size.data
    item.contactInfo=form.contactInfo.data
    item.category=form.category.data
    db.session.commit()
    flash('Item Updated')
    return redirect(url_for('items.item', item_id=item.id))

  elif request.method == 'GET':
    form.itemName.data=item.itemName
    form.itemDescription.data=item.itemDescription
    form.price.data=item.price
    form.condition.data=item.condition
    form.size.data=item.size
    form.contactInfo.data=item.contactInfo
    form.category.data=item.category

  return render_template('create_item.html', title='Updating', form=form) 