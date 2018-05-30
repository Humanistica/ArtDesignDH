#!flask/bin/python
from flask import Flask, render_template, request, send_file

from api_caller import execute_query
from data_manager import check_form, parse_query, reset_usr_data


SESSION_TYPE = 'memcache'

app = Flask(__name__)

filters = {'items_type': '',
           'items_dataProvider': ''}

items = None
usr_data = {'key': '',
            'creator': '',
            'date': '',
            'items_type': '',
            'items_dataProvider': '',
            'keywords': '',
            'from': '',
            'to': ''
            }


@app.route('/')
def index():
    return render_template('index.html', usr=usr_data)


@app.route('/', methods=['POST'])
def get_request_infos():
    global usr_data
    global items

    for key in usr_data:
        usr_data[key] = request.form[key].rstrip()

    for key in filters:
        filters[key] = request.form[key].rstrip()

    if check_form(usr_data) is True:
        query = parse_query(usr_data)
        items = execute_query(query, filters)
        usr_data = reset_usr_data(usr_data)
        return result_page()
    else:
        return index()


@app.route('/result')
def result_page():
    return render_template('result.html', items=items, len=len(items))


@app.route('/return-file/')
def return_file():
    return send_file('./tmp/output.csv',
                     attachment_filename='europeana_api_data.csv')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
