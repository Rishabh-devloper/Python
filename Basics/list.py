# a = [1,-30 ,-20 ,7,10,-4,5,-6,3]
# m=[]
# min=[]
# for i in a:
#     if i<0:
#         min.append(i)
#     else:
#         m.append(i)
# print(min)
# print(m)

"""                                               Mean Of List                                                               """

# a=[1 ,2,3,4 , 5 ,6]
# sums=0
# for i in a:
#     sums= sums+i
# avg = sums / len(a)
# print(avg)

"""                            greatest eleemnt in list                                                                   """
# a=[30 , 50 ,67, 89, 20 ,4 ,29,]
# maxx=a[0]
# secondlargest=a[0]
# index=0
# for i in range(len(a)):
#     if maxx<=a[i]:
#         secondlargest=maxx
#         maxx=a[i]
#         index=i


# print(f"largest {maxx} second largest {secondlargest}")



"""                          checvk the list is shorted or not                                                  """
a=[0 , 50 ,67, 89, 20 ,4 ,29]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("not sorted")
        break