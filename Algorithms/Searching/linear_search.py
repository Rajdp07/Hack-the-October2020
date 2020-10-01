def linear_search(ar, key):
    for i in range(len(ar)):
        if ar[i] == key:
            return i
    return -1



if __name__ == "__main__":
    ar = list(map(int, input().split()))
    key = int(input())
    pos = linear_search(ar, key)
    if pos >= 0:
        print('Key Present at position {}!!'.format(pos+1))
    else:
        print('Key Not Present!!!')
        
        
****************************************

#include <iostream> 
using namespace std; 
  
int search(int arr[], int n, int x) 
{ 
    int i; 
    for (i = 0; i < n; i++) 
        if (arr[i] == x) 
            return i; 
    return -1; 
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int x = 10; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int result = search(arr, n, x); 
   (result == -1)? cout<<"Element is not present in array" 
                 : cout<<"Element is present at index " <<result; 
   return 0; 
} 
