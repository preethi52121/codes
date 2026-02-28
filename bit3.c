//Clear nth bit
int clearBit(int num, int n) {
    return num & ~(1 << n);
}