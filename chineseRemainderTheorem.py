from IPython.display import display, Markdown, Latex

def crt(p,q):
    tab = [ [ -1 for _ in range(q) ] for _ in range(p) ]
    #we now have table with p rows and q cols
    for i in range(p*q):
        tab[i%p][i%q] = i
    return tab

def crtJacobi(p,q):
    from isASquare import jacobi
    tab = [ [ -1 for _ in range(q) ] for _ in range(p) ]
    #we now have table with p rows and q cols
    for a in range(p*q):
        tab[a%p][a%q] = jacobi(a,p*q,0,False)
    return tab


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