def areKnotsAdjacent(knot1, knot2):
    if not isinstance(knot1, tuple):
        raise ValueError("knot1 must be tuple type")
    if not isinstance(knot2, tuple):
        raise ValueError("knot2 must be tuple type")
    return ((knot1[0] - 1) <= knot2[0]) and (knot2[0] <= (knot1[0] + 1))\
        and ((knot1[1] -1) <= knot2[1]) and (knot2[1] <= (knot1[1] + 1))

def moveFollowKnot(leadKnot, followKnot):
    if not isinstance(leadKnot, tuple):
        raise ValueError("leadKnot must be tuple type")
    if not isinstance(followKnot, tuple):
        raise ValueError("followKnot must be tuple type")
    horzDelta = leadKnot[0] - followKnot[0]
    vertDelta = leadKnot[1] - followKnot[1]
    if horzDelta == 0:
        if vertDelta == 0:
            print("leadKnot and followKnot are at the same point")
        else:
            if vertDelta < 0:
                followKnot = (followKnot[0], followKnot[1] - 1)
            else:
                followKnot = (followKnot[0], followKnot[1] + 1)
    else:
        if vertDelta == 0:
            if horzDelta < 0:
                followKnot = (followKnot[0] - 1, followKnot[1])
            else:
                followKnot = (followKnot[0] + 1, followKnot[1])
        else:
            if vertDelta < 0:
                if horzDelta < 0:
                    followKnot = (followKnot[0] - 1, followKnot[1] - 1)
                else:
                    followKnot = (followKnot[0] + 1, followKnot[1] - 1)
            else:
                if horzDelta < 0:
                    followKnot = (followKnot[0] - 1, followKnot[1] + 1)
                else:
                    followKnot = (followKnot[0] + 1, followKnot[1] + 1)
    return followKnot

if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        lines = inputFile.readlines()
        # init 10 knots
        knotsCount = 10
        knots = list()
        for i in range(knotsCount):
            knots.append((0,0))
        tail = knots[knotsCount - 1]
        tailTraveledPos = set()
        tailTraveledPos.add(tail)
        for line in lines:
            moveTokens = line.strip().split()
            direction = moveTokens[0]
            length = int(moveTokens[1])
            for i in range(length):
                head = knots[0]
                if direction == "R":
                    head = (head[0] + 1, head[1])
                elif direction == "L":
                    head = (head[0] - 1, head[1])
                elif direction == "U":
                    head = (head[0], head[1] + 1)
                elif direction == "D":
                    head = (head[0], head[1] - 1)
                knots[0] = head
                for j in range(1, knotsCount):
                    leadKnot = knots[j - 1]
                    followKnot = knots[j]
                    if areKnotsAdjacent(leadKnot, followKnot):
                        continue
                    followKnot = moveFollowKnot(leadKnot, followKnot)
                    knots[j] = followKnot
                tail = knots[knotsCount - 1]
                tailTraveledPos.add(tail)
        print(len(tailTraveledPos))
    finally:
        inputFile.close()