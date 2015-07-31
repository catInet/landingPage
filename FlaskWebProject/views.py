"""
Routes and views for the flask application.
"""
import datetime
import config
from flask import render_template, request, url_for
from FlaskWebProject import app
from forms import MessageForm
from azure.storage import TableService


@app.route('/', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        #Save to db
        table_service = TableService(account_name=config.ACC_NAME, 
                                     account_key=config.ACC_KEY)
        message = {'PartitionKey': 'message', 
                   'RowKey': form.name.data + datetime.datetime.now().isoformat(), 
                   'name' : form.name.data,
                   'email': form.email.data,
                   'date' : str(datetime.datetime.now())}
        if form.message_body.data:
            message["message"] = form.message_body.data
        table_service.insert_entity('landingmessages', message)
        return render_template(
            'index.html',
            hiden_block='#wright-us',
            form=form,
        )
    return render_template(
        'index.html',
        hiden_block='#got-ur-message',
        form=form,
    )


