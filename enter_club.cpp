// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main() {
    /*int age;
    cout << "Hello, please enter your age" <<endl;
    cin>> age ;
    if (age <= 17) 
    {
        cout << "Go back to your mom";
    }
    else if (age == 69)
    {
        cout << "nice";
    }
    else 
    { 
        cout << "You can enter";
    }   
    */
    int number1, number2;
    string typeOfCalucation; 
    cout << "Hello, please enter if you want to subtract or sum" <<endl;
    cin>> typeOfCalucation;
    if (typeOfCalucation == "subtract")
    {
        cout << "Please enter your number \n"; 
        cin >> number1;
        cout << "Please enter your number \n";
        cin >> number2;
        cout << number1 - number2;  
    }
    else if (typeOfCalucation == "sum")
    {
        cout << "Please enter your number \n"; 
        cin >> number1;
        cout << "Please enter your number \n";
        cin >> number2;
        cout << number1 + number2;
    }
    else 
    {
        cout << "Please enter only the word sum and subtract";
    }
    return 0;
}
    