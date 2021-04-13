import re

################################################################################
########### IMPORTANT VARIABLES
################################################################################

file = 'chat.txt'
top_n = 10

################################################################################
########### FUNCTIONS
################################################################################
def parseLine(line):
    '''
    Inputs a line, decides if it's the header or the body of the message. Returns a tuple.
    :param line: Line (string) to be parsed.

    :returns: Tuple - (True/False, String) Is header or not, and the message.
    '''

    head = False
    msg = ''

    header_pattern = '\d{1,2}\/\d{1,2}\/\d{2},{0,1} \d{1,2}:\d{2}\s-\s'
    regexp = re.compile(header_pattern)
    # Check for header format
    if (regexp.search(line)):
        head = True
        # Message starts from the second ':' char until the end.
        index = line.find(':')
        index = line.find(':', index + 1)
        msg = line[index+2:].replace('\n', '')
    else:
        msg = line.replace('\n', '')

    return (head, msg)

def goodbye():
    print()
    gb = '''
                ######################\n
                    See you around!\n
                ######################
             '''
    print(gb)
################################################################################
########### EXECUTION SEQUENCE
################################################################################
try:
    run = True

    print("Introduce name under which you've saved the user's contact.\nBe mindful it has to be the exact name! If you're not sure, take a look at the .txt to figure it out!")
    while(run):
        print("\n\tIf you'd like to exit the program, just press ENTER or press 'CTRL/CMD + C'\n")
        user = input('Name: ')

        if user == '':
            goodbye()
            break

        # Open the chat
        with open(file, encoding='utf8') as chat:

            # Filter every line from the specific user.
            lines = chat.readlines()
            user += ':'
            lines = [x.lower() for x in lines if user in x]
            line_count = len(lines)

            # Filter multimedia messages and erased messages - Lazy!
            mm_string = '<multimedia omitido>'
            lines = [x.lower() for x in lines if mm_string not in x]
            mm_string = 'este mensaje fue eliminado'
            lines = [x.lower() for x in lines if mm_string not in x]
            mm_string = '<media omitted>'
            lines = [x.lower() for x in lines if mm_string not in x]
            mm_string = 'this message was deleted'
            lines = [x.lower() for x in lines if mm_string not in x]
            mm_string = 'you deleted this message'
            lines = [x.lower() for x in lines if mm_string not in x]

            # Debugging
            # with open('lines.txt', encoding='utf8', mode='w') as dump:
            #    content = map(lambda x:x+'\n', lines)
            #    dump.writelines(lines)

            # Extract the messages
            pos = 0
            msg_list = []
            full_msg = ''

            lastHeader = False

            while(pos < len(lines)):
                isHeader, msg = parseLine(lines[pos])

                if isHeader:
                    # Save last full message
                    if full_msg != '':
                        msg_list.append(full_msg)
                    # Get the start of the new message
                    full_msg = msg
                else:
                    # Append the rest of the message to
                    full_msg += msg

                pos += 1

            # Select the top 3.
            msg_counter = {}
            for msg in msg_list:
                if msg in msg_counter:
                    msg_counter[msg] += 1
                else:
                    msg_counter[msg] = 1

            popular = sorted(msg_counter, key = msg_counter.get, reverse = True)

            top = popular[:top_n]


            # Spanish why yes
            print('\nThe {} most popular interventions from {}, after analyzing {} messages are:\n'.format(top_n, user, line_count))
            for pos in range(len(top)):
                print('#{} with {} coincidences:\n  "{}"'.format(pos + 1, msg_counter[top[pos]], top[pos]))

except KeyboardInterrupt:
    goodbye()
