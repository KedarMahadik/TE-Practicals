/******************************************************************************

Write a program to demonstrate Sub-netting and find subnet masks.

*******************************************************************************/
#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

int main()
{
    char ip[50];
    int prefixLength;
    int w,x,y,z;
    unsigned long netMask;
    unsigned long firstAddress;
    unsigned long lastAddress;
    unsigned long ipAddress;
    int noOfAddr;

    
    cout<<"\nEnter IP Address (in the format w.x.y.z): ";
    cin>>ip;
    cout<<"\nEnter prefix length: ";
    cin>>prefixLength;
    
    sscanf(ip, "%d.%d.%d.%d", &w,&x,&y,&z);


    printf("\nIp Address: %d.%d.%d.%d\n",w,x,y,z);
    cout<<"\nPrefixLength: "<<prefixLength<<endl;

    ipAddress=w*pow(256,3) + x*pow(256,2) + y*pow(256,1)+z*pow(256,0);
    printf("\nIP Address: %d.%d.%d.%d\n",
        (int)((ipAddress >> 24) & 0xFF),
        (int)((ipAddress >> 16) & 0xFF),
        (int)((ipAddress >> 8) & 0xFF),
        (int)(ipAddress & 0xFF));
        
    netMask = 0xFFFFFFFFUL << (32 - prefixLength);
    printf("\nNetwork Mask: %d.%d.%d.%d\n",
        (int)((netMask >> 24) & 0xFF),
        (int)((netMask >> 16) & 0xFF),
        (int)((netMask >> 8) & 0xFF),
        (int)(netMask & 0xFF));    
        
    noOfAddr=pow(2,32-prefixLength);
    cout<<"\nNumber of Addresses="<<noOfAddr<<endl;
    
    firstAddress=ipAddress & netMask;    
    printf("\nFirst Address: %d.%d.%d.%d\n",
        (int)((firstAddress >> 24) & 0xFF),
        (int)((firstAddress >> 16) & 0xFF),
        (int)((firstAddress >> 8) & 0xFF),
        (int)(firstAddress & 0xFF));
        
    lastAddress=ipAddress | ~netMask;    
    printf("\nLast Address: %d.%d.%d.%d\n",
        (int)((lastAddress >> 24) & 0xFF),
        (int)((lastAddress >> 16) & 0xFF),
        (int)((lastAddress >> 8) & 0xFF),
        (int)(lastAddress & 0xFF));    
 
//Subnetting
cout<<"\n*************Subnetting******************\n";
    int noOfSubnets;
    int subprefixLength;
    unsigned long tempFirstIP, tempLastIP,tempSubnetMask,tempAddr;

    cout<<"\nEnter number of subnets: ";
    cin>>noOfSubnets;
    
    subprefixLength=prefixLength+log2(noOfSubnets);
    
    cout<<"\nnsub (prefix Length of subnetworks):"<<subprefixLength<<endl;
    
    noOfAddr=pow(2,32-subprefixLength);
    cout<<"\nNumber of Addresses in each subnetworks="<<noOfAddr<<endl;
    
    tempSubnetMask = 0xFFFFFFFFUL << (32 - subprefixLength);
    printf("\nSubnet Mask : %d.%d.%d.%d\n",
        (int)((tempSubnetMask >> 24) & 0xFF),
        (int)((tempSubnetMask >> 16) & 0xFF),
        (int)((tempSubnetMask >> 8) & 0xFF),
        (int)(tempSubnetMask & 0xFF));

    tempAddr=firstAddress;
    
    for(int i=1;i<=noOfSubnets;i++)
    {
        cout<<"\n\n******** This is subnetwork "<<i<<"********"<<endl;
       
        tempFirstIP=tempAddr & tempSubnetMask;
        printf("\nFirst Address: %d.%d.%d.%d\n",
        (int)((tempFirstIP >> 24) & 0xFF),
        (int)((tempFirstIP >> 16) & 0xFF),
        (int)((tempFirstIP >> 8) & 0xFF),
        (int)(tempFirstIP & 0xFF));
        
        lastAddress=tempAddr | ~tempSubnetMask;    
        printf("\nLast Address: %d.%d.%d.%d\n",
        (int)((lastAddress >> 24) & 0xFF),
        (int)((lastAddress >> 16) & 0xFF),
        (int)((lastAddress >> 8) & 0xFF),
        (int)(lastAddress & 0xFF));
        cout<<"\n##### This is end of subnetwork "<<i<<"#####"<<endl;

        tempAddr=lastAddress+1;
    }

    return 0;
}

