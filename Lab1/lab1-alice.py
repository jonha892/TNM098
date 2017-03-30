#from __future__ import division
# Percent of zeros is simply 100 - returned value
# Should be 45-55% for a random sequence
def percentones(sequence):
	total = 0
	for num in sequence:
		if num == '1':
			total += 1
	return total * 100/(len(sequence)-1)

# Suspect values: more than 120, less than 80
# Also return their lengths
def runs(sequence):
	currlen = 1
	# Start from second number
	lengths = []
	for i, num in enumerate(sequence):
		if i != 0:
			if num != sequence[i-1] and num != '\n':
				lengths.append(currlen)
				currlen = 1
			else:
				currlen += 1
	return lengths # Length of this is total length of array

if __name__ == "__main__":
	# Loop through everything
	file = open("CoinToss.txt", "r")
	# Write a csv file with features
	output = open("cointoss.csv", "w")
	output.write("sequence,percentones,nruns,maxrunlenght\n")
	for i, line in enumerate(file):
		sequence = list(line)
		ones = percentones(sequence)
		runlist = runs(sequence)
		curroutput = [str(i),str(ones),str(len(runlist)),str(max(runlist))]
		output.write(",".join(curroutput))
		output.write('\n')
		if ones < 45 or ones > 55 or len(runlist) > 120 or len(runlist) < 80:
			print "Suspicious values found!"
			print "Ones:", percentones(sequence), "%, and runs total:", len(runlist)
