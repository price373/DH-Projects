import sys

"""Print all lines beginning with a pattern"""
def startgrep(args):
    if len(args) < 2:
        print("Invalid input")
        print("Usage: startgrep.py  pattern FILENAME..."
        exit(1)
    pattern = args.pop(0)
    for fileName in args:
        f = open(fileName)
	for line in f:
	    if line.startswith(pattern):
	    print(line, end = "")
	f.close

if __name__ == "__main__":
    if len(sys.argv) > 2:
        startgrep(sys.argv[1:])
    else:
        print("Usage startgrep.py PATTERN FILE...")
