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

6) *Also, sometimes between states transitions, no light will be recorded. This is because the traffic light blinks.*

   For example:

   ... Red - Red - No Light On - Red - Yellow - ...

## The challenge: *Creating an applicable python code, which determines if the traffic light works correctly*
### General approach:
The general idea of the code is the following:
  1) Open the data accordingly, process it and convert it to a list.
  2) Define the possible states of the traffict light as color:code.
  3) Define a rule dictionary which contains the valid transitions based on the acceptable sequences of a working traffic light.
  4) Define a for loop which compares the data with the valid transitions, and therefore determines if the traffic light works.  

## The Code
Two codes were created.

### Code A:
This code is a for loop which compares the data with a dictionary containing the possible light switches (based on the correct patterns defined before), and returns either "Traffic light works" or "Traffic light does not work". 
However, this code does not check for repeated states over a define threshold in tandem. I.e., if for example the traffic light is getting stuck in a state longer than it should, but still it changes to yellow (applicable transition), this wouldn't be detected. 

*Let's say that the expected maximum number of a single state in a row is 10.
If the camera suddenly registers any number over 10 of a single state, then we could conclude that maybe the traffic light is getting stuck.*

This is where the second code comes in.

### Code B:
This second code is a function called "is_traffic_light_working" which can be used with any traffic light data, switching rule, and maximum number of states in a row threshold (for now on, called "stuck_threshold").
The function permits 3 arguments:
    
  ***is_traffic_light_working(traffic_light_data, rule_set, stuck_threshold=n)***
    
  *where "n" is the maximum permited number of states in a row*

The function consists of a for loop and an if statement.

The for loop does two things:

a) it compares the data with the permitted rules, and determines if all sequences in the data are valid, and

b) it counts the amount of equal states in a row, and if this number excedes the stuck_threshold, it stops the for loop and returns "The traffic light might be getting stuck on *color*". 

The if statement only returns "The traffic light works properly." if all transitions are valid, and the the maximum number of states in a row in the data does not exceed the stuck_threshold.

*Please note:* I provided an additional line of code with an example of data which repeats the yellow state exceeding a threshold of 10, to check the functionality of the function.

## Results:
Given the data sample (traffic_light_data)  we can conclude that the traffic light works correctly. 
