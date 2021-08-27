#include <iostream>
#include <algorithm>
using namespace std;
bool triplet(int *arr, int size, int value)
{
	bool tripletExists= false;
	sort(arr, arr+size);
	for(int i=0;i<size-1;i++)
	{
		for(int j=i+1, k=size-1;j<k;)
		{
			int temp=arr[i]+arr[j]+arr[k];
			if(temp==value)
			{
				tripletExists = true;
				cout<<arr[i]<<" "<<arr[j]<<" "<<arr[k]<<endl;
				j++;
				k--;
			}
			else if(temp>value)
			k--;
			else
			j++;
		}
	}
	return tripletExists;
}
int main() {
	int n, val; cin>>n>>val;
	int A[n];
	for(int i=0;i<n;i++)
	cin>>A[i];
	if(triplet(A,n,val))
	cout<<"Above triplet sum up to provided value";
	else
	cout<<"No such triplets exist";
	return 0;
}