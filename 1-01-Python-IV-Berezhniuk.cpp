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
    for (int i=0; i<5; i+=1){
        for (int j=5; j>0; j-=2){
            a += 1;
        }
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

int divv(int a, int b){
    return a / b;
}

int sub(int a, int b){
    return a - b;
}

int main(){
    int a = 25;
    int b = sum(a, 5);
    int c = mul(max(a, b), 2);
    int d = divv(sub(a, c), 5);
    a += 1;
    b -= 1;
    c *= 2;
    d /= 2;
    a *= min(a * 3, d);
    while (a < 100){
     a += 1;
     b -= 1;
    }
    for (int i=0; i<10; i+=2){
        a += 2;
    }
    return func(a, b, sqr(c / b));
}