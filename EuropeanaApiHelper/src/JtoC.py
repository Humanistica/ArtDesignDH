import json
import csv
import argparse

from unfold import unfold


def json_to_csv(json_path):
    '''
        Turns json file to csv
    '''
    csv_path = json_path[:-4] + 'csv'

    with open(json_path) as f:
        unfolded = []
        header = set()
        items = json.load(f)['items']

        for i in items:
            # unfold row
            row = unfold('item', i)
            unfolded.append(row)

            # Update header
            header.update(list(row.keys()))

    # Write data to csv
    with open(csv_path, 'w') as f:
        header = list(header)
        writer = csv.DictWriter(f, fieldnames=header)

        writer.writeheader()
        writer.writerows(unfolded)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a europeana \
                                                 json file to csv')
    parser.add_argument('json_path', type=str, help='path to your json file')
    args = parser.parse_args()

    if args.json_path.endswith('.json'):
        json_path = args.json_path
        json_to_csv(json_path)
