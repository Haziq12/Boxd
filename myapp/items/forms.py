from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FloatField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    itemName = StringField('Item Name', validators=[DataRequired()])
    itemDescription = TextAreaField('Item Description', validators=[DataRequired()])
    price = FloatField('Price (please enter a number', validators=[DataRequired()])
    condition = TextAreaField('Condition', validators=[DataRequired()])
    size = SelectField('Size', choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')])
    contactInfo = TextAreaField('Contact Info', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Mens Clothes', 'Mens Clothes'), ('Womens Clothes', 'Womens Clothes'), ('Appliances', 'Appliances'), ('Other', 'Other')])
    submit = SubmitField('Post')