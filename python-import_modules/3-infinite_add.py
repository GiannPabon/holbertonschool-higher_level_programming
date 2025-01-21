#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
for arg in sys.argv[1:]:  # Skip the first element
    total += int(arg)    # Convert each argument to an integer and add it
print("{}".format(total))
