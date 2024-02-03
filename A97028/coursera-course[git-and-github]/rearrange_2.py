# import re module to use regular expressions
import re

# function that rearranges the name
def rearrange_name(name):
    # using the search method to find the first and last name
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    # if the name is not in the correct format, return the name as is
    if result == None:
        # if the name is not in the correct format, return the name as is
        return name
    # if the name is in the correct format, return the rearranged name
    return "{} {}".format(result[2], result[1])
