from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from flask_babel import lazy_gettext as _l
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

class ContactForm(FlaskForm):
	first_name   = StringField  (_l('First Name')     , validators=[] )
	last_name    = StringField  (_l('Last Name')  , validators=[])
	phone	     = StringField  (_l('Phone Number or E-mail')  , validators=[DataRequired()])
	message      = StringField  (_l('Message')     , validators=[])
