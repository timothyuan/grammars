from itertools import chain, combinations

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def productions(nullables, x):
    prod = []
    # all possible combination of nullables
    combos = list(powerset(nullables))
    for combo in combos:
        s = x[2:]
        for c in combo:
            s = s.replace(c, '')
        if len(s)>0:
            prod.append(x[:2]+s)
    return prod


def remove(p):
    nullables = []
    # add variables in form A -> _ to nullables
    for x in p:
        if '_' in x:
            nullables.append(x[0])

    # add variables in form A -> A1A2.... where Ai is nullable to nullables
    nullables2 = []
    for x in p:
        if all(y in nullables for y in x[2:]) and x[0] not in nullables:
            nullables2.append(x[0])

    while(len(nullables2)>0):
        nullables.extend(nullables2)
        nullables2 = []
        for x in p:
            if all(y in nullables for y in x[2:]) and x[0] not in nullables:
                nullables2.append(x[0])

    # create new productions from lambda productions
    p2 = []
    for x in p:
        #print(list(set(nullables).intersection(x[2:])))
        p2.extend(productions(list(set(nullables).intersection(x[2:])), x))
    p.extend(p2)

    # remove productions in form A -> _
    p = set(x for x in p if '_' not in x)
    p = [x for x in p if x[0]=='S'] + [x for x in p if x[0]!='S']
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
