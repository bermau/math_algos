import argparse

def create_cmdarg():
    parser = argparse.ArgumentParser(description='Muliple Two numbers')
    parser.add_argument('num1', type=float, help='First Value')
    parser.add_argument('num2', type=int, help='Second Value')
    args = parser.parse_args()
    return (args.num1, args.num2)

def karatsuba(num1, num2):
    if ( num1 < 10 ) and ( num2 < 10):
        return num1*num2

if __name__ == '__main__':
    num1,num2 = create_cmdarg()
    print (karatsuba(num1, num2))
