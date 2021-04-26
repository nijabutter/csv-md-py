import sys
'''
TODO:
- add -p (pretty) option to enable padding for the text e.g
    -p:
    |header|header    |header |
    |abc   |abcdefghij|ab     |
    |abcdef|abc       |abcdefg|
- redirect from stdin and stdout if - is used
'''
delimiter = ","

if len(sys.argv) != 2 and len(sys.argv) != 4:
    print("Usage: table.py FILE [-d ,]")
    sys.exit(0)
  
for i in range(len(sys.argv)):
    if sys.argv[i] == "-d" and i < len(sys.argv)-1:
        i += 1
        delimiter = sys.argv[i][0]
    else:
        file_name = sys.argv[i]

with open(file_name) as f:
    contents = f.readlines()
    if not contents:
        exit(1) # output empty table instead ?

    longest = [0] * len(contents[0].split(delimiter)) # split the first line to get the number of columns
    # will be used later to store the longest (char len) column in each row to add padding

    for i, line in enumerate(contents):
        line = line.split(delimiter)
        if len(line) > len(longest):
            print(f"Line {i} contains {len(line)} delimiters instead of {len(longest)}:")
            print(delimiter.join(line))
            exit(1)
        for j, col in enumerate(line):
            longest[j] = max(longest[j], len(col))
    
    seperator = ""
    firstRow = contents[0].split(delimiter)
    for l in range(len(longest)):
        seperator += "-" * longest[l]
        print(firstRow[l].replace("\n", "").ljust(longest[l]),end="")
        if l != len(longest)-1:
            seperator += "|"
            print("|",end="")
    print("\n" + seperator)

    for row in contents[1:]:
        row = row.split(delimiter)
        for l,col in enumerate(row):
            col = col.replace("\n", "")
            print(col.ljust(longest[l]), end="")
            if l != len(longest)-1:
                print("|", end="")
        print()
