import sys

delimiter = ","

if len(sys.argv) != 2 and len(sys.argv) != 4:
    print("Usage: table.py FILE [-d ,]")
    sys.exit(0)

for i in range(len(sys.argv)):
    if sys.argv[i] == "-d":
        i += 1
        delimiter = sys.argv[i][0]
    else:
        file_name = sys.argv[i]

with open(file_name) as f:    
    contents = f.readlines()
    if not contents:
        exit(1)

    longest = [0] * len(contents[0].split(delimiter)) # split the first line to get the number of columns

    for i, line in enumerate(contents):
        line = line.split(delimiter)
        if len(line) > len(longest):
            print(f"Line {i} contains {len(line)} delimiters instead of {len(line)}:")
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
