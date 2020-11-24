int main() {
    int a = 0b10101 + 3;
    char c = 'c';
    float testvar = -1;
    a = (a * 2) / (2 + 1) - 1;
    if (a > 100) {
        return 0;
    } else {
    if (a > 10) {
        {
            int a = -1;
            char c = 'z';
        }
        if (a == -1){
            return -1;
        }
        a = a * testvar;
        testvar = 0;
    } else {
        return -10;
    }
    }
    if (testvar == 0){
        int newvar = -20;
        a = (-a * newvar) && (a / newvar);
    }
    return a;
}