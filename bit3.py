#Clear nth bit
def clear_bit(num, n):
    return num & ~(1 << n)