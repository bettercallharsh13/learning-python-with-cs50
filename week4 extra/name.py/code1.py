import sys
their is another way

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
       print("too many argument")
else:
       print("hello i m", sys.argv[1])
