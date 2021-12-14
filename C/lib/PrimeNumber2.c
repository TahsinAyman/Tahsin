/*
"""
aslkdjfl sakdjf
"""
o = []
N = int(input("Enter a number: "))
for a in range(N):
    num = int(input("Enter a number: "))
    flag = True
    limit = (num//2)+1
    if num % 2 == 0:
        flag = False
    else:
        if num > 3:
            for i in range(3, limit, 2):
                if (num % i) == 0:
                    flag = False
                    break
    o.append(f"{num} is prime" if flag else f"{num} is not prime")


for x in o:
    print(x)
*/

void PrimeNumber2(unsigned int num)
{
    int flag = 1;
    unsigned int limit = (num / 2);
    if (num % 2 == 0)
    {
        flag = 0;
    }
    else
    {
        if (num > 3)
        {
            for (int i = 3; i <= limit; i += 2)
            {
                if (num % i == 0)
                {
                    flag = 0;
                    break;
                }
            }
        }
        if (flag)
        {
            printf("%u is prime", num);
        }
        else
        {
            printf("%u is not prime", num);
        }
    }
}