
double = [ i*2 for i in range(0,10)]
print(double)

friends = ["ram", "shyam","mohan", 'sohan']
invite_with_s = [name for name in friends if name.startswith("s") ]
print(invite_with_s)
doube = [ i*2 for i in range(10)]
print(doube)
keyPair = {i: i * 2 for i in range(10)}
print(keyPair)

totalSum = lambda x,y: x+y
print(totalSum( 6,6))
