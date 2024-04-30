with open('24.13.txt') as f:
    print(max([len(s) for s in f.readline().split('AXMM')]) + 6)