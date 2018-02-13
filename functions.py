eglist = [10, 50, 30, 12, 6, 8, 100]


def egfunc(eglist):
    highest = max(eglist)
    lowest = min(eglist)
    first = eglist[0]
    last = eglist[-1]
    return(highest, lowest, first, last)


series = egfunc(eglist)
print(series)
