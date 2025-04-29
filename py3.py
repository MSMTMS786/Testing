# # IO
# openfile = open('myfile.txt','w')
# rewading=openfile.flush()
# print(rewading)


openfile = open('myfile.txt','a')
writing=openfile.write('Hello World\n'.capitalize())
print(writing)
openfile.close()

openfile = open('myfile.txt','r')
reading=openfile.read()
print(reading)


