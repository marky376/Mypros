#!/usr/bin/env python3
age = int(input("What's your age? "))
def main():
    if age <= 18:
        print("Kid")
    elif age > 65:
        print("Retired")
    else:
        print("Young and Active")

main()
