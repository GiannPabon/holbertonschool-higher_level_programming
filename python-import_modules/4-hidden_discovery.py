#!/usr/bin/python3
import sys
sys.path.append('/tmp/hidden_4.pyc.')
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
