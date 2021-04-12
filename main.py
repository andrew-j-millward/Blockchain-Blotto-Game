import sys

def simulate(network_vector, attack_vector):
	pass

if __name__ == "__main__":
	args = sys.argv
	if len(args) > 1:
		if args[1] == "-h":
			print("\nThe following arguments are used to specify system parameters:\n\n\tpython main.py <Diagnostics -h -v> <Number of cryptocurrencies> <Total network hashing power TH/s>\n")
	if len(args) == 3 or len(args) == 4:
		
		# Valid input
		if args[-1].isnumeric() and args[-2].isnumeric():
			n = int(args[-2])
			hash_power = int(args[-1])

			# Even distribution of mining efforts...
			network_vector = [1/n for i in range(n)]
			network_hash = [hash_power*network_vector[i] for i in range(n)]
			print(network_vector, network_hash)

		# Invalid input
		else:
			print("Invalid input...")
