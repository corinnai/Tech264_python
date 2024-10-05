import sys

#check for arguments

if len(sys.argv) > 1:
    print("you gave me an argument")
    print("Print argument with index 0")
    print(sys.argv[0])
    print("Print argument with index 1")
    print(sys.argv[1])

else:
    print("you gave me no argument")
    print("Print argument with index 0")
    print(sys.argv[0])

