def conatainsDuplicate(list1):
    seen =set()
    dup=0
    for num in list1:
        if num in seen:
            dup=dup+1
        seen.add(num)

    if dup!= 0:
        return True
    else:
        return False

            
   


print(conatainsDuplicate([11,11,12]))