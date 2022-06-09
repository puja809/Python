"""
                                    Command Line Utility Using Python
"""

import argparse
import sys


def calc(args):
    if args.o == "add":
        return args.x + args.y
    if args.o == "sub":
        return args.x - args.y
    if args.o == "mul":
        return args.x * args.y
    if args.o == "div":
        return args.x / args.y
    else:
        return "Invalid input"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="This CLI is for adding numbers. Enter 1st number")
    parser.add_argument('--y', type=float, default=9.0, help="This CLI is for adding numbers. Enter 2nd number")
    parser.add_argument('--o', type=str, default="add", help="This CLI is for adding numbers. Enter operator")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

"""
Run the abode file through terminal
"""