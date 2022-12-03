#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    Uin = argv[1:]
    size = len(Uin)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size != 1) else "argument",
                 "." if (size == 0) else ":"))
    for idx, arg in enumerate(Uin):
        print("{:d}: {:s}".format(idx + 1, arg))
