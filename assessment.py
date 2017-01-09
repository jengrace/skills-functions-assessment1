"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def is_my_town(town_name):
    """ Return True if input string is my town. Return False otherwise. """

    my_town = 'Miami'
    town_name = town_name.title()
    return my_town == town_name

# tests that function is working as intended
print is_my_town('miami')  # True
print is_my_town('Miami')  # True
print is_my_town('honolulu')  # False

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def get_full_name(first_name, last_name):
    """ Return two input strings concatenated. """

    full_name = first_name + ' ' + last_name
    return full_name.title()


# test that function is working as intended
print get_full_name('Billy', 'Joel')

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def get_person_info(hometown, first_name, last_name):
    """ Print a specific string depending on input hometown """

    full_name = get_full_name(first_name, last_name)
    if is_my_town(hometown):
        print "Hi, %s, we're from the same place!" % full_name
    else:
        print "Hi, %s, where are you from?" % full_name

# tests that function is working as intended
get_person_info('miami', 'jennifer', 'grace')
get_person_info('san francisco', 'john', 'deer')

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    new_list = list(lst)
    new_list.append(num)

    return new_list


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(item_price, state_abbr, tax=0.05):
    """ Returns total cost of each item depending on state taxes and fees """

    state_abbr.upper()
    if state_abbr == 'CA':
        recycling_fee = 0.03
        total_cost = item_price + item_price*tax + item_price*recycling_fee
    elif state_abbr == 'PA':
        highway_safety_fee = 2.00
        total_cost = item_price + item_price*tax + highway_safety_fee
    elif state_abbr == 'MA':
        if item_price < 100.00:
            commonwealth_fee = 1.00
        elif item_price > 100.00:
            commonwealth_fee = 3.00
        total_cost = item_price + item_price*tax + commonwealth_fee
    else:
        total_cost = item_price + item_price*tax

    return total_cost


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def appending_to_list(lst, *arg):
    """ Return input list that has an `n` number of arguments appended to it """

    for element in arg:
        lst.append(element)

    return lst

# tests that function is working as intended
appending_to_list([1, 3, 5], 10, 20, 30)

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def get_word(word):
    """ Return the input string and result of multiple_of_word function """

    if word == '':
        print 'Please provide a word as an input.'
        return

    def multipe_of_word(word):
        """ Return the input string multiplied three times """
        return word * 3

    return word, multipe_of_word(word)

# tests that functions are working as intended
print get_word('apple')
print get_word('')

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
