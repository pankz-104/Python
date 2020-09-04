import argparse
# for making ocmmand line utility
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "something went wrong"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float, default=1.0,
                        help='Enter first number. This is utility u can make. Do dm me for further')
    parser.add_argument('--y', type=float, default=2.0,
    help = 'Enter 2nd number. This is utility u can make. Do dm me for further')

    parser.add_argument('--o', type=str, default='add',
    help = 'This is utility u can make. Do dm me for further')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
