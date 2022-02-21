# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.


# Variant 1 ( without dict comprehension )
def func_1(dict_1, dict_2):
    count_dict = dict()
    for key, value in dict_1.items():
        count_dict[key] = value * dict_2[key]
    return count_dict


# Variant 2 ( with dict comprehension )
def func_2(dict_1, dict_2):
    count_dict = {key: value*dict_2[key] for key,value in dict_1.items()}
    return count_dict


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


print(func_1(stock, prices))
print(func_2(stock, prices))
