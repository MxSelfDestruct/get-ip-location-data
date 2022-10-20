#!/usr/bin/python3

import json, re, requests, sys, time

IP_ADDRESS_REGEX = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" # This regex could be made more accurate.
IP_API_QUERY_FIELDS = "status,message,country,regionName,city,zip,lat,lon,isp,org,mobile,proxy,hosting,query"

# Function that finds and removes all duplicate entries in a list.
# Takes a list as an argument.
# Returns a list that has all duplicates removed.
def strip_duplicates_from_list(n):
    return_list = []

    for i in n:
        if i not in return_list:
            return_list.append(i)

    return return_list

# Function that finds all entries in a list of strings that match a regular expression.
# Takes a regular expression and a list of strings as arguments.
# Returns a list of all strings that matched.
def re_matches_in_list(pattern, list_of_strings):
    matching_strings = []

    for i in list_of_strings:
        matching_strings += re.findall(pattern, i)
    
    return matching_strings

# Function to get a response from ip-api.com with information about an IP address.
# Takes an IP address and a response type as an argument.
# Returns the data from ip-api as a string with the header stripped off.
def get_ip_data(ip_address, fields):
    return requests.get("http://ip-api.com/json/{}?{}".format(ip_address, fields)).text.replace(",", ", ").replace("{", "{ ").replace("}", " }")

# Function to divide list into sub-lists of up to n indicies
# Takes a list and a sub-list size as an argument.
# returns a list of sub-lists of up to n indicies containing the original list's contents in the order they were before.
def divide_list_into_sublists(l, sublist_size):
    return [l[i:i + sublist_size] for i in range(0, len(l), sublist_size)]

def main():
    # Builds a list of arguments comprised of everything piped in and all user command line arguments
    arguments = sys.argv[1:]

    # If there's piped input, add it to the argument list
    if not sys.stdin.isatty():
        arguments = sys.stdin.read().split() + arguments

    # Get rid of any whitespace or empty strings that sneak in
    for i in range(len(arguments)):
        if arguments[i].isspace() == True or arguments[i] == "":
            del(arguments[i])
    
    # If there are no arguments, exit.
    if arguments == []:
        print("No arguments given.")
        sys.exit(1)
    
    # Extract the IP addresses and text file names from sys.argv.
    ip_addresses = re_matches_in_list(IP_ADDRESS_REGEX, arguments)

    # Check for arguments that weren't sorted into ip_addresses and assume that they are text files.
    # Try to open them and pull out anything that looks like an IPv4 address.
    for i in arguments:
        if i not in ip_addresses:
            try:
                f = open(i, "r").read()
                f = f.split()
                ip_addresses += re_matches_in_list(IP_ADDRESS_REGEX, f)

            except FileNotFoundError:
                print("{}: {}: No such file or directory".format(sys.argv[0], i))
                sys.exit(1)

    # Strip any duplicates and then divide the list into chunks of 100 addresses
    ip_addresses = strip_duplicates_from_list(ip_addresses)
    ip_address_chunks = divide_list_into_sublists(ip_addresses, 100)

    # Build the request strings
    request_strings = []
    
    for i in ip_address_chunks:
        request_string = "["
        
        for j in i:
            request_string += ("{" + "\"query\":\"{}\", \"fields\":\"{}\"".format(j, IP_API_QUERY_FIELDS) + "},")

        request_string = request_string.rstrip(",")
        request_string += "]"

        request_strings.append(request_string)

    # Send each request string to ip-api.com, tidy up the responses, and print them
    for i in request_strings:
        ip_api_response = json.dumps(json.loads(requests.post("http://ip-api.com/batch", data = i).text), indent = 2)

        print(ip_api_response.replace("]\n", "\n]\n\n")) # Ew.

        # Unless this is the last request, wait four seconds to avoid flooding
        if i != request_strings[-1]:
            time.sleep(4)

    print()

if __name__ == "__main__":
    main()
