# CLI-enhanced analyze_traffic_light.py

import argparse

# Creating a rule_set dictionary for valid transitions, knowing that the only allowed sequences are:
# red, yellow, green, yellow, red
# red, yellow, green left, green, yellow, red
# ONLY green and green left blink
rule_set = {
    (1, 0, 0, 0): [(0, 1, 0, 0), (1, 0, 0, 0)], # red -> yellow or red
    (0, 1, 0, 0): [(0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0)], # yellow -> green, red, green left, or yellow
    (0, 0, 1, 0): [(0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 1, 0)], # green -> yellow, no light on, or green
    (0, 0, 0, 1): [(0, 0, 1, 0), (0, 0, 0, 0), (0, 0, 0, 1)], # green left -> green, no light on, or green left
    (0, 0, 0, 0): [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0)]  # no light on -> yellow, green, green left, or no light on
}

# code_to_color dictionary for multiple lights
code_to_color = {
    tuple([1, 1, 0, 0]): "RED + YELLOW", tuple([1, 0, 1, 0]): "RED + GREEN", tuple([1, 0, 0, 1]): "RED + GREEN LEFT",
    tuple([0, 1, 1, 0]): "YELLOW + GREEN", tuple([0, 1, 0, 1]): "YELLOW + GREEN LEFT", tuple([0, 0, 1, 1]): "GREEN + GREEN LEFT",
    tuple([1, 1, 1, 0]): "RED + YELLOW + GREEN", tuple([0, 1, 1, 1]): "YELLOW + GREEN + GREEN LEFT", tuple([1, 1, 1, 1]): "ALL LIGHTS ON",
    tuple([0, 0, 0, 0]): "No Light On", tuple([1, 0, 0, 0]): "Red", tuple([0, 1, 0, 0]): "Yellow", tuple([0, 0, 1, 0]): "Green", tuple([0, 0, 0, 1]): "Green Left"
}

# Defining color string only for when repeated states or shut down
code_to_stuck_color = {
    tuple([0, 0, 0, 0]): "SHUT DOWN",
    tuple([1, 0, 0, 0]): "STUCK in Red",
    tuple([0, 1, 0, 0]): "STUCK in Yellow",
    tuple([0, 0, 1, 0]): "STUCK in Green",
    tuple([0, 0, 0, 1]): "STUCK in Green Left",
}

# Defining greens list for testing if greens blink correctly
greens = [tuple([0, 0, 1, 0]), tuple([0, 0, 0, 1])]

# MAIN
def main(file):
    data = open_traffic_light_file(file)
    traffic_light_data = process_traffic_light_data(data)
    analyze_traffic_light(traffic_light_data)

# Opening the file
def open_traffic_light_file(file):
    with open(file, 'r') as f:
        return f.readlines()

# Processing the data: removing '\n', splitting with commas, and converting to int
def process_traffic_light_data(data):
    processed_data = []
    for line in data:
        stripped_line = line.strip()
        split_line = stripped_line.split(',')
        integer_line = [int(x) for x in split_line]
        processed_data.append(integer_line)
    return processed_data

# Defining a threshold for stuck and max greens (for lack of blinking)
stuck_threshold = 10
max_greens = 6

# Testing the traffic light
def analyze_traffic_light(traffic_light_data):
    light_count = 0
    green_count = 0

    for i in range(0, len(traffic_light_data) - 1):
        current_state = tuple(traffic_light_data[i])
        next_state = tuple(traffic_light_data[i + 1])

        # Detects more than one light at the same time
        assert sum(current_state) <= 1 and sum(next_state) <= 1, \
            f"Attention! More than one light turned on near index {i}: traffic light went from {code_to_color.get(current_state, 'UNKNOWN')} to {code_to_color.get(next_state, 'UNKNOWN')}."
    
        # Detects invalid transitions
        assert next_state in rule_set.get(current_state, 'UNKNOWN'), \
            f"Traffic light does not work. Invalid transition detected at index {i}: transition from {code_to_color.get(current_state, 'UNKNOWN')} to {code_to_color.get(next_state, 'UNKNOWN')}."

        # Detects if traffic light gets stuck or shuts down
        if current_state == next_state:
            light_count += 1
            assert light_count < stuck_threshold, f"Attention! The traffic light is {code_to_stuck_color.get(current_state, 'UNKNOWN')}!"
        else:
            light_count = 0

        # Detects green light not blinking
        if current_state in greens and current_state == next_state:
            green_count += 1
            assert green_count <= max_greens, f"Attention! {code_to_color.get(current_state, 'UNKNOWN')} is not blinking."
        else:
            green_count = 0

    print("Traffic light works!")

# CLI implementation
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze traffic light behavior.")
    parser.add_argument("file", help="Path to the traffic light data file.")
    args = parser.parse_args()

    main(args.file)
