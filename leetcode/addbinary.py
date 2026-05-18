def addBinary(a,b):
    s= ''
    c= '0'
    a = a[::-1]
    b = b[::-1]
    while len(a) != len(b):
        if len(a) > len(b):
            b = '0' + b
        else:
            a = '0' + a
    
    for i, j in zip(a,b):
        if (i == '0' and j == '0' and c == '0'):
            s = '0' + s
            c = '0'

        elif (i == '0' and j == '1' and c == '0') or (i == '1' and j == '0' and c == '0') or (i == '0' and j == '0' and c == '1'):
            s = '1' + s
            c = '0'
        
        elif (i == '1' and j == '1' and c == '0') or (i == '1' and j == '0' and c == '1') or (i == '0' and j == '1' and c == '1'):
            s = '0' + s
            c = '1'
        
        else:
            s = '1' + s
            c = '1'
        
    if (c == '1'):
        s = '1' + s
    return s

print(addBinary('11', '1'))