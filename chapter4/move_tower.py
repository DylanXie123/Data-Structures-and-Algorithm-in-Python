def moveTower(height, fromPole, toPole, withPole):
    if(height >= 1):
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


def moveDisk(fromPole, toPole):
    print('move disk from ', fromPole, ' to ', toPole)

moveTower(5, 'A', 'B', 'C')