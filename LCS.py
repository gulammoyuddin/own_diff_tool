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
    x=n1
    y=n2
    while dir_graph[x][y]!=-1:
        # print(x,y)
        if dir_graph[x][y]==2:
            result=s1[x-1]+result
            x=x-1
            y=y-1
        else:
            if dir_graph[x][y]==1:
                x=x-1
            else:
                if dir_graph[x][y]==0:
                    y=y-1
    return result