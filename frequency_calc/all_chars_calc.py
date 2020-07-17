import pprint
import csv

count = {}


def count_letters(msg):
    if msg in ['', ' ']:
        msg = read_txt_file()
    for character in msg.lower():
        print(character)
        if character == ',':
            count.setdefault('comma', 0)
            count['comma'] += 1
        elif character == ';':
            count.setdefault('semicolon', 0)
            count['semicolon'] += 1
        elif character == '.':
            count.setdefault('dot', 0)
            count['dot'] += 1
        elif character == ':':
            count.setdefault('colon', 0)
            count['colon'] += 1
        elif character == '"':
            count.setdefault('quotes', 0)
            count['quotes'] += 1
        elif character == ' ':
            count.setdefault('space', 0)
            count['space'] += 1
        else:
            count.setdefault(character, 0)
            count[character] += 1

    final_dict = pprint.pformat(count)
    print(final_dict)


"""
The file will be as follow:
key_1, value_1
key_2, value_2
key_3, value_3
key_4, value_4
...

"""


def save_to_csv_row():
    f_name = '../test_files/svg_files/letters_row.csv'
    with open(f_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for key, value in count.items():
            tmp_list = [key, value]
            csv_writer.writerow(tmp_list)


"""
The file will be as follow:
key_1, key_2, key_3, key_4
value_1, value_2, value_3, value_4
...

"""


def save_to_csv_columns():
    f_name = '../test_files/svg_files/letters_columns.csv'
    with open(f_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(count.keys())
        csv_writer.writerow(count.values())


"""
Modes:
r - (default mode) open the file for reading
w - open the file for writing, overwriting the content if the file already exists with data
x - creates a new file, failing if it exists
a - open the file for writing, appending new data at the end of the file's contents if it already exists
b - write binary data to files instead of the default text data
+ - allow reading and writing to a mode

"""


def read_txt_file():
    my_data = open('../test_files/txt_files/an_unexpected_party.txt', 'r')
    return my_data.read()


if __name__ == '__main__':
    message = input('Insert a world or a phrase: ')
    count_letters(message)
    save_to_csv_row()
    save_to_csv_columns()
