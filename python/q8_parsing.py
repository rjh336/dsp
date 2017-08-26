def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    f = open(filename, "r")
    data_list = []
    header = f.readline().split(',') # first line is header row
    for line in f:
        text_line = line[:len(line)-1]    # remove newline character at end of each line
        list_line = text_line.split(',')  # split text into list delimited by commas
        data_list.append(list_line)
    return data_list


def get_index_with_min_abs_score_difference(parsed_data):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    goal_spreads = []
    for line in parsed_data:
        goal_spread = abs(int(line[5]) - int(line[6]))
        goal_spreads.append(goal_spread)
    return goal_spreads.index(min(goal_spreads))
    
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    return parsed_data[index_value][0]

footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))
