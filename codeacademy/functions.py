def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

#function calling a function
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n)+ 2
# build in functions

def distance_from_zero(number):

    if type(number)==int or type(number)==float:
        return abs(number)
    else:
        return "Nope"
