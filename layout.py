# Linnea Kirby
# 4 January 2016
#
# PageOrder.py
# Takes in a number of pages
# (and, optionally, the number of sheets per signature)
# and outputs the the layout of all signatures

import string

# rounds the number of pages to the nearest multiple of 4
def roundPages(pages):
    extra = pages%4
    if extra:
        extra = 4-extra
    return pages+extra

# finds the number of sheets needed (i.e. the rounded number of pages divided by 4)
def getSheets(pages):
    rPages = roundPages(pages)
    return rPages//4

# Prints one signature
def printPages(count, end, total):
    start = 1
    for p in range(start, end):
        print("FRONT OF PAGE", p, "\t BACK OF PAGE", p)
        print(" _______________ \t _______________ ")
        print("|       |       |\t|       |       |")
        print("|       |       |\t|       |       |")
        print("{:^1}{:^7}{:^1}{:^7}{:^1}{:^7}{:^1}{:^7}{:^1}".format("|",count,"|",total,"|\t|",count+1,"|",total-1,"|"))
        print("|       |       |\t|       |       |")
        print("|_______|_______|\t|_______|_______|")
        count+=2
        total-=2
        print()

# rounds the number of signatures up and finds the number of signatures needed
def getSigs(sheets, sps):
    if sheets%sps == 0:
        return sheets//sps
    else:
        return (sheets//sps)+1

# Prints multiple signatures
def printSignatures(sheets, sps):
    pps = sps*4
    start = 1
    soFar = pps
    sigs = getSigs(sheets, sps)
    print("\n",sigs, "signatures are needed.")
    for s in range(1, sigs+1):
        print("\t\tSignature", s, ":")
        printPages(start, sps+1, soFar)
        start=sigs*s*4+1
        soFar+=pps
        

# Decides if one or multiple signatures are needed
def printOrder(pages, sps):
    sheets = getSheets(pages)
    if sheets <= sps:
        printPages(1, sheets+1, sheets*4)
    else:
        printSignatures(sheets, sps)

# Finds a reasonable number of sheets per signature
def getSps(pages):
    sheets = getSheets(pages)
    
    lowest = 10
    for i in range (3, 7):
        if sheets%i == 0:
            return i
        elif sheets%i < lowest:
            lowest = i
    return lowest

def main():
    print("Welcome! This program takes in a number of pages and outputs a valid layout.\n")
    print("Note: There may be blank pages at the end, as the number of total pages must be a multiple of 4.\n")
    
    try:
        pages = eval(input("Please enter the number of pages: "))    
    
        sps = getSps(pages)
    
        printOrder(pages, sps)
    except Exception as e:
        print("I'm sorry, but your input was invalid.")

main()

