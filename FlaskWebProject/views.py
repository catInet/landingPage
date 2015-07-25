"""
Routes and views for the flask application.
"""
import datetime
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
        table_service = TableService(account_name='kotinternet', 
                                     account_key='IBUYL+wZCeSOXxl9k8Z11QmCo6XZexbImsMzZW2IQL/ngfyAM+pfFENNz+T8/m8c3Dx0+lgprqnf6g4jfj75iw==')
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


