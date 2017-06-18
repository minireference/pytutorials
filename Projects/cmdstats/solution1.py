
import csv
csv_file = open('commands_data.csv', 'r')
csv_lines_raw = csv_file.readlines()
csv_lines_clean = [line for line in csv_lines_raw if len(line.strip()) > 0]
header = csv_lines_clean[0]
csv_data = csv_lines_clean[1:]
csv_reader = csv.reader(csv_data)


# compute total
total = 0
for row in csv_reader:
    if len(row) == 3:
        # print('processing row', row)
        try:
            count = float(row[1])
        except ValueError:
            count = 0
        total += count

print(total)

def get_count_for_cmd(cmd ):
    csv_reader = csv.reader(csv_data)
    for row in csv_reader:
        print(row)
        if row[0] == cmd:
            try:
                count = float(row[1])
            except ValueError:
                count = 0
            return count
    return 0

print( get_count_for_cmd('git')/total )
