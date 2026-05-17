def calPoints(operations):
    score=[]
    last=len(score)-1
    result=0

    def addition(score):  
        sum1 = score[last] + score[last-1]
        score.append(sum1)

    def D(score):
        double=2 *(score[last])
        score.append(double)

    def C(score):
        score.pop()
        
    for i in range(0, len(operations)):
        if operations[i] == "+":
            addition(score)
        elif operations[i] == "D":
            D(score)
        elif operations[i] == "C":
            C(score)

        else:
            num=int(operations[i])
            score.append(num)

    for i in range(len(score)):
        result = result + score[i]
    return result

print(calPoints(["5","-2","4","C","D","9","+","+"]))

