#!flask/bin/python
import csv

from flask import Flask, render_template, request, Response

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
        dates = [usr_data['from'], usr_data['to']]
        if dates == ['', '']:
            dates = None
        query = parse_query(usr_data)
        items = execute_query(query, filters, dates)
        usr_data = reset_usr_data(usr_data)
        return result_page()
    else:
        return index()


@app.route('/result')
def result_page():
    return render_template('result.html', items=items, len=len(items))


@app.route('/return-file')
def return_file():
    with open('./tmp/output.csv') as f:
        data = f.read()
    return Response(
        data,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=europeana_data.csv"})


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
