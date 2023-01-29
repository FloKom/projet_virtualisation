#include <bits/stdc++.h>
using namespace std;

int main(){

   int a[4];

   __asm__("mov $0x1, %eax\n\t");
   //__asm__("mov $0x0, %ecx\n\t");

   __asm__("cpuid\n\t");
   __asm__("mov %%eax, %0\n\t":"=r" (a[0]));
   __asm__("mov %%ebx, %0\n\t":"=r" (a[1]));
   __asm__("mov %%ecx, %0\n\t":"=r" (a[2]));
   __asm__("mov %%edx, %0\n\t":"=r" (a[3]));
  
   cout << bitset<32>(a[2]).to_string() << endl;
   cout << bitset<32>(a[3]).to_string() << endl;

   return 0;
}