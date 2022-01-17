import sys
import json
import requests

from searching import *


DATASET_FILE_NAME = 'dataset.csv'
RESULT_FILE_NAME = 'matches.json'
GIST_URL = 'https://gist.githubusercontent.com/pseudo-usama/aeab91fca119392b20a83b78871debcd/raw/c98a280a66d52bf091892137cd1b1c37d5644e90/dataset.csv'


def what_to_extract(argv):
    if argv == []:
        sys.exit('Please specify what to extract from file.')

    option = str.lower(argv[0])

    if option == 'emails':
        return extract_emails
    if option == 'numbers':
        return extract_numbers
    if option == 'dates':
        return extract_dates

    exit('Invalid choice. Try again')


def get_dataset(filename):
    # As dataset is big so downloading takes time
    # That's why I've commented downloading from GIST code
    # And just reading from local file
    # return requests.get(GIST_URL, allow_redirects=True).content

    with open(filename, 'r') as f:
        return f.read()


def to_file(data_to_save):
    with open(RESULT_FILE_NAME, 'w') as f:
        json.dump(data_to_save, f, indent=4)


if __name__ == '__main__':
    extraction_fn = what_to_extract(sys.argv[1:])
    dataset = get_dataset(DATASET_FILE_NAME)

    matches = extraction_fn(dataset)
    print(f'Searching completed. Now saving results to ./{RESULT_FILE_NAME}')
    to_file(matches)
