from sys import stdin
from syntax import *

def main():
    for line in stdin:
        line = line.strip()
        if line == '#':
            break
        else:
            if CheckSyntax(line):
                print("Formeln är syntaktiskt korrekt")


if __name__ == "__main__":
    main()