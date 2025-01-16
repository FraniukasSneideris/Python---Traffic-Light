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
  3) Define a for loop function which compares the data with the valid transitions, and therefore determines if the traffic light works.  

## The Code
This code is a for loop function which compares the data with a dictionary containing the possible light switches (based on the correct patterns defined before), and returns either "Traffic light works" or "Traffic light does not work", and if it traffic light does not work, it also returns the index and color codes of the invalid transition found. 

**PLEASE NOTE**: The "analyze_traffic_light_pytest.py" requires of previous pytest module installation to run.

## Results:
Given the data sample (traffic_light_data)  we can conclude that the traffic light works correctly. 
