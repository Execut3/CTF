// A Naive recursive C++ program to find minimum of coins
// to make a given change V
#include<bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
 
// m is size of coins array (number of different coins)
int minCoins(int coins[], int m, int V)
{
   // base case
   if (V == 0) return 0;
 
   // Initialize result
   int res = INT_MAX;
 
   // Try every coin that has smaller value than V
   for (int i=0; i<m; i++)
   {
     if (coins[i] <= V)
     {
         int sub_res = minCoins(coins, m, V-coins[i]);
 
         // Check for INT_MAX to avoid overflow and see if
         // result can minimized
         if (sub_res != INT_MAX && sub_res + 1 < res)
            res = sub_res + 1;
     }
   }
   return res;
}
 
// Driver program to test above function
int main(int argc, char* argv[])
{
    int coins[] =  {1, 5, 10, 25, 50, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000};
    int m = sizeof(coins)/sizeof(coins[0]);
    int V = atoi(argv[1]);
    cout << "Minimum coins required is "
         << minCoins(coins, m, V);
    return 0;
}