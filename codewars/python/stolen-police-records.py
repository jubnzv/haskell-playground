'''
https://www.codewars.com/kata/5a5bef7a5c770d08cd0032fa

A crime scene has been discovered, and among the evidence is a list of agents, with no apparent connection.

Your job in the records department is to match this list with police records to find an exact match.

Your function will receive a list as the first parameter, the stolen record, followed by a list of lists, the database.

A match is found only if it contains the same names in the same order, no more, no less. Your code should return None if the first parameter is an empty list. The database will always contain more than one list. A match should return "Match found". If no matches are found, your code should return "No matches found".

Example: agents(["John", "Sarah"], [["John", "Sarah"], ["Mary", "David"]]) == "Match found"
'''
def agents(list_found, list_records):
    if len(list_found) == 0: return None
    if len(list_records) == 0: return 'No matches'
    return ('No matches', 'Match found')[list_found in list_records]
