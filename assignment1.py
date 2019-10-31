from string import punctuation


# open and read file
def read_file(filename):
    with open(filename, 'r') as f:
        s = f.read()
        return s


# adds tokens to dictionary and counts occurrences
def tokens_to_dictionary(lst):
    d = {}
    for y in lst:
        size = len(y)
        y = y.lower()
        if y[size - 1] in punctuation:
            if y[size - 1] in d.keys():
                d[y[size - 1]] += 1
            else:
                d[y[size - 1]] = 1
            if y[:-1] in d.keys():
                d[y[:-1]] += 1
            else:
                d[y[:-1]] = 1
        elif y[0] in punctuation:
            if y[0] in d.keys():
                d[y[0]] += 1
            else:
                d[y[0]] = 1
            if y[1:] in d.keys():
                d[y[1:]] += 1
            else:
                d[y[1:]] = 1
        else:
            if y in d.keys():
                d[y] += 1
            else:
                d[y] = 1
    return d


# sort in descending order
def sort_values(d):
    sv = sorted(d.items(), key=lambda k: k[1], reverse=True)
    return sv


# print five most occurring tokens
def print_most_occurrences(tokens):
    count = 0
    for y in tokens:
        if count < 5:
            print(y)
        if count == 4:
            return
        count += 1


user_input = input("Enter file name: ")
file_string = read_file(user_input)
token_count = tokens_to_dictionary(file_string.split())
sorted_values = sort_values(token_count)
print_most_occurrences(sorted_values)

        










