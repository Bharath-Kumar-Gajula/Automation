def interchange_first_and_last_element(lst):
    ty = type(lst)
    print(ty)
    if ty == "list":
        print("*****")
    elif ty == 'dict':
        print("**")
        print(type(lst))
        lst1=[]
        for i in lst:
            a = lst[i]
            lst1.append(a)
        lst = lst1

    end = lst[0]
    lst[0] = lst[-1]
    lst[-1] = end
    return lst

print(interchange_first_and_last_element({"Hello" :"Hi", 1:2, 3:"bye"}))
