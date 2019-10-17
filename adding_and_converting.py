#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This program adds two decimals together
#  and converts number to scientific notation


def main():
    # this program convertsto base 10 and adds two integers
    print(0.1 + 0.2)

    # this converts to scientific notation
    speed_of_light = 299792458
    print("{:.2e}".format(speed_of_light))


if __name__ == "__main__":
    main()
