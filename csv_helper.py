"""
CSV helper functions.
"""
import csv


def read_headers(csv_file):
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        headers = next(csv_reader, None)
    return headers


def read_csv(csv_file, skip_headers=True):
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        if skip_headers:
            next(csv_reader, None)
            rows = []
        else:
            rows = next(csv_reader, None)
        for row in csv_reader:
            rows.append(row)
    return rows


def append_csv(csv_file, row):
    with open(csv_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
