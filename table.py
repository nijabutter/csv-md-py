import sys

if len(sys.argv) != 2:
    print("Usage: table.py <file-name.csv>")
    sys.exit(0)

with open(sys.argv[1]) as f:
    
    contents = f.readlines()
    longest = [0] * len(contents[0].split(","))

    for r in range(len(contents)):
        row = contents[r].split(",")
        for c in range(len(row)):
            if len(row[c]) > longest[c]:
                longest[c] = len(row[c])
    
    seperator = ""
    firstRow = contents[0].split(",")
    for l in range(len(longest)):
        seperator += "-" * longest[l]
        print(firstRow[l].replace("\n", "").ljust(longest[l]),end="")
        if l != len(longest)-1:
            seperator += "|"
            print("|",end="")
    print("\n" + seperator)

    for row in contents[1:]:
        row = row.split(",")
        for l,col in enumerate(row):
            col = col.replace("\n", "")
            print(col.ljust(longest[l]), end="")
            if l != len(longest)-1:
                print("|", end="")
        print()
