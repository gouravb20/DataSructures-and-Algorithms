                                                                                                                                                            def removeDuplicates(i, count, var):
    if var == q[i] and count == 1:
        res.pop()
        removeDuplicates(i+1, count + 1, res[-1])
    elif count > 1:

    else:
        res.append(q[i])
        removeDuplicates(i+1, 1)




q = [1,2,3,5,5,6,6]
res = []
print(q)