# Open CSV file as file object
f = open("./football.csv", "r")

# Will be used to store our team names and goal metrics
data = {}

# Store first line as field name headers
header = f.readline()

# Parse each line of CSV and store results in 'data'
for line in f:
	text_line = line[:len(line)-1]    # remove newline character at end of each line
	list_line = text_line.split(',')  # split text into list delimited by commas
	team_name = list_line[0]          # first element is the team's name

	# difference between 6th and 7th elements is the goal spread metric we want
	# we want to take the absolute value of this difference to figure out the 
	# lowest spread, rather than the lowest 
	goal_spread = abs(int(list_line[5]) - int(list_line[6]))
	data[goal_spread] = team_name

# Print name of team with smallest difference in 'for' and 'against goals'
print(data[min(data)])