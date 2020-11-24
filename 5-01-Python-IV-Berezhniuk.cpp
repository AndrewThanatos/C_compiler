int max(int a, int b){
    if (a > b){
        return a;
    } else {
        return b;
    }
}

int min(int a, int b){
    if (a < b){
        return a;
    } else {
        return b;
    }
}

int func(int a, int b, float c){
    a += 1;
    b += 1;
    c -= 1;
    if (a < 0){
        a *= -1;
    }
    if (b < 0){
        b *= -1;
    }
    if (c < 0){
        c *= -1;
    }
    return a + b + c;
}

int sqr(int a){
    return a * a;
}

int sum(int a, int b){
    return a + b;
}

int mul(int a, int b){
    return a * b;
}

int div(int a, int b){
    return a / b;
}

int sub(int a, int b){
    return a - b;
}

int main(){
    int a = 25;
    int b = sum(a, 5);
    int c = mul(max(a, b), 2);
    int d = div(sub(a, c), 5);
    a += 1;
    b -= 1;
    c *= 2;
    d /= 2;
    a *= d;
    return func(a, b, sqr(c));
}
