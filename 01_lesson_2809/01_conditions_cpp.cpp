#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Введите число: " << endl;
    cin >> num;  // прошу пользователя ввести число и сохраняю его

    if ((num % 2) == 0) {  // если число делится на 2 без остатка
    cout << "Четное!" << endl;  // пишу это
                       cout << "молодец!" << endl;  // пишу это
    } else {  // иначе
        cout << "Нечетное!" << endl;  // пишу это
    }
    return 0;
}
