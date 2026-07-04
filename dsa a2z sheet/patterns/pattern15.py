def pattern15(n):
    for i in range(n,0,-1):
            row_str=''
            for j in range(i):
                row_str+=chr(65+j)
            print(row_str)
pattern15(4)