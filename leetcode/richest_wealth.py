def richest_customer(accounts):
    row_total=[0]*len(accounts)
    rows=len(accounts)
    cols=len(accounts[0])
    for i in range(rows):
        for j in range(cols):
            row_total[i]=row_total[i]+accounts[i][j]

    maximum=max(row_total)
    return maximum

accounts=[
    [1,2,3],
    [4,5,6]
]

print(richest_customer(accounts))