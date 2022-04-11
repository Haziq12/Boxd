from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FloatField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    itemName = StringField('Item Name', validators=[DataRequired()])
    itemDescription = TextAreaField('Item Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    condition = TextAreaField('Condition', validators=[DataRequired()])
    size = SelectField('Size', choices=[('XS'), ('S'), ('M'), ('L'), ('XL')])
    contactInfo = TextAreaField('Contact Info', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Mens Clothes'), ('Womens Clothes'), ('Appliances'), ('Other')])
    submit = SubmitField('Post')