import os
import sys

import language

def main():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1]) as f:
                _, err = language.run(sys.argv[1], f.read())
                if err:
                    print(err)
        else:
            print("File not found")
    else:
        print("No file specified")

if __name__ == "__main__":
    main()