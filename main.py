import sys, random, pylab
import matplotlib.pyplot as plt
from numpy import dot
##pylab.xlabel ('Time')
##pylab.plot (timeData, moleculesA)
#fig1 = figure()
#ax = fig1.add_subplot(111)
#ax.grid(True)
#ax.set_title("Whatever Model")
##xlabel('time')
##ylabel('Concentrations')
##ax.legend(loc='lower right')
##show()
#ax.plot(t, Ns)
##plot(t, np.sin(0.3*y))
#xlabel('time', fontsize=14)
#ylabel('population', fontsize=14)
#savefig("Population",fmt="png",bbox_inches='tight', pad_inches=0.03,dpi=300)
#plt.show()


############################################
##   FP Typecasting - Input Validation    ##
############################################
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

############################################
##           Varience Function            ##
############################################
def marketAdjust(payout_vector):
	bias = 70 # Averaged rate of market return over longer time
	random_adj_vector = [(1+((random.randrange(0,1000)+bias-500)/1000000))*payout_vector[i] for i in range(len(payout_vector))]
	return random_adj_vector

############################################
##    Compute Payoffs for Each Player     ##
############################################
def payoff(network_vector, attack_vector, payout_vector):
	for i in range(len(network_vector)):
		if attack_vector[i] > network_vector[i]:
			return (-100, 100)
	print(network_vector, attack_vector, payout_vector)
	return (dot(network_vector, payout_vector), dot(attack_vector, payout_vector))

############################################
##         Maximize Network Profit        ##
############################################
def greedy_heuristic(network_vector, attack_vector, payout_vector):
	adj_payout_vector = [sum(payout_vector)/len(payout_vector) for i in range(len(payout_vector))]
	adj_network_vector = [network_vector[i]/(payout_vector[i]/adj_payout_vector[i]) for i in range(len(network_vector))]
	size_adj = sum(network_vector)/sum(adj_network_vector)
	adj_network_vector = [adj_network_vector[i]*size_adj for i in range(len(adj_network_vector))]
	return (adj_network_vector, adj_payout_vector)

############################################
##         Optimize Attack Vector         ##
############################################
def attacker_heuristic(attack_vector, network_vector, payout_vector):
	old_i = -1
	for i in range(len(attack_vector)):
		if attack_vector[i] != 0:
			old_i = i

	min_i = -1
	min_dif = -1
	for i in range(len(network_vector)):
		if (min_dif == -1 or min_dif > network_vector[i]):
			min_dif = network_vector[i]
			min_i = i

	print(old_i, min_i)

	hash_power_attacker = sum(attack_vector)
	adj_attack_vector = [0 for i in range(number_coins)]
	adj_attack_vector[min_i] = hash_power_attacker

	# Shifting attacker focus artificially changes difficulty...
	adj_payout_vector = payout_vector
	adj_amt = payout_vector[old_i]/(network_vector[old_i]/(network_vector[old_i]+hash_power_attacker))-payout_vector[old_i]
	adj_payout_vector[old_i] += adj_amt
	adj_payout_vector[min_i] -= adj_amt
	if adj_payout_vector[min_i] < 1e-8:
		adj_payout_vector[old_i] += adj_payout_vector[min_i]-1e-8
		adj_payout_vector[min_i] = 1e-8
	return (adj_attack_vector, adj_payout_vector)

############################################
##       Blotto Simulator Function        ##
############################################
def simulate(number_coins, hash_power_network, hash_power_attacker, max_iter):

	# Within this game, each player will take turns playing. The network will
	# make the first move, followed by the attacker. After each round, the
	# payout will be determined. The game will go for 5 iterations or until
	# the attacker gains a majority in any coin.

	# Initialize vectors
	network_vector = [1/number_coins for i in range(number_coins)]
	network_vector = [hash_power_network*network_vector[i] for i in range(number_coins)]
	attack_vector = [0 for i in range(number_coins)]
	attack_vector[1] = hash_power_attacker
	payout_vector = [random.randrange(1,100)/100 for i in range(number_coins)]
	if (payoff(network_vector, attack_vector, payout_vector) == (-100,100)):
		return 0, network_vector, attack_vector, payout_vector

	for i in range(0,max_iter):
		network_vector, payout_vector = greedy_heuristic(network_vector, attack_vector, payout_vector)
		attack_vector, payout_vector = attacker_heuristic(attack_vector, network_vector, payout_vector)
		pay_tuple = payoff(network_vector, attack_vector, payout_vector)
		print(pay_tuple)
		if (payoff(network_vector, attack_vector, payout_vector) == (-100,100)):
			return i+1, network_vector, attack_vector, payout_vector
		payout_vector = marketAdjust(payout_vector)

	return i+1, network_vector, attack_vector, payout_vector

############################################
##             Input Parsing              ##
############################################
if __name__ == "__main__":
	args = sys.argv
	if len(args) > 1:
		if args[1] == "-h":
			print("\nThe following arguments are used to specify system parameters:\n\n\tpython main.py <Diagnostics -h> <Number of cryptocurrencies> <Total network hashing power TH/s> <Attacker hashing power TH/s>\n")
	if len(args) == 4 or len(args) == 5:
		
		# Valid input
		if (args[-1].isnumeric() and args[-2].isnumeric() and args[-3].isnumeric()) or (isFloat(args[-1]) and isFloat(args[-2]) and isFloat(args[-3])):

			print("Note: All payoff vectors are 1-payoff. This is a bug and needs to be fixed.")
			total_iterations = 0

			number_coins = int(args[-3])
			hash_power_network = float(args[-2])
			hash_power_attacker = float(args[-1])
			max_iter = 50

			# Run the simulation on the given parameters...
			total_iterations, end_network_vector, end_attack_vector, end_payoff_vector = simulate(number_coins, hash_power_network, hash_power_attacker, max_iter)

			# Print Results
			print("Simulator Results:")
			print("Total number of iterations (max: " + str(max_iter) + "): " + str(total_iterations))
			print("Ending Network Vector" + str(end_network_vector))
			print("Ending Attack Vector" + str(end_attack_vector))

		# Invalid input
		else:
			print("Invalid input...")
