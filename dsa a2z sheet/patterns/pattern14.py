def pattern14( n):
        for i in range(n):
            row_str = ""
            for j in range(i + 1):
                row_str += chr(65 + j)
            print(row_str)
pattern14(5)