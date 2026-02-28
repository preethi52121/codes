#Check whether the nth bit (0-based index) of a number is set.
def is_bit_set(num, n):
    return (num & (1 << n)) != 0