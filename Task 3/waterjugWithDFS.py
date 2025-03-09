from collections import deque

def waterJugProblem(jugSize1,jugSize2,target):
    stack=deque()
    visited=set()
    stack.append((0,0,[]))
    while stack:
        jug1,jug2,path=stack.pop()
        if (jug1,jug2) in visited:
            continue
        visited.add((jug1,jug2))
        currPath=path+[(jug1,jug2)]
        if jug1==target or jug2==target:
            print("The steps are Following")
            for step in currPath:
                print(step)
            return True    
        rules=[
            (jugSize1,jug2),
            (jug1,jugSize2),
            (0,jug2),
            (jug1,0)
        ]        


        #Rule no 5
        transfer=min(jug1, jugSize2 - jug2)
        rules.append((jug1 - transfer, jug2 + transfer))


        #Rule no 6
        transfer = min(jug2, jugSize1 - jug1)
        rules.append((jug1 + transfer, jug2 - transfer))

        
        for state in rules:
            if state not in visited:
                stack.append((*state,currPath))
    print("No Solution Found")
    return False




jugSize1=4
jugSize2=3
target=2
waterJugProblem(jugSize1,jugSize2,target)
