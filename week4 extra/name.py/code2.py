import sys
try:
        print("hello i m ", sys.argv[1])
except IndexError:
        sys.exit("your on worng location")
