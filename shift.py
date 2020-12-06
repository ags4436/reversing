import string

def shift(x,shift,symbole):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    if(symbole=='+'):
	    for i in x:
	        if i.isupper() is True:
	            n.append(upper[(upper.index(i)+shift)%26])
	        elif i.islower() is True:
	            n.append(lower[(lower.index(i)+shift)%26])
	        elif i.isdigit() is True:
	            n.append(digits[(digits.index(i)+shift)%10])
    if(symbole=='-'):
	    for i in x:
	        if i.isupper() is True:
	            n.append(upper[(upper.index(i)-shift)%26])
	        elif i.islower() is True:
	            n.append(lower[(lower.index(i)-shift)%26])
	        elif i.isdigit() is True:
	            n.append(digits[(digits.index(i)-shift)%10])
    return n

text=input("Enter the Text need to be shifted: ")
shift_integer=int(input("Enter the shift (integer): "))
symbole=input("+ (or) -: ")
print("Shifted Text: ")
for i in shift(text,shift_integer,symbole):
	print(i,end="")
