import sys

try:
    total = int(sys.argv[1])
    if(total < 0):
        raise ValueError
    total += 1
    for n in range(1, total):
        if( n % 3 == 0 and n % 5 == 0):
            print("fizz buzz")
        elif( n % 3 == 0):
            print("fizz")
        elif( n % 5 == 0):
            print("buzz")
        else:
            print(n)
except (IndexError, ValueError) as e:
    condition = True
    while(condition):
        try: 
            total = int(input("Please enter a positive integer: "))
            if(total < 0):
                raise ValueError
            total += 1
            for n in range(1,total):
                if( n % 3 == 0 and n % 5 == 0):
                    print("fizz buzz")
                elif( n % 3 == 0):
                    print("fizz")
                elif( n % 5 == 0):
                    print("buzz")
                else:
                    print(n)
            condition = False
        except (IndexError, ValueError) as e:
            print("Please enter a positive integer")