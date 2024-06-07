with open('24_4627.txt') as f:
    s = f.readline().replace('NPO', '*').replace('PNO', '*').replace('N', ' ').replace('P', ' ').replace('O', ' ')
    print(max(len(e) for e in s.split()))