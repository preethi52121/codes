//Check whether the nth bit (0-based index) of a number is set.
int isBitSet(int num, int n) {
    return (num & (1 << n)) != 0;
}