# traffic_light_data_analyzer.py

# Creating a rule-based dictionary for valid transitions, knowing that the only allowed sequences are:
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

def main(file_path):
    data = open_file(file_path)
    traffic_light_data = process_data(data)
    test_traffic_light(traffic_light_data)

# Opening the file
def open_file(file):
  with open(file, 'r') as f:
    return f.readlines()

data = open_file(file_path)

# Processing the data: removing '\n', splitting with commas and converting to int
def process_data(data):
  processed_data = []
  for line in data:
    stripped_line = line.strip()
    split_line = stripped_line.split(',')
    integer_line = [int(x) for x in split_line]
    processed_data.append(integer_line)
  return processed_data

traffic_light_data = process_data(data)

# Testing the traffic light
def test_traffic_light(traffic_light_data):
    for i in range(0, len(traffic_light_data) - 1):
        current_state = tuple(traffic_light_data[i])
        next_state = tuple(traffic_light_data[i + 1])

        assert next_state in rule_set.get(current_state, []), \
            f"Traffic light does not work. Invalid transition detected at index {i}: transition from {current_state} to {next_state}" 

    print("Traffic light works!")

# Calling the final function to test the traffic light:
test_traffic_light(traffic_light_data)

if __name__ == "__main__":
    main("traffic_light_data.txt")
