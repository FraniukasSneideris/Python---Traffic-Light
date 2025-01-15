# Data which produces the following output "Traffic light might be getting stuck on yellow."
traffic_light_data = [
    [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0],\
    [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0],\ 
    [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0],\
    [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0],\
    [0, 1, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]
]

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

# We define the color strings based on the color codes, so that the function can print the name of the color if the traffic light is stuck
# This step is unnecesary, but it makes the output easier to understand in case of stuck
color_map = {
    (1, 0, 0, 0): "red",
    (0, 1, 0, 0): "yellow",
    (0, 0, 1, 0): "green",
    (0, 0, 0, 1): "green_left",
    (0, 0, 0, 0): "no_light_on"
}

# Defining the function 
# The number of repeated states that determine the threshold has been arbitrarily chosen to be 10
def is_traffic_light_working(traffic_light_data, rule_set, stuck_threshold=10): 

    traffic_light_works = True  
    stuck_counter = 1  # Counter for states in a row (repeated states)

    for i in range(len(traffic_light_data) - 1):
        current_state = tuple(traffic_light_data[i])
        next_state = tuple(traffic_light_data[i + 1])

        # The following if checks if the transitions are valid based on the rule_set
        if next_state not in rule_set.get(current_state, []):
            print(f"Traffic light does not work: Invalid transition detected at index {i}.")
            traffic_light_works = False
            return traffic_light_works

        # The following if checks if there are stuck states (more than 10 repeated states)
        if next_state == current_state:
            stuck_counter += 1
            if stuck_counter >= stuck_threshold:
                print(f"Traffic light might be getting stuck on {color_map[current_state]}.")
                break
        else:
            stuck_counter = 1  # The counter resets if the state changes

    if traffic_light_works and stuck_counter < 10:
        print("Traffic light works properly.")
        
# Using the function
is_traffic_light_working(traffic_light_data, rule_set, stuck_threshold=10)
