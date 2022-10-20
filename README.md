# get-ip-location-data
Kludgy Python script to get the geolocations of many IP addresses at once. Uses [Requests](https://pypi.org/project/requests/) for API interaction and [IP-API](https://ip-api.com) for data. This script was initially created to scrape IP addresses from [Endlessh](https://github.com/skeeto/endlessh) logs, but can read and process IP addresses from many other sources, such as an SSHD auth log.

# Installation (optional)
To "install", mark the script as executable and place it somewhere in your path. You may also want to remove the .py extension. To uninstall, just delete the script.

# Usage
Pass or pipe a bunch of IPv4 addresses and/or the names of files containing IPv4 addresses to the script. Program will output locational data for all IPv4 addresses supplied in JSON notation, divided into groups of 100 (or less) JSON objects.

# Example
    $ echo "93.184.216.34" | get-ip-location-data.py /var/log/auth.log
    [
      {
        "status": "success",
        "country": "United States",
        "regionName": "Massachusetts",
        "city": "Norwell",
        "zip": "02061",
        "lat": 42.1591,
        "lon": -70.8163,
        "isp": "Edgecast Inc.",
        "org": "",
        "mobile": false,
        "proxy": true,
        "hosting": false,
        "query": "93.184.216.34"
      },
      {
        "status": "success",
        "country": "United States",
        "regionName": "New York",
        "city": "New York",
        "zip": "10123",
        "lat": 40.7128,
        "lon": -74.006,
        "isp": "Verizon Business",
        "org": "Verizon Business",
        "mobile": true,
        "proxy": false,
        "hosting": false,
        "query": "63.41.9.207"
      },
      {
        "status": "success",
        "country": "Russia",
        "regionName": "Moscow",
        "city": "Moscow",
        "zip": "102473",
        "lat": 55.7483,
        "lon": 37.6171,
        "isp": "Delta Ltd",
        "org": "Delta Ltd",
        "mobile": false,
        "proxy": false,
        "hosting": false,
        "query": "109.248.6.103"
      },

      ...

      {
        "status": "success",
        "country": "China",
        "regionName": "Guangdong",
        "city": "Shenzhen",
        "zip": "",
        "lat": 22.5431,
        "lon": 114.058,
        "isp": "China Internet Network Information Center",
        "org": "Tencent cloud computing (Beijing) Co., Ltd.",
        "mobile": false,
        "proxy": false,
        "hosting": false,
        "query": "124.220.187.30"
      }
    ]
    
    $
# Notes
• This script requires the [Requests](https://pypi.org/project/requests/) library to function. \
• Contributions are more than welcome. \
• IP-API forbids use of its free endpoint for commercial use, so if you're using this in a commercial production environment - which you should not do - you'll have to fork over some cash to them. \
• This script has only been tested on Linux. I can't think of a reason it wouldn't work on Windows or Mac OS, but if it doesn't please let me know.

# random-ip-generator
A script to generate random IP addresses for testing get-ip-location-data.

# Installation (optional)
See the above instructions for get-ip-location-data.

# Usage
Call it with a number as an argument and the script will generate that many IP addresses.

# Example
    $ random-ip-generator 8
    248.208.104.220
    253.233.60.118
    238.16.218.137
    177.13.106.138
    43.201.167.237
    113.146.35.71
    147.35.217.41
    58.35.3.219
    
    $

# Notes
• This script has only been tested on Linux. I can't think of a reason it wouldn't work on Windows or Mac OS, but if it doesn't please let me know.
