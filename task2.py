from queue import Queue

def reachable(a, u):
    r = set()
    q = Queue()
    q.put(a)
    while not q.empty():
        x = q.get()
        for y in [y[2] for y in u if y[0]==x and y[2] not in r]:
            r.add(y)
            q.put(y)
    return list(r)


def remove(p):
    vars = set(x[0] for x in p) # variables
    unit = set(x for x in p if len(x)==3 and x[2].isalpha() and x[2].isupper()) # unit productions
    dict = {} # reachable values from unit productions
    for v in vars:
        dict[v] = reachable(v, unit)
    for v in dict:
        for reached in dict[v]:
            for prod in [prod for prod in p if prod[0]==reached and prod not in unit]:
                if v + prod[1:] not in p:
                    p.append(v + prod[1:])
    p = set(x for x in p if x not in unit)
    return p

def main():
    p = []
    n = int(input())
    for i in range(n):
        p.append(input())
    p = remove(p)
    print(len(p))
    for x in p:
        print(x)

if __name__ == '__main__':
    main()
