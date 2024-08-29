#lambda arguments: expression
#add = lambda a,b: a + b 
#print(add(3,5))

#square = lambda a: a * a
#print(square(4))

#numbers = [1,2,3,4,5]

#number =list(map(lambda a: 2 * a,numbers))
#print(number)

#if x>y give me x or else y value

#maximum = lambda x,y: x if x>y else y
#print(maximum(3,4))

lista=[6,3,7,-9,4]
coordinates = [(1,2),(3,1),(5,-1),(0,0)]
#sort it based on y value output is [(5,-1),(0,0),(3,1),(1,2)]
lista.sort()
coordinates.sort()
print(lista)
print(coordinates)
y=sorted(coordinates,key=lambda x: x[1] )
print(y)

x = lambda a,b: a - b
print(x(5,3))

numbers = [1,2,3,4,5,6]
out = [(lambda x:x*2)(x) for x in numbers]
print(out)