import argparse


def create_cmdarg():
    parser = argparse.ArgumentParser(description='Find Exponent')
    parser.add_argument('base', type=float, help='Base Value')
    parser.add_argument('exponent', type=int, help='Exponent Value')
    args = parser.parse_args()
    return (args.base, args.exponent)


def exp(base, exponent):
    if exponent < 0:
        return exp(1/base, -exponent)
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent % 2 == 0:
        return exp(base*base, exponent/2)
    elif exponent % 2 == 1:
        return base * exp(base*base, (exponent-1)/2)

if __name__ == '__main__':
    base, exponent = create_cmdarg()
    print (exp(base, exponent))
