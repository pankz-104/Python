import sys
import argparse
n1 = int(input("Enter 1st num: \n"))
n2 = int(input("Enter 2nd num: \n"))
op = input("Select operator : + - * / \n")
def solution(args):
    if args.op == '+':
        if args.n1 == 56 and args.n2 == 4:
            print(args.n1, '+', args.n2, "is","77")
        else:
            print(args.n1, '+', args.n2, 'is',args.n1+args.n2)
    elif args.op == '-':
        if args.n1 == 45 and args.n2 == 5:
            print(args.n1, '-', args.n2, 'is ',"50")
        else:
            print(args.n1, '-', args.n2, 'is ',args.n1-args.n2 )
    elif args.op == '*':
        if args.n1 == 55 and args.n2 == 7:
            print(args.n1, '*', args.n2,' is ',444)
        else:
            print(args.n1,'*',args.n2, ' is ',args.n1*args.n2)
    else:
        print(args.n1,'/',args.n2,'is',args.n1/args.n2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n1', type = float, default = 1.0, help = 'adding the 1st args')
    parser.add_argument('--n2',type = float, default = 2.0, help = 'adding the 2nd number')
    parser.add_argument('--op',type = str, default='rip', help='Solving the probllems')

    args = parser.parse_args()
    sys.stdout.write(str(solution(args)))
