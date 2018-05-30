import os
import csv
import json
import copy

from unfold import unfold

labels = ['items_id', 'items_title', 'items_country', 'items_dataProvider',
          'items_type', 'items_edmTimespanLabelLangAware_def',
          'items_dcCreator', 'items_edmPreview']


def clean_list(value):
    if isinstance(value, list):
        return ' '.join(value)
    else:
        return value


def filter(items, filters):
    new_items = [copy.deepcopy(i) for i in items]
    to_remove = []
    for i in range(len(items)):
        for f in filters:
            if len(filters[f]) > 0 and filters[f] != items[i][f]:
                to_remove.append(items[i])

    for i in to_remove:
        new_items.remove(i)

    return new_items


def parse_date(items):
    new_items = []

    for i in items:
        try:
            date = i['items_edmTimespanLabelLangAware_def']
            date = date.split(' ')[0]
            print(i['items_edmTimespanLabelLangAware_def'], '-->', date)

        except KeyError:
            date = '-1'

        new_item = copy.deepcopy(i)
        new_item.update({'items_edmTimespanLabelLangAware_def': date})

        new_items.append(new_item)

    return new_items


def filter_dates(items, dates):
    new_items = [copy.deepcopy(i) for i in items]
    to_remove = []

    date_from, date_to = dates[0], dates[1]

    for i in items:
        c_date = i['items_edmTimespanLabelLangAware_def']

        if c_date[-2:] == '..':
            print('je passe 1')
            new_c_date = c_date[:-2] + '00'
            new_c_date = int(new_c_date)
            if int(new_c_date) < int(date_from) or int(new_c_date) > int(date_to):
                print(c_date, '-->', date_from, date_to)
                to_remove.append(i)
        elif c_date == -1:
            to_remove.append(i)
            print('je passe 2')
        else:
            print('je passe 3')
            print(c_date)
            if int(c_date) < int(date_from) or int(c_date) > int(date_to):
                print(c_date, '-->', date_from, date_to)
                to_remove.append(i)

    for i in to_remove:
        new_items.remove(i)

    return new_items


def execute_query(query, filters, dates):

    cursorMark = '*'
    nextCursor = ''
    items = []

    while(1):

        # Execute command and save data in tmp file
        cmd = 'curl ' + '"' + query + '&cursor=' + cursorMark + '"' + \
              ' > tmp/tmp.json'
        print('\n\n', cmd, '\n')
        os.system(cmd)
        print('\n\n======================================================')

        try:
            # Parse current API response
            with open('tmp/tmp.json') as f:
                data = json.load(f)

                try:
                    # Save current items
                    for i in data['items']:
                        items.append(unfold('items', i))

                    # Retrive next markup
                    nextCursor = data['nextCursor']
                    cursorMark = nextCursor

                except KeyError:
                    os.remove('./tmp/tmp.json')
                    break
        except json.decoder.JSONDecodeError:
            return 0

    # Write true csv
    with open('tmp/true.csv', 'w') as f:
        header = []
        for i in items:
            for k in i:
                header.append(k)
        header = list(set(header))
        writer = csv.DictWriter(f, fieldnames=list(header))
        writer.writeheader()
        writer.writerows(items)

    # Filter items
    items = [{k: clean_list(i[k]) for k in i if k in labels} for i in items]
    items = parse_date(items)
    if dates is not None:
        items = filter_dates(items, dates)
    items = filter(items, filters)
    print('[ + ] Items found:', len(items))

    for i in items[-1]:
        print(i, ' : ', items[-1][i])

    # Save data to csv
    with open('./tmp/output.csv', 'w') as f:

        header = []
        for i in items:
            for k in i:
                header.append(k)
        header = list(set(header))

        writer = csv.DictWriter(f, fieldnames=list(header))
        writer.writeheader()
        writer.writerows(items)

    return items
