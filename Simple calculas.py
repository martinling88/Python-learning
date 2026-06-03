n1=float(input("first number:"))
n2=float(input("second number:"))
op=(input("choose +,-,*,/:"))
if op=="+":
	print(n1+n2)
elif op=="-":
	print(n1-n2)
elif op=="*":
	print(n1*n2)
elif op=="/":
	print(n1/n2)
else:
	print("False format")