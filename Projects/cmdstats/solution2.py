
import csv
csv_file = open('commands_data.csv', 'r')
csv_lines_raw = csv_file.readlines()
csv_lines_clean = [line for line in csv_lines_raw if len(line.strip()) > 0]
dict_reader = csv.DictReader(csv_lines_clean)


# compute total
total = 0
for datum in dict_reader:
    try:
        count = float(datum['count'])
    except ValueError:
        count = 0
    total += count


def get_count_for_cmd(cmd):
    dict_reader = csv.DictReader(csv_lines_clean)
    for datum in dict_reader:
        if datum['command'] == cmd:
            try:
                count = float(datum['count'])
            except ValueError:
                count = 0
            return count
    return 0

print( get_count_for_cmd('git')/total )
