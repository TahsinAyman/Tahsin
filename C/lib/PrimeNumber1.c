/*
#Z = int(input("Enter a number: "))
import sys

Z = sys.maxsize-8

# 6n-1 / 6n + 1

factor = Z // 6
p1 = (factor + 1) * 6 - 1
p2 = (factor - 1) * 6 + 1

if Z in (p1, p2):
    print(f"{Z} is prime")
else:
    print(f"{Z} is not prime")
*/

void PrimeNumber1(unsigned long long int z)
{
    unsigned long long int factor = z / 6;
    unsigned long long int p1, p2;
    p1 = (factor + 1) * 6 - 1;
    p2 = (factor - 1) * 6 + 1;

    if (z == p1 || z == p2)
    {
        printf("%lld is prime", z);
    }
    else
    {
        printf("%lld is not prime", z);
    }
}