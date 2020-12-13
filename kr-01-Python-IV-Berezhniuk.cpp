// Фунція для визнчення більшого серед двох чисел
int max(int a, int b){
    return (a > b) ? a: b;
}

int main(){
    // Перше ціле число
    int num1 = 15;
    // Друге ціле число
    int num2 = 14;

    int sum = 0;
    int bigger = max(num1, num2);
    for (int i=1; i<=bigger; i+=1){
     if (bigger % i == 0){
        sum += i;
     }
    }
    return sum;
}