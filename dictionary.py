
# d= {
#     "name":"Rishabh",
#     "age":20,
#     "phn":9198921795,
#     2:100,
#     4:9000
# }

# d2 ={
#     1:9009,
#     20:700,
#     90:5678
# }
# sum =0
# for i in d2:
#     sum =sum +d2[i]
# print(sum)


a=[1,1,1,1,2,2,2,3,3,3,4,4,4,4,4,4,5,5,5]
d={}

for i in a:
    if i in d.keys():
        d[i]= d[i] +1
    else:
        d[i]=1
print(d)
