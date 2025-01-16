import pytest
from traffic_light_data_analyzer import process_data, analyze_traffic_light


# Test for process_data()
def test_process_data():
    data = ["1,0,0,0\n", "0,1,0,0\n", "0,0,1,0\n"]
    expected_result = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

    result = process_data(data)

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
