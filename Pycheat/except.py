#!/usr/bin/env python3
my_dict = {"a":1, "b":2, "c": 3}
try:
    value = my_dict[4]
except KeyError:
    print("That key does not exist!!!")
except IndexError:
    print("This index does not exist")
except:
    print("Some other problem happened")
