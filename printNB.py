from IPython.display import display, Markdown, Latex

def printCrtTable(tab):
    mkdwn = "|p/q"
    #display(Markdown('*some markdown* $\phi$'))
    numCols = len(tab[0])
    for col in range(numCols):
        mkdwn += f"|${col}$"
    mkdwn += "|\n"
    for _ in range(numCols+1):
        mkdwn += f"|:-:"
    mkdwn += "|"
    rowN = 0
    for row in tab:
        mkdwn += f"\n|${rowN}$|"
        rowN += 1
        for col in row:
            mkdwn += f"${col}$|"
    display(Markdown(mkdwn))

def printTable(dic):
    res = "|"
    nextLine = "|"
    for key in list(dic.keys()):
        res += f"{key}|"
        nextLine += ":-:|"
    res += "\n" + nextLine + "\n"
    for row in range(len(dic[list(dic.keys())[0]])):
        nex = "|"
        for key in list(dic.keys()):
            nex += f"{dic[key][row]}|"
        res += nex + "\n"
    printmd(res)

def boldifyList(li):
    return list(map(boldify, li))

def boldify(a):
    return f"**{a}**"

def latexifyList(li):
    return list(map(latexify, li))

def latexify(a):
    return f"${a}$"

def printex(a):
    printmd(latexify(a))

def printmd(a):
    display(Markdown(f"{a}"))

