int main() {
    bool a = 3 > 2;
    bool b = 1 == 1;
    int c = 10;
    if (a){
        if (b){
            c  = 20;
        }
        if (c < 20){
            c = 0;
        } else {
            c += 50;
        }
    } else {
        c = 0;
    }
    return c;
}