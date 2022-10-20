# get-ip-location-data
Kludgy Python script to get the geolocations of many IP addresses at once. Uses https://ip-api.com for data.

# Usage
Pass or pipe a bunch of IPv4 addresses and/or the names of files containing IPv4 addresses to the script. Program will output locational data for all IPv4 addresses supplied in JSON notation.

# Example
    $ cat "93.184.216.34" | get-ip-location-data.py /var/log/auth.log
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
• Contributions are more than welcome.\
• ip-api forbids use of its free endpoint for commercial use, so if you're using this in a commercial production environment (god help you), you'll have to fork over some cash to them.
