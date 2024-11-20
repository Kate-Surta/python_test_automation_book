import re

# Define if a string contains the required characters. E.g. if '7865serS3'
initial_string = '7865serS3'
case_1 = '583'
case_2 = '973'


def if_string_contains_characters(characters, full_string):
    for char in characters:
        if re.search(re.escape(char), full_string):
            continue
        else:
            print(f'{characters} does not exist in {full_string}')
            return
    print(f'{characters} exists in {full_string}')


# includes '583' - True; '973' - False
if_string_contains_characters(case_1, initial_string)
if_string_contains_characters(case_2, initial_string)

# 2 Count a number of Upper case letters in the string. E.g. '7865serS3' - 'Number of Capital letters: 1'
initial_string = '7865serS3'


def count_upper_case_letters(string):
    letters = re.findall(r'[A-Z]', string)
    return len(letters)


n = count_upper_case_letters(initial_string)
print(f'Number of Upper case letters is {n}')

# 3 Define if the string contains at least one Upper case letter followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;

case_1 = '75serS3'
case_2 = '75WseTrS3'


def contains_upper_followed_by_lower(string):
    pattern = r'[A-Z][a-z]+'
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False


if contains_upper_followed_by_lower(case_2):
    print('passed')
else:
    print('failed')
