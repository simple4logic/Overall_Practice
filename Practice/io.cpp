#include<stdio.h>
int main()
{
 int n,z,x;
 scanf("%d",&n);
 for(z=1;z<=n;z++){
  for(x=0;x!=n-z;x++)printf("1");
  for(x=0;x!=z;x++)printf("*1");
  puts("");
 }
 return 0;
}