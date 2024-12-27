import string


def open_file(file_path):
    try:
        return open(file_path, 'r+')
    except FileNotFoundError:
        print(f'{file_path} was not found')
        return None


def read_file(file):
    return file.readlines()


def write_lines_to_file(file, lines):
    file.seek(0)
    file.writelines(lines)
    file.truncate()


def close_file(file):
    file.close()


def remove_equal_lines(lines):
    unique_lines = list(dict.fromkeys(lines))
    return unique_lines


def find_words_with_particular_length(file, n):
    words = file.split()
    words_without_punctuation = [word.strip(string.punctuation) for word in words]
    a = []
    for word in words_without_punctuation:
        if (len(word) == n):
            a.append(word)
    return a


def write_to_file(content, path):
    with open(path, 'w') as c:
        c.write(content)


def combine_two_files(file_1, file_2, result_file):
    file_3 = file_1 + "\n" + file_2
    write_to_file(file_3, result_file)


# Task 1: Read the file and remove equal lines (if any).
file = open_file('London is the capital of Great Britain.txt')
lines = read_file(file)
new_lines = remove_equal_lines(lines)
write_lines_to_file(file, new_lines)
close_file(file)

# Task 2: print out all words with length of n-characters
file = open_file('London is the capital of Great Britain.txt').read()
list_of_words = find_words_with_particular_length(file, 5)
print(list_of_words)

# Task 3: Combine two files into a third file
file_london = open_file('London is the capital of Great Britain.txt').read()
file_rome = open_file('What is the Capital of Italy.txt').read()
result_file = 'London + Rome.txt'
combine_two_files(file_london, file_rome, result_file)
