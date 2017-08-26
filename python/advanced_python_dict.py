import re

def read_csv(file):
	f = open(file, "r")
	first_line = f.readline()
	first_line = re.sub('\n', '', first_line)
	headers = re.split(',\s?', first_line)
	data = []
	for line in f:
		text_line = re.sub('\n', '', line)
		row = re.split(',', text_line)
		data.append(row)
	f.close()
	return (headers, data)

# Q6
def get_dict_last_name():
	data_list = read_csv('./faculty.csv')[1]
	faculty_dict = {}
	for row in data_list:
		full_name = row[0].split()
		last_name = full_name[len(full_name) - 1]
		if last_name not in faculty_dict:
			faculty_dict[last_name] = [row[1:]]
		else:
			faculty_dict[last_name] = faculty_dict[last_name] + [row[1:]]
	return faculty_dict

#Q7
def get_dict_full_name():
	data_list = read_csv('./faculty.csv')[1]
	faculty_dict = {}
	for row in data_list:
		full_name = tuple(row[0].split())
		faculty_dict[full_name] = row[1:]
	return faculty_dict

#Q8
def print_dict_sorted(dict):
	sorted_keys = sorted(dict.keys(), key=lambda k: k[len(k)-1])
	for key in sorted_keys:
		print(key, " : ", dict[key])

def print_dict(dict):
	for key, val in dict.items():
		print(key, " : ", val)


###################################
faculty_dict = get_dict_full_name()

#print_dict(get_dict_last_name())  # Q6 answer
#print('\n')
#print_dict(faculty_dict)          # Q7 answer
#print('\n')
#print_dict_sorted(faculty_dict)   # Q8 answer