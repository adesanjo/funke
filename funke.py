import os
import sys

import language

def main():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1]) as f:
                _, err = language.run(f.read())
                if err:
                    print(err)
        else:
            print("File not found")
    else:
        print("No file specified, using test code")
        _, err = language.run("add(a, b) = +(a, b)\nprint(n) = $(n)\nprint(add(3, 4))")
        if err:
            print(err)

if __name__ == "__main__":
    main()