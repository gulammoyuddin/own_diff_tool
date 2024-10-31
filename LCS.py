def initialize_diffgraph(a,b):
    result = []
    for i in range(a+1):
        row = []
        for j in range(b+1):
            row.append(-1)
        result.append(row)
    return result

def initialize_countgraph(a,b):
    result = []
    for i in range(a+1):
        row = []
        for j in range(b+1):
            row.append(0)
        result.append(row)
    return result

def compare(a,b):
    if a==b:
        return 0
    if a>b:
        return -1
    if a<b:
        return 1
# s1 is row, s2 is column
# - = 0 | = 1 / = 2
def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    count_graph = initialize_countgraph(n1,n2)
    dir_graph = initialize_diffgraph(n1,n2)
    for i in range(len(s1)):
        x=i+1
        for j in range(len(s2)):
            y=j+1
            if s1[i] == s2[j]:
                comp = compare(count_graph[x][y-1],count_graph[x-1][y])
                if comp > -1:
                    count_graph[x][y]= count_graph[x-1][y]+1
                else:
                    count_graph[x][y]= count_graph[x][y-1]+1
                dir_graph[x][y]=2
            else:
                comp = compare(count_graph[x][y-1],count_graph[x-1][y])
                if comp > -1:
                    count_graph[x][y]= count_graph[x-1][y]
                    dir_graph[x][y]=1
                else:
                    count_graph[x][y]= count_graph[x][y-1]
                    dir_graph[x][y]=0
    result = ''
    if type(s1) == type([]):
        result = []
    x=n1
    y=n2
    while dir_graph[x][y]!=-1:
        # print(x,y)
        if dir_graph[x][y]==2:
            if type(s1) == type([]):
                result = [s1[x-1]]+result
            else:
                result = s1[x-1] + result
            x=x-1
            y=y-1
        else:
            if dir_graph[x][y]==1:
                x=x-1
            else:
                if dir_graph[x][y]==0:
                    y=y-1
    return result

# x= lcs, y= txt1, z=txt2
def get_diff(txt1,txt2):
    diff = []
    l = lcs(txt1,txt2)
    # print(type(l))
    x=0
    y=0
    z=0
    while x<len(l) and y<len(txt1) and z<len(txt2):
        if l[x] == txt1[y] and l[x] == txt2[z]:
            pass
        else:
            if l[x] == txt1[y]:
                while z<len(txt2) and l[x] != txt2[z]:
                    diff.append('> ' + txt2[z])
                    z=z+1
            else:
                if l[x] == txt2[z]:
                    while y<len(txt1) and l[x] != txt1[y]:
                        diff.append('< ' + txt1[y])
                        y=y+1
                else:
                    while z<len(txt2) and l[x] != txt2[z] and y<len(txt1) and l[x] != txt1[y]:
                        diff.append('> ' + txt2[z])
                        z=z+1
                        diff.append('< ' + txt1[y])
                        y=y+1
                    while z<len(txt2) and l[x] != txt2[z]:
                        diff.append('> ' + txt2[z])
                        z=z+1
                    while y<len(txt1) and l[x] != txt1[y]:
                        diff.append('< ' + txt1[y])
                        y=y+1
        x=x+1
        y=y+1
        z=z+1
    while z<len(txt2) and y<len(txt1):
        diff.append('> ' + txt2[z])
        z=z+1
        diff.append('< ' + txt1[y])
        y=y+1
    while z<len(txt2):
        diff.append('> ' + txt2[z])
        z=z+1
    while y<len(txt1):
        diff.append('< ' + txt1[y])
        y=y+1
    return diff
