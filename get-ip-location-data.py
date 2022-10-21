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

import json, re, requests, sys, time

IP_ADDRESS_REGEX = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" # This regex could be made more accurate.
IP_API_QUERY_FIELDS = "status,message,country,regionName,city,zip,lat,lon,isp,org,mobile,proxy,hosting,query"
MAX_ADDRESSES_IN_QUERY = 100

def main(arguments):
    # If there's piped input, add it to the argument list
    if not sys.stdin.isatty():
        arguments = sys.stdin.read().split() + arguments

    # Quit with error if no arguments given
    if arguments == []:
        print("Usage: get-ip-location-data <ip addresses> <text files>", file=sys.stderr)
        return 1

    # Make a string containing arguments seperated by spaces
    joined_argument_string = " ".join(arguments)

    # Extract IP addresses into their own list
    ip_addresses = re.findall(IP_ADDRESS_REGEX, joined_argument_string)

    # Check to see if all arguments are IP addresses by splitting the argument string by spaces and comparing it to
    # the IP address list
    if joined_argument_string.split(" ") != ip_addresses:
        invalid_args = []

        for i in joined_argument_string.split(" "):
            if i not in ip_addresses:
                # If it's not an IP address, see if it's a file. If it is, open it and scan for IP addresses. If not,
                # Log it as an invalid argument.
                try:
                    f = open(i, "r").read()
                    ip_addresses += re.findall(IP_ADDRESS_REGEX, f)

                except FileNotFoundError:
                    invalid_args.append(i)

        if len(invalid_args) > 1:
            print("Error: Invalid IP addresses or filenames: " + ', '.join(invalid_args), file=sys.stderr)

            return 1

    # Filter out repeated IP addresses and divide into chunks of 100 for IP-API queries
    unique_ip_addresses = [*set(ip_addresses)]
    query_chunks = [unique_ip_addresses[i:i + MAX_ADDRESSES_IN_QUERY] for i in range(0, len(unique_ip_addresses), MAX_ADDRESSES_IN_QUERY)]

    # Construct request strings
    request_strings = []

    for i in query_chunks:
        request_string = []

        for address in i:
            request_string.append('{"query": "' + address + '", "fields": "' + IP_API_QUERY_FIELDS + '"}')

        request_string = "[" + ", ".join(request_string) + "]"

        request_strings.append(request_string)

    # Send each request string to ip-api.com, tidy up the responses, and print them
    for i in request_strings:sha22
        print(json.dumps(json.loads(requests.post("http://ip-api.com/batch", data = i).text), indent = 2))

        # Unless this is the last request, wait 4 seconds to avoid flooding. We're not worried about false positives
        # since duplicates have already been filtered out
        if i != request_strings[-1]:
            time.sleep(4) # IP-API only allows up to 15 batch requests per minute without payment.

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
