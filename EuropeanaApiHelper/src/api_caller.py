import os
import csv
import json
import copy

from unfold import unfold

labels = ['items_id', 'items_title', 'items_country', 'items_dataProvider',
          'items_type']


def clean_list(value):
    if isinstance(value, list):
        return ' '.join(value)
    else:
        return value


def filter(items, filters):
    new_items = [copy.deepcopy(i) for i in items]
    to_remove = []
    for i in range(len(items)):
        print(len(new_items))
        for f in filters:
            if len(filters[f]) > 0 and filters[f] != items[i][f]:
                to_remove.append(items[i])

    for i in to_remove:
        new_items.remove(i)

    return new_items


def execute_query(query, filters):

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

    # Choose labels
    for k in items[-1]:
        print(k)
    items = [{k: clean_list(i[k]) for k in i if k in labels} for i in items]
    items = filter(items, filters)
    print('[ + ] Items found:', len(items))

    for k in items[-1]:
        print(k)

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
