import re

################################################################################
########### IMPORTANT VARIABLES
################################################################################

file = 'chat.txt'
user = 'Diego 328'
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

    header_pattern = '\d{1,2}\/\d{1,2}\/\d{2} \d{2}:\d{2}\s-\s'
    regexp = re.compile(header_pattern)
    # Check for header format
    if (regexp.search(line)):
        head = True
        # Message starts from the second ':' char until the end.
        msg = line[line.rindex(':') + 1:].replace('\n', ' ')
    else:
        msg = line.replace('\n', ' ')


    return (head, msg)

################################################################################
########### EXECUTION SEQUENCE
################################################################################

# Open the chat
chat = open(file, encoding='utf8')

# Filter every line from the specific user.
lines = chat.readlines()
lines = [x.lower() for x in lines if user in x]
line_count = len(lines)

# Filter multimedia messages
mm_string = '<multimedia omitido>'
lines = [x.lower() for x in lines if mm_string not in x]

# Extract the messages
pos = 0
msg_list = []
full_msg = ''

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
print('\nLas {} intervenciones más populares de {}, tras analizar {} mensajes son:\n'.format(top_n, user, line_count))
for pos in range(len(top)):
    print('#{} con {} apariciones:\n  "{}"'.format(pos + 1, msg_counter[top[pos]], top[pos]))
