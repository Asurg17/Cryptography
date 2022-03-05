import math

# Find out answer
def checkRightSide(table, g, b, p):

	multiplier = pow(g, b, p)
	mpart = multiplier

	for i in range(1, b):

		if mpart in table:	
			print(i*b + table[mpart]) # x = x0*B + x1
			return

		mpart = (mpart * multiplier) % p

	print(0)

# Calculate all possible values of left size and save results in hash table
# we have h * X -> X = (g^x1)^-1 -> (g^x1)^-1 = g^x1^p-2 
# we can calculate: ((h%p * X%p) %p) -> h%p = h cause h is always less than p
# g^x1^(p-2) % p = ((g^(p-2) % p)^x1) % p 
def calculateLeftSide(table, h, g, b, p):
    	
	fPart = pow(g, p-2, p)
	sPart = fPart
    	
	for i in range(1, b):
    	
		# table[(pow(pow(g, p-2, p), i, p) * (h % p)) % p] = i
		# table[(pow(fPart, i, p) * h) % p] = i

		table[(sPart * h) % p] = i

		sPart =  (sPart * fPart) % p

	# print(table)
    	


# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(g, h, p, max_x):

	b = math.sqrt(max_x)

	hash_table = dict()

	calculateLeftSide(hash_table, h, g, int(b), p)
	checkRightSide(hash_table, g, int(b), p)



def main():
	
	p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
	g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
	h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
	
	max_x = 1 << 40 # 2^40

	discrete_log(g, h, p, max_x)

if __name__ == '__main__':
	main()












