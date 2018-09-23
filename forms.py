from flask_wtf import Form 
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
  category = SelectField('Category', choices = [('1', 'Dairy'), ('2', 'Produce'),('3', 'Fruits'),('4', 'Bevarage')])
  sub_category = SelectField('Sub category', choices=[])
  product = SelectField('Product', choices=[] )
  submit = SubmitField('Check')

