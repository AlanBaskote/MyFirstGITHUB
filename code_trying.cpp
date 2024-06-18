// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main(){
    string nameOfTheReciepient;
    cout << "Please state your name?" << endl;
    cin >> nameOfTheReciepient;
    if (nameOfTheReciepient == "Bob" || nameOfTheReciepient == "bob" || nameOfTheReciepient == "BOB" )
    {
        cout << "Funny name";
    }
    else
    {
        cout << "That's a nice name amigo";
    } 

}  