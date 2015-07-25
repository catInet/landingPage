from wtforms import Form
from wtforms import TextField
from wtforms.validators import Required

class MessageForm(Form):
    name = TextField('name', validators = [Required()])
    email = TextField('email', validators = [Required()])
    message_body = TextField('query')
