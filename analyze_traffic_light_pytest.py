import pytest
from analyze_traffic_light import process_traffic_light_data, analyze_traffic_light


# Test for process_traffic_light_data()
def test_process_traffic_light_data():
    data = ["1,0,0,0\n", "0,1,0,0\n", "0,0,1,0\n"]
    expected_result = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

    result = process_traffic_light_data(data)

    assert result == expected_result, f"Expected {expected_result}, however result is {result}."


# analyze_traffic_light() against valid sequences:
def test_traffic_light_valid_sequences():
    valid_traffic_light_data_1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
    valid_traffic_light_data_2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

    try:
        analyze_traffic_light(valid_traffic_light_data_1)
        analyze_traffic_light(valid_traffic_light_data_2)
    
    except AssertionError:
      pytest.fail("test_traffic_light.py fails against valid data.")


# analyze_traffic_light() against invalid sequences:
def test_traffic_light_invalid_sequence():
    invalid_traffic_light_data = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0]]  # invalid transition no light on -> red on index 3

    with pytest.raises(AssertionError):
      analyze_traffic_light(invalid_traffic_light_data)

####
# analyze_traffic_light() detects SHUT DOWN:
def test_traffic_light_shutdown():
    shutdown_data = [
        [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],\
        [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    with pytest.raises(AssertionError):
      analyze_traffic_light(shutdown_data)

# analyze_traffic_light() detects STUCK:
def test_traffic_light_stuck():
    stuck_data = [
        [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0],\
        [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
    
    with pytest.raises(AssertionError):
      analyze_traffic_light(stuck_data)

# analyze_traffic_light() detects more than one light turned on:
def test_traffic_light_multiple_lights():
    multiple_lights_data = [
        [0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
    
    with pytest.raises(AssertionError):
      analyze_traffic_light(multiple_lights_data)

# analyze_traffic_light() detects Green or Green Left not blinking:
def test_traffic_light_blinks():
    green_not_blinking_data = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
    green_left_not_blinking_data = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]

    try:
        analyze_traffic_light(green_not_blinking_data)
        analyze_traffic_light(green_left_not_blinking_data)
    
    except AssertionError:
      pytest.fail("test_traffic_light.py fails against green/green left not blinking.")


def main():
    print("Executing tests with pytest...")
    pytest.main(["-v", "analyze_traffic_light_pytest.py"])


if __name__ == "__main__":
    main()
