# Python---Traffic-Light
Analyzing the functionality of a traffic light with Python. 

## Description:
A traffic light needs to be checked. 
For that, a camera which will take a picture of the traffic light every 5 seconds is set.
The data is stored, processed and then sent to the transit state department for analysis. 
The analysis needs to be done using Python.

### Considerations:
1) The processed data is stored as codes, where each code represent a color, as follows:  
**1, 0, 0, 0** means *red*.  
**0, 1, 0, 0** means *yellow*.  
**0, 0, 1, 0** means *green*.  
**0, 0, 0, 1** means *green left arrow*.  
**0, 0, 0, 0** means *no light is on*.

2) For the traffic light to be considered as working correctly, it can only switch in two different sequences, as follows:

   **Red -> Yellow -> Green -> Yellow -> Red (and repeat)**

   **Red -> Yellow -> Green left -> Green -> Yellow -> Red (and repeat)**

4) *Since the camera takes a picture every 5 seconds, the data will have repeated traffic light states (colors) in tandem.*

   For example:

   If the total time the traffic light stays in red state is 30 seconds, and the camera takes the picture from the moment the light turns red, then most probably in the data 6 consecutive red states will be recorded.

5) *The traffic light blinks only for the two green states.*

   This means, that it is possible to get no_light_on between the greens, and between a green and yellow.

## The challenge: *Creating an applicable python code, which determines if the traffic light works correctly*
### General approach:
The general idea of the code is the following:
  1) Open the data accordingly, process it and convert it to a list.
  2) Define a rule dictionary which contains the valid transitions based on the acceptable sequences of a working traffic light.
  3) Define a for loop function which compares the data with the valid transitions, and therefore determines if the traffic light works. This loop will also include edge scenarios, like multiple lights turned on at the same time, traffic light off or stuck in a particular light, green lights not blinking or if the binary color code data is unknown (for example 0,1,5,J). 

## The Code
The main script ("analyze_traffic_light.py) is a for loop function, whith Common-Line Interface, which compares the data with a dictionary containing the possible light switches (based on the correct patterns defined before), and returns either "Traffic light works" or an AssertionError with a customed message that tells you what the error is:

- If more than one lights are on, it returns: "Attention! More than one light turned on near index {i}: traffic light went from {current_color} to {next_color}.
- If there is an invalid transition (for example from green to red), it returns: "Attention! Invalid transition detected at index {i}: transition from {current_color)} to {next_color}."
- If the traffic light gets stuck in a particular light, it returns: ""Attention! The traffic light is STUCK in {current_color}!"
- If the traffic light shuts down, it returns: ""Attention! The traffic light is SHUT DOWN!"
- If the green or green left lights stop blinking, it returns: "Attention! {green or green_left} is not blinking."
- If an unknown binary code is detected (for example 0,1,5,J) current_code/next_code will be replaced by UNKNOWN, for example: "Attention! More than one light turned on near index {i}: traffic light went from {current_color} to {UNKNOWN}.

Pytest script was included (analyze_traffic_light_pytest.py), which checks all the conditions and functionalities of the main script. 
**PLEASE NOTE**: This file requires of previous pytest module installation to run. To install pytest, please enter "pip install pytest" and run it.

## How to Use the Code:
1. Download the following files and save them in the same folder:  
   - `analyze_traffic_light.py`  
   - `analyze_traffic_light_pytest.py`  
   - `traffic_light_data.txt`  
2. Open your preferred **IDE (Integrated Development Environment)**.
4. Open a new terminal and make sure you are in the directory where the files have been saved.
5. To run the main script (analyze_traffic_light.py), use the following command:

   python analyze_traffic_light.py traffic_light_data.txt
7. Press Enter to execute the program.
8. To run the pytest script (analyze_traffic_light_pytest.py) repeat steps 5 and 6, but change the command to:

   *python analyze_traffic_light_pytest.py*.

### Results:
Given the data sample (traffic_light_data.txt) we can conclude that the traffic light works correctly. 

### Testing the code a little bit more:
If you would like to run the script with more files, and check the results with tampered data (multiple colors, traffic light off, etc), you can go to the branch "Tampered-data", download the files, and check the results you get when running the main script with those files. 
The instructions are the same, but the command will change depending on the file you use, ie:
*python analyze_traffic_light.py tampered_data_xxxxx.txt*

If you would like to see the first version of the code, which ONLY can detect if there are invalid transitions or if the traffic light works and doesn't have CLI, you can check the "First-code- branch.
