import sys

line = sys.stdin.readlines()

# Name, Full Name, Description, Type
for i in range(0,4):
    print("_"*150)
    print(line[i].rstrip())

# Formula
str_rpl = {
        "*EQ":"==",
        "*VALUE":"",
        "*OR": "\n OR",
        "*AND": "AND",
        "*IF": "\n",
        "*GT": ">",
        "*GE": ">=",
        "*LT": "<",
        "*LE": "<=",
        "*NE": "!=",
        "*UNTIL": "\nUNTIL",
        "*STR": "SubSet_Of_A_String",
        "*SCAN": "Scan_String"
        }

for to_rpl, new_vl in str_rpl.items():
    line[4] = line[4].replace(to_rpl, new_vl)
print("_"*150)
print(line[4])


# Sampling Interval, Run At Start Up
for i in range(5,7):
    print("_"*15)
    print(line[i].rstrip())


# Distribution
lst = line[7].rstrip().split(" : ")[1].split(",")

msl = [i for i in lst if ":" not in i ]
ag = [i for i in lst if ":" in i ]

print ("{} :".format(line[7].rstrip().split(" : ")[0].split(",")[0]))
if msl:
    print ("MSL(s): {}".format(", ".join(msl)))
if ag:
    print("Agent(s): {}".format(", ".join(ag)))

# Text
# Action Location
# Action Selection
# System Command
# True For Multiple Items
# TEC Severity
# TEC Forwarding
# TEC Destination

for i in range(8,len(line)):
    print("_"*150)
    print(line[i].rstrip())
