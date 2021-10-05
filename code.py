# Fiat-Shamir Protocol
import random
from Crypto.Util.number import *

if __name__ == "__main__":
	p = getPrime(15)
	q = getPrime(15)
	n = p*q

	secret = "Earth is flat"
	# Convert message in to decimal form.
	S = bytes_to_long(b"Earth is flat")

	# v is public key.
	v = pow(S, 2, n)

	count = 0
	no_of_iterations = 5
	print("Message		= ", S)
	print("Prime 		= ", n)

	for i in range(no_of_iterations):
		# Alice chooses a random r in the interval (1 ,n-1) and sends x=(r**2)%n to Bob.
		r = random.randint(1, n-1)
		x = pow(r, 2, n)

		# Bob randomly selects a bit e (0 or 1) and sends it to Alice.
		e = random.randint(0, 1)

		# Alice computes y=(r*(S**e))%n and sends it back to Bob.
		y = (r*(S**e))%n

		# Bob checks the equality y**2 == (x*(v**e))%n. If it is true, it proceeds to the next round of 
		# the protocol, otherwise the proof is not accepted.
		print("=====================================================")
		print("Iteration "+str(i+1))
		print("r 		= ", r)
		print("x		= ", x)
		print("e 		= ", e)
		print("y 		= ", y)
		print("y**2 		= ", pow(y,2,n))
		print("(x*(v**e)) 	= ", (x*(v**e))%n)

		print("\nIteration "+str(i+1)+":	", end="")
		if(pow(y,2,n) == (x*(v**e))%n):
			print("Passed")
			count += 1
		else:
			print("Failed")

		print("=====================================================")

	if(count == no_of_iterations):
		print("Alice has the secret.")
	else:
		print("Alice does not have the secret.")

