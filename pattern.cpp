#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter the number:";
    cin>>n;
    int i,j;
    for(i=1;i<=2*n;i++)
    {
        if(i<=n)
        {
           for(j=1;j<=i;j++)
           {
            cout<<j<<" ";
           }
           cout<<endl;
        }
        else if(i>n)
        {
           for(j=1;j<=2*n+1-i;j++)
           {
            cout<<j<<" ";
           }
           cout<<endl;
        }
    }
}