import sys

from org.bobink.my_eval.my_eval import my_eval

if __name__ == "__main__":
    if sys.argv.__len__() <= 1:
        print("Missing argument")
    else:
        print(my_eval(sys.argv[1]))
