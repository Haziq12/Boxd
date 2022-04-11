from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    itemName = StringField('Item Name', validators=[DataRequired()])
    itemDescription = TextAreaField('Item Description', validators=[DataRequired()])
    submit = SubmitField('Post')