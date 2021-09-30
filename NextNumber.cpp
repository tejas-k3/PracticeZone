#include <iostream>
#include <string>
using namespace std;
int leftBit=-1, rightBit=-1;
string decimalToBinary(int n)
{
	string BinaryRep="";
    // Size of an integer is assumed to be 32 bits
    for (int i = 31; i >= 0; i--) {
        int k = n >> i;
        if (k & 1)
            BinaryRep+='1';
        else
            BinaryRep+='0';
    }
    // cout<<BinaryRep<<endl;
    return BinaryRep;
}
int binaryToDecimal(string n)
{
    string num = n; int dec_value = 0, base = 1, len = num.length();
    for (int i = len - 1; i >= 0; i--) {
        if (num[i] == '1')
            dec_value += base;
        base = base * 2;
    }
    return dec_value;
}
bool OnBitsTogether(string val)
{
	//int leftBit=-1, rightBit=-1;	
	for(int i=0, j=31;i<32;i++,j--)
	{
		if(val[i]=='1'&&leftBit==-1)
		leftBit=i;
		if(val[j]=='1'&&rightBit==-1)
		rightBit=j;
		if(rightBit!=-1&&leftBit!=-1)
		break;
	}
	for(int i=leftBit;i<=rightBit;i++)
	{
		if(val[i]=='0')
		return false;
	}
	return true;
}
int nextNumber(string binaryNum)
{
	bool bitsMask =OnBitsTogether(binaryNum);
	int trailingZeros=0;
	for(int i=31;i>=rightBit;i--)
		{
			if(binaryNum[i]=='0')
			trailingZeros++;
		}
	if(leftBit==rightBit)
	{
		binaryNum[leftBit-1]='1';
		binaryNum[leftBit]='0';
		return binaryToDecimal(binaryNum);
	}
	if(bitsMask)
	{
		int total1s=rightBit-leftBit;
		// cout<<"Trailing zeros"<<trailingZeros<<endl;
		// cout<<"Total 1s "<<total1s<<endl;
		binaryNum[31-trailingZeros-1-total1s]='1';
		binaryNum[leftBit]='0';
		// cout<<binaryNum<<endl;
		for(int index=31;index>leftBit;index--)
		{
			if(total1s!=0)
			{binaryNum[index]='1';
			total1s--;}
			else
			binaryNum[index]='0';
		}
		// cout<<"New rep "<<binaryNum<<endl;
		return binaryToDecimal(binaryNum);
	}
	// On bits not together 1000100101
	int index, zeros=0;
	for(int i=31;i>=1;i--)
	{
		if(binaryNum[i]=='1'&&binaryNum[i-1]=='0')
		{
			binaryNum[i]='0';
			binaryNum[i-1]='1';
			index=i;
			break;
		}
	}
	if(trailingZeros!=0)
	{
		for(int i=index; i<32;i++)
		{
			if(binaryNum[i]=='0')
			zeros++;
		}
		for(int i=index;i<32;i++)
		{
			if(zeros>0)
			{
				binaryNum[i]='0';
				zeros--;
			}
			else
			binaryNum[i]='1';
		}
	}
    return binaryToDecimal(binaryNum);
}
int main()
{
    int val;
    cin>>val;
    cout<<"Input "<<val<<endl<<"Output ";
    if(val==0)
    {
    	cout<<"Only 0 has all bits 0";
    }
    else
    cout<<nextNumber(decimalToBinary(val));
}