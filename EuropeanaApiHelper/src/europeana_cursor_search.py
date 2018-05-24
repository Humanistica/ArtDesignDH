import os
import csv
import json
import argparse

from unfold import unfold
from pprint import pprint


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='extract all \
                                            items from a collection')
    parser.add_argument('query', type=str, help='Query without \
                                                        cursor indication')
    parser.add_argument('file_path', type=str, help='Output csv filename')
    parser.add_argument('--col', type=str, help='Path to your column file')

    args = parser.parse_args()

    if len(args.query) > 0 and len(args.file_path) > 0:

        cursorMark = '*'
        nextCursor = ''
        items = []

        while(1):

            # Execute command and save data in tmp file
            new_query = '"' + args.query + '&cursor=' + cursorMark + '"'
            cmd = 'curl ' + new_query + ' > tmp.json'
            print('\n\n', cmd, '\n')
            os.system(cmd)
            print('\n\n======================================================')

            # Parse current API response
            with open('tmp.json') as f:
                data = json.load(f)

                try:
                    # Save current items
                    for i in data['items']:
                        items.append(unfold('items', i))

                    # Retrive next markup
                    nextCursor = data['nextCursor']
                    cursorMark = nextCursor

                except KeyError:
                    os.remove('tmp.json')
                    break

        if args.col.endswith('.txt'):
            try:
                with open(args.col) as f:
                    to_keep = [s.rstrip() for s in f]
                    items = [{k: i[k] for k in i if k in to_keep}
                             for i in items]
            except Exception:
                print('\n\n[ ! ] Cannot open', args.col)
                exit()

        print('[ + ] Items found:', len(items))

        # Save data to csv
        with open(args.file_path, 'w') as f:

            header = []
            for i in items:
                for k in i:
                    header.append(k)
            header = list(set(header))

            writer = csv.DictWriter(f, fieldnames=list(header))
            writer.writeheader()
            writer.writerows(items)

            pprint(sorted(header))
