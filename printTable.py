from IPython.display import display, Markdown, Latex

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
    display(Markdown(res))