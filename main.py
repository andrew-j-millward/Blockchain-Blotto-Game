import sys, random
from numpy import dot

############################################
##    Compute Payoffs for Each Player     ##
############################################
def payoff(network_vector, attack_vector, payout_vector):
	for i in range(len(network_vector)):
		if attack_vector[i] > network_vector[i]:
			return (-100, 100)
	print(network_vector, payout_vector)
	return (dot(network_vector, payout_vector),0)

############################################
##         Maximize Network Profit        ##
############################################
def greedy_heuristic():
	pass

############################################
##         Optimize Attack Vector         ##
############################################
def attacker_heuristic(attack_vector, network_vector):
	min_i = -1
	min_dif = -1
	for i in range(len(network_vector)):
		if (min_dif == -1 or min_dif < network_vector[i]):
			min_dif = network_vector[i]
			min_i = i
	hash_power_attacker = sum(attack_vector)
	attack_vector = [0 for i in range(number_coins)]
	attack_vector[min_i] = hash_power_attacker
	return attack_vector

############################################
##       Blotto Simulator Function        ##
############################################
def simulate(number_coins, hash_power_network, hash_power_attacker):
	network_vector = [1/number_coins for i in range(number_coins)]
	network_hash = [hash_power_network*network_vector[i] for i in range(number_coins)]
	attack_vector = [0 for i in range(number_coins)]
	attack_vector[0] = hash_power_attacker
	payout_vector = [random.randrange(0,100)/100 for i in range(number_coins)]
	print(network_vector, network_hash)
	print(payoff(network_vector, attack_vector, payout_vector))
	print(attacker_heuristic(attack_vector, network_vector))

############################################
##             Input Parsing              ##
############################################
if __name__ == "__main__":
	args = sys.argv
	if len(args) > 1:
		if args[1] == "-h":
			print("\nThe following arguments are used to specify system parameters:\n\n\tpython main.py <Diagnostics -h -v> <Number of cryptocurrencies> <Total network hashing power TH/s> <Attacker hashing power TH/s>\n")
	if len(args) == 4 or len(args) == 5:
		
		# Valid input
		if args[-1].isnumeric() and args[-2].isnumeric() and args[-3].isnumeric():
			number_coins = int(args[-3])
			hash_power_network = int(args[-2])
			hash_power_attacker = int(args[-1])

			# Run the simulation on the given parameters...
			simulate(number_coins, hash_power_network, hash_power_attacker)

		# Invalid input
		else:
			print("Invalid input...")
