#!/usr/bin/python3

#  get-ip-location-data.py
#
#  Copyright 2022 Nat H. <nat@2darkpark.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import random, sys

def main():
    if len(sys.argv) != 2:
        print("Usage: random-ip-generator <number>", file=sys.stderr)

        return 1

    try:
        n = int(sys.argv[1])

    except ValueError:
        print("Usage: random-ip-generator <number>", file=sys.stderr)

        return 1

    if n < 0:
        print("Error: number must be greater than zero.", file=sys.stderr)

        return 1

    for i in range(int(n)):
        print(f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}")
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
