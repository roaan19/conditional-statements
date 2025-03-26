m=input("what is the capital of india ? ")
if m=="delhi":
    print("correct")
else:
   print("incorrect")

m=input("what is the capital of maharastra ? ")
if m=="mumbai":
    print("correct")
else:
   print("incorrect")

#profit and loss
sp=int(input("enter the selling price "))
cp=int(input("enter the cost price "))

if sp>cp:
    print("profit")
    pp=sp-cp
    print(pp)
else:
    print("loss")

#even and odd
m=int(input("enter the number "))
if (m%2==0):
    print("the number is even ")
else:
    print("the number is odd")