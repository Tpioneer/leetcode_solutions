if __name__ == "__main__":
    # for i in range(n):
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     price, state = line.split()
    #     items.append((int(price),int(state)))
    # for i in range(m):
    #     line = sys.stdin.readline().strip()
    #     total, discount = line.split()
    #     discounts.append((int(total), int(discount)))
    items = [(1,1),(2,1),(3,0)]
    dicounts = [(5,1)]
    sum1 = 0
    for i in items:
        sum1 += i[0] if i[1] == 0 else i[0]*0.8
    origin = sum([i[0] for i in items])
    for i in range(len(dicounts)-1, 0):
        if origin > dicounts[i][0]:
            sum2 = min(sum2, sum2-dicounts[i][1])
    print(min(sum1,sum2))