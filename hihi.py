input1=50

def bottom_n(input):
	temp=0
	for i in range(30):
		temp+=i
		if temp>=input:
			return i
def top_n(input):
	temp=0
	bottom = bottom_n(input)
	for i in range(bottom,0,-1):
		temp+=i
		if temp>=input:
			return i+input-temp

print bottom_n(input1)
print top_n(input1)