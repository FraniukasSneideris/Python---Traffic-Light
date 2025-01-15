# Opening the file
with open(file_path, 'r') as f:
  data = f.readlines()

# Processing the data: removing '\n', splitting with commas and converting to int
processed_data = []
for line in data:
  stripped_line = line.strip() 
  split_line = stripped_line.split(',')  
  integer_line = [int(x) for x in split_line]  
  processed_data.append(integer_line)  

traffic_light_data = processed_data

# Defining traffic light states
red = [1, 0, 0, 0]
yellow = [0, 1, 0, 0]
green = [0, 0, 1, 0]
green_left = [0, 0, 0, 1]
no_light_on = [0, 0, 0, 0]

# Creating a rule-based dictionary for valid transitions, knowing that the only allowed sequences are:
# red, yellow, green, yellow, red 
# red, yellow, green_left, green, yellow, red
# ONLY green and green_left blink
rule_set = {
    tuple(red): [tuple(yellow), tuple(red)],
    tuple(yellow): [tuple(green), tuple(red), tuple(green_left), tuple(yellow)],
    tuple(green): [tuple(yellow), tuple(no_light_on), tuple(green)],
    tuple(green_left): [tuple(green), tuple(no_light_on), tuple(green_left)],
    tuple(no_light_on): [tuple(yellow), tuple(green), tuple(green_left), tuple(no_light_on)]
           }

# Creating the final for loop which determines if the traffic light works
traffic_light_works = True

for i in range(0, len(traffic_light_data) - 1):
  current_state = tuple(traffic_light_data[i])
  next_state = tuple(traffic_light_data[i + 1])
  if next_state not in rule_set.get(current_state, []):
    traffic_light_works = False
    print('Traffic light does not work')
    break
else:
  print('Traffic light works')
