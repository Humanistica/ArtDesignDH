from flask import flash
import os


def delete_tmp_content():
    '''
        Remove all files in ./tmp/
    '''
    for f in os.listdir('./tmp/'):
        filename = './tmp/' + f
        os.remove(filename)


def reset_usr_data(data):
    '''
        Empty all user input fields
    '''
    for k in data:
        data[k] = ''
    return data


def check_date_format(date):
    try:
        date = date.split('-')
        year, month, day = date[0], date[1], date[2]
    except Exception:
        flash('Mauvais format de date (aaa-mm-jj)')
        return False
    try:
        if (len(year) != 4 and not isinstance(int(year), int)) or \
           (len(month) != 2 and not isinstance(int(month), int)) or \
           (len(day) != 2 and not isinstance(int(day), int)):
            flash('Erreur date : type incorrect')
            return False
    except Exception:
        return False
    return True


def check_year_format(date):
    try:
        if len(date) < 5 and isinstance(int(date), int):
            return True
        else:
            return False
    except Exception:
        return False


def check_form(usr_data):
    flag = True

    if usr_data['key'] == '':
        flash("Entrez votre clé d'authification publique (public key)")
        flag = False

    if usr_data['keywords'] == '' and usr_data['from'] == '' and \
       usr_data['to'] == '':
        flash('Entrez au moins un champs de requête')
        flag = False

    if usr_data['from'] == '' and len(usr_data['to']) > 0:
        if check_year_format(usr_data['from']) and \
           check_year_format(usr_data['to']):
            flash('Veuillez entrer la borne inférieure')
            flag = False
    elif len(usr_data['from']) > 0 and usr_data['to'] == '':
        if check_year_format(usr_data['from']) and \
           check_year_format(usr_data['to']):
            flash('Veuillez entrer la borne superieur')
            flag = False

    return flag


def parse_query(data):
    base = 'https://www.europeana.eu/api/v2/search.json?wskey='

    query = base + str(data['key'])

    # Keywords
    if len(data['keywords']) > 0:
        keywords = data['keywords'].split(' ')
        q1 = '&query=' + '"' + '+'.join(keywords) + '"'
    else:
        q1 = ''

    return query + q1
