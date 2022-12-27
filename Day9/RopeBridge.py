def areKnotsAdjacent(knot1, knot2):
    if not isinstance(knot1, tuple):
        raise ValueError("knot1 must be tuple type")
    if not isinstance(knot2, tuple):
        raise ValueError("knot2 must be tuple type")
    return ((knot1[0] - 1) <= knot2[0]) and (knot2[0] <= (knot1[0] + 1))\
        and ((knot1[1] -1) <= knot2[1]) and (knot2[1] <= (knot1[1] + 1))

if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        lines = inputFile.readlines()
        head = (0,0)
        tail = (0,0)
        tailTraveledPos = set()
        tailTraveledPos.add(tail)
        for line in lines:
            moveTokens = line.strip().split()
            direction = moveTokens[0]
            length = int(moveTokens[1])
            for i in range(length):
                if direction == "R":
                    head = (head[0] + 1, head[1])
                elif direction == "L":
                    head = (head[0] - 1, head[1])
                elif direction == "U":
                    head = (head[0], head[1] + 1)
                elif direction == "D":
                    head = (head[0], head[1] - 1)
                if not areKnotsAdjacent(head, tail):
                    horzDelta = head[0] - tail[0]
                    vertDelta = head[1] - tail[1]
                    if horzDelta == 0:
                        if vertDelta == 0:
                            print("head and tail are at the same point")
                        else:
                            if vertDelta < 0:
                                tail = (tail[0], tail[1] - 1)
                            else:
                                tail = (tail[0], tail[1] + 1)
                    else:
                        if vertDelta == 0:
                            if horzDelta < 0:
                                tail = (tail[0] - 1, tail[1])
                            else:
                                tail = (tail[0] + 1, tail[1])
                        else:
                            if vertDelta < 0:
                                if horzDelta < 0:
                                    tail = (tail[0] - 1, tail[1] - 1)
                                else:
                                    tail = (tail[0] + 1, tail[1] - 1)
                            else:
                                if horzDelta < 0:
                                    tail = (tail[0] - 1, tail[1] + 1)
                                else:
                                    tail = (tail[0] + 1, tail[1] + 1)
                    tailTraveledPos.add(tail)
        print(len(tailTraveledPos))
    finally:
        inputFile.close()