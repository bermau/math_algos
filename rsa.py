from random import randint
import math

def is_prime(x):
	i = 2
	root = math.ceil(math.sqrt(x))
	while i <= root:
		if x % i == 0:
			return False
		i += 1
	return True


if __name__ == "__main__":
	p = int(input("Enter p: "))
	q = int(input("Enter q: "))
	n = p * q
	n1 = (p - 1) * (q - 1)

	print (n)
	print (n1)

	while True:
		r = randint(2,n1)
		if is_prime(r):
			break
	e = r
	print("e = %d" % e)

	d = (1 + n1)/e
	print("d = %d" % d)

	m = input("Enter message: ")
	for x in m:
		print (int(x));
	c = (pow(m, e)) % n
	print("Encrypted message = %d" % c)
	m1 = (pow(c, p)) % n
	print("Decrypted message = %d" % m1)