import re

def read_csv(file):
	f = open(file, "r")
	first_line = f.readline()
	first_line = re.sub('\n', '', first_line)
	headers = re.split(',\s?', first_line)
	data = []
	for line in f:
		text_line = re.sub('\n', '', line)
		row = re.split(',\s?', text_line)
		data.append(row)
	f.close()
	return (headers, data)


# Q1
def get_degree_freq(data, headers):
	field_num = headers.index("degree")
	freqs = {}
	for row in data:
		value = re.sub('[.]', '', row[field_num])
		values = value.split()
		if len(values) > 1:
			for val in values:
				if val not in freqs:
					freqs[val] = 1
				else:
					freqs[val] += 1
		else:
			if value not in freqs:
				freqs[value] = 1
			else:
				freqs[value] += 1

	return freqs


# Q2
def get_title_freq(data, headers):
	field_num = headers.index("title")
	freqs = {}
	for row in data:
		value = re.sub('is\s', 'of ', row[field_num])
		values = value.split()
		if value not in freqs:
			freqs[value] = 1
		else:
			freqs[value] += 1

	return freqs


# Q3
def get_email_list(data, headers):
	field_num = headers.index("email")
	email_list = [x[field_num] for x in data]
	return email_list


# Q4
def get_unique_domains(list):
	return set([ re.sub('.*@', '', x) for x in list if '@' in x ])


# Used to print markdown tables for Q1 and Q2
def print_markdown(col):
	total = 0
	print('| Title | Frequency |')
	print('| ----- | --------- |')

	for d in col:
		print("| " + str(repr(d)) + " | " + str(col.get(d)) + " |")
		total += col.get(d)

	print("| TOTAL | " + str(total) + " |")


#########################################

f = "./faculty.csv"
data_and_headers = read_csv(f)
headers = data_and_headers[0]
data = data_and_headers[1]

degrees = get_degree_freq(data, headers)
titles = get_title_freq(data, headers)
emails = get_email_list(data, headers)
unique_domains = get_unique_domains(emails)

#print_markdown(degrees) #Q1 answer 
#print_markdown(titles)  #Q2 answer
#print(emails)   #Q3 answer
#print(unique_domains)   #Q4 answer