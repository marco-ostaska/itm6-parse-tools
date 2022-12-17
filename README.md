IBM Tivoli Monitoring 6 Simple Parse tools
---

This is a simple tool for parsing the output of some ITM6 commands.

requirements
----

Python 3+

Description
----

he script reads in the output of the tacmd viewsit command through the standard input stream and processes it line by line. The script then performs the following actions:

- Prints a line of underscores for visual separation
- Prints the first 4 lines of the input, which contain the name, full name, description, and type of the situation.
- Replaces certain strings in the formula line with their equivalent values and prints the resulting line.
- Prints a line of underscores for visual separation
- Prints the sampling interval and run at start up lines.
- Splits the distribution line into two lists: one for MSLs and one for agents. It then prints the name of the distribution followed by the lists of MSLs and agents.
- Prints a line of underscores for visual separation
- Prints the remaining lines of the input, which contain the text, action location, action selection, system command, true for multiple items, TEC severity, and TEC forwarding and destination.


Example
----

```
tacmd viewsit -s <situation> | python fmt_viewsit.py
```

This will parse the output of the tacmd viewsit command and display it in a formatted manner.

Customization
----
The script includes a dictionary called str_rpl that maps certain strings to their equivalent values. You can modify this dictionary to customize the output of the script. For example, you can change the string *EQ to = in order to display equal signs in the formula instead of ==.

Notes
----
- The script assumes that the input follows a specific format. If the input does not follow this format, the script may not produce the expected output.
- The script does not perform any error checking. It is the responsibility of the user to ensure that the input is valid and in the correct format.

