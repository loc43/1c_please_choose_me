import operator
import time


def is_infected(array, vertice, answer):
    return len(set(array[vertice]).intersection(answer)) > 1 or vertice in answer

array = []
m = int(input())
for i in range(m + 2):
    array.append([])
ans = set()

for i in range(m):
    tmp = str(input())
    tmp1 = tmp.split()
    a = int(tmp1[0])
    b = int(tmp1[1])
    array[a].append(b)
    array[b].append(a)

timer = time.time()

for i in range(1, m + 2):
    if(len(array[i]) == 1 or (len(array[i]) == 2 and i in array[i])):
        ans.add(i)

vert_deg = dict()
for i in range (1, m + 2):
    if len(array[i] ) > 0:
        vert_deg[i] = len(array[i])
sorted_vert = sorted(vert_deg.items(), key=operator.itemgetter(1))
m = len(vert_deg)

for i in range(m  - 1, -1, -1):
    if not is_infected(array, sorted_vert[i][0], ans):
        ans.add(sorted_vert[i][0])

for i in range(m):
    vert = sorted_vert[i][0]
    if vert in ans:
        ans.remove(vert)
        flag = not is_infected(array, vert, ans)
        for elem in array[vert]:
            if not is_infected(array, elem, ans):
                flag = True
        if flag:
            ans.add(vert)

timer2 = time.time()

print(ans, len(ans), timer2 - timer)
