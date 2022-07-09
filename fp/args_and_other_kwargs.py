# Write function that accepts any number of arguments and keyword arguments
# Function returns dictionary of arguments and keyword arguments

# Proper format
# {
#   index: argument
#   name: keyword_argument,
# }
# if parameter is unnamed, its index is key


def list_parameters(*args, **kwargs):
    new_dict = kwargs
    for index, item in enumerate(args):
        new_dict[index] = item
    return new_dict
