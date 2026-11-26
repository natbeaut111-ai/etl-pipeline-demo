import csv

def extract_data(path="data/input.csv"):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    ## This changes are done to test feature extract branch.
    ## This is second change are done to test feature extract branch.
    return rows
