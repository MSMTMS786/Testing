
# # Python program to illustrate
# with open('myfile.txt', 'r') as f:

#     # print(type(f))
#     # f.write('Hello, World  !')
#     # f.write('\n')
#     # f.write('Python')
#     f.seek(2) # places the cursor at the 5th position

#     data=f.read(5)
#     print(data)
def allfunc(func,val):
    return func(val)

#Lambda function
double = lambda x: x * 2
avg= lambda x,y,z: (x+y+z)/2
print("Avg = ",avg(2,3,4))
print("Double = ",double(5))
print(allfunc(double,5))