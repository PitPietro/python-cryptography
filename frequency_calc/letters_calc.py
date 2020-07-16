import pprint
import csv

count = {}


def count_letters(msg):
    if msg in ['', ' ']:
        msg = 'qwerty'
    for character in msg.lower():
        count.setdefault(character, 0)
        count[character] = count[character] + 1

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
    f_name = 'letters_row.csv'
    with open(f_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for key, value in count.items():
            tmp_list = [key, value]
            csv_writer.writerow(tmp_list)


if __name__ == '__main__':
    message = input('Insert a world or a phrase: ')
    count_letters(message)
    # TODO: save the result in a CSV file (whit the commas)
    # TODO: replace the input whit the reading of a .txt file
    #  (it allows the study of the frequency for a specific cryptography method)
    # TODO: Make a cake diagram from it and display it whit pandas!

    save_to_csv_row()
