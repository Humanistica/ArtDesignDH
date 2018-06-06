#!flask/bin/python
from flask import Flask, render_template, request, Response

from api_caller import execute_query
from data_manager import check_form, parse_query, reset_usr_data, \
    delete_tmp_content


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
    delete_tmp_content()
    return render_template('index.html', usr=usr_data)


@app.route('/', methods=['POST'])
def get_request_infos():
    global usr_data
    global items

    # Retrieve usr data and store it global variables
    for key in usr_data:
        usr_data[key] = request.form[key].rstrip()
    for key in filters:
        filters[key] = request.form[key].rstrip()

    if check_form(usr_data) is True:

        # Check date formats
        dates = [usr_data['from'], usr_data['to']]
        if dates == ['', '']:
            dates = None

        # Parse query with usr values
        query = parse_query(usr_data)

        # Execute curl + usr query
        items = execute_query(query, filters, dates)

        # Check if any items in collection
        if items is None:
            return no_result_page()
        else:
            usr_data = reset_usr_data(usr_data)
            return result_page()
    else:
        return index()


@app.route('/result')
def result_page():
    return render_template('result.html', items=items, len=len(items))


@app.route('/no_result')
def no_result_page():
    return render_template('no_result.html')


@app.route('/return-csv-file')
def return_csv_file():
    with open('./tmp/output.csv') as f:
        data = f.read()
    return Response(
        data,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=europeana_data.csv"})


@app.route('/return-json-file')
def return_json_file():
    with open('./tmp/output.json') as f:
        data = f.read()
    return Response(
        data,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=europeana_data.json"})


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
