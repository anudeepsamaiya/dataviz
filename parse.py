import csv
import sys

SAMPLE_DATA_FILE = 'data/sample_sfpd_incident_all.csv'


def parse(filename, delimiter):
    """Parse csv data and return output
    """
    with open(filename) as data_file:
        csv_data = csv.reader(data_file, delimiter=delimiter)
        fields = csv_data.__next__()
        csv_data = [dict(zip(fields, x)) for x in csv_data]
    return csv_data


def main(filename=None):
    """
    """
    if not filename:
        filename = SAMPLE_DATA_FILE
    parse_data = parse(filename, ',')

    print(parse_data)

if __name__=="__main__":
    if len(sys.argv) > 1:
        for each in sys.argv[1:]:
            main(each)
    else:
        main()

