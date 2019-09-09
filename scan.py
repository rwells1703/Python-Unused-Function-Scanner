import re, sys

def get_match_positions(text, regex):
    if regex == "":
       return []

    matches = []

    start_pos = 0
    again = True

    while again:
        search = re.search(regex, text[start_pos:])

        if search == None:
            again = False
        else:
            span = search.span()
            matches.append((start_pos + span[0], start_pos + span[1]))
            start_pos = start_pos + span[1]

    return matches

def get_function_identifier(definition):
    args_start = re.search("\(", definition)
    if args_start != None:
        return definition[4:args_start.span()[0]]
    return None

def check_identifier_usage(text, definition_positions):
    unused = []

    for d in definition_positions:
        identifier = get_function_identifier(text[d[0]:d[1]])
        matches = get_match_positions(text, identifier)

        count = 0
        for m in matches:
            if not text[m[0]-4:m[0]-1] == "def":
                count += 1
        
        if count == 0:
            unused.append(identifier)

    if len(unused) == 0:
        print("No problems in '" + sys.argv[1] + "' , all defined functions are used.")
    else:
        for u in unused:
            print("Warning, '" + u + "' is an unused function!")


if sys.argv[1] == None:
    print("Please pass in the path to a python script to scan for unused functions.")
    exit()

text_file = open(sys.argv[1], "r")
text = text_file.read()
text_file.close()

definition_positions = get_match_positions(text, "def (.)+\((.)*\):")
check_identifier_usage(text, definition_positions)