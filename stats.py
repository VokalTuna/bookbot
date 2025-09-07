def get_num_words(book):
    return len(book.split())

# string -> dict
# dict is a dictionary with the occurence for each letter in a book.
def char_count(book):
    dict_count = {}
    book = book.lower()
    for c in book:
        if c in dict_count:
            dict_count[c] += 1
        else:
            dict_count[c] = 1
    return dict_count

# dictionary[string] = int -> list of dictionary {string:string, string: int}
# Convert a dictionary which have a character in string, and their number of occurence.
# To a list of dictionary which have "char" as key, with the key from the other dictionary as its value,
# and have "num" as key with the integer from the other dictionary as its value.
def sort_on(items):
    return items["num"]

def convert_to_list(dictionary):
    temp_dic = dictionary
    list_of_dictionary = []
    for key, val in temp_dic.items():
        list_of_dictionary.append({"char":key, "num":val})
    list_of_dictionary.sort(reverse=True, key=sort_on)
    return list_of_dictionary
