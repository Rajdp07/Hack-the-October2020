def binary_search(ar, key):
    low, high = 0, len(ar)-1
    while low <= high:
        mid = (low + (high-low))//2
        if ar[mid] == key:
            return mid
        elif ar[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    if low > high:
        return -1



if __name__ == "__main__":
    ar = list(map(int, input().split()))
    ar.sort()
    print('Sorted Array :- ', ar)
    key = int(input())
    pos = binary_search(ar, key)
    if pos >= 0:
        print('Key Present at position {}!!'.format(pos+1))
    else:
        print('Key Not Present!!!')
        
        
        
        
*************************
#include <iostream>
using namespace std;

int main()
{
	int count, i, arr[30], num, first, last, middle;
	cout<<"how many elements would you like to enter?:"; 
        cin>>count;

	for (i=0; i<count; i++)
	{
		cout<<"Enter number "<<(i+1)<<": "; 
                cin>>arr[i];
	}
	cout<<"Enter the number that you want to search:"; 
        cin>>num;
	first = 0;
	last = count-1;
	middle = (first+last)/2;
	while (first <= last)
	{
	   if(arr[middle] < num)
	   {
		first = middle + 1;

	   }
	   else if(arr[middle] == num)
	   {
		cout<<num<<" found in the array at the location "<<middle+1<<"\n"; 
                break; 
           } 
           else { 
                last = middle - 1; 
           } 
           middle = (first + last)/2; 
        } 
        if(first > last)
	{
	   cout<<num<<" not found in the array";
	}
	return 0;
}
