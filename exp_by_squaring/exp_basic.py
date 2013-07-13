import argparse


def create_cmdarg():
    parser = argparse.ArgumentParser(description='Find Exponent')
    parser.add_argument('base', help='Base Value')
    parser.add_argument('exponent', help='Exponent Value')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    try:
        create_cmdarg()
    catch:
    
    print base
    print exponent