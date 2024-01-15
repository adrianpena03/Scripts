'''
Parse arbitrary logs

Collect logs (of any kind) and write a parser which 
pulls out specific details (domains, executable names, timestamps etc.)

1. Read the file
2. Extract Date/Time, End time, OS version, Hardware model
3. Save output to csv file
'''

log_data = {}

with open('log.txt', 'r') as f:
    for line in f:
        # Check if there is a colon in the line
        if ':' in line:
            # Split each line into a key and value, separate by first colon
            key, value = line.split(':', 1)

            # store these values into log_data (dictionary)
            log_data[key.strip()] = value.strip()

# Retrieve keys
date_time = log_data.get('Date/Time')
End_time = log_data.get('End time')

print("Date/Time:", date_time)
print("End time:", End_time)

# ------ Second Version bc why not -------

# with open('log.txt', 'r') as f:
#     new_txt = [line.strip().split(':', 1)for line in f]

#     for line in new_txt:
#         if 'Date/Time' in line:
#             print('Date/Time:', line[1].strip())
#         elif 'End time' in line:
#             print('End time', line[1].strip())
