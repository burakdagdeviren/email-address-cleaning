import re
import os

os.system('cls')
a = input("Please paste from clipboard:\n")
print("\n")

pattern = "<(.*?)>"
first =""


print("Printing Results ===========")
try:
    for n in range(len(a)):
        substring = re.search(pattern, a[n:]).group(1)
        start = a.find(substring) + len(substring)
        if substring != first:
            first = substring
            print(first + ", ", end="")
except AttributeError:
        print("\n\nDone..")

exit()

