# Kartify
This is a flask web application that is intended to provide a one-stop browsing point for electronics across different sites.
There is also an api that runs alongside the application. The application runs on port 5001 and the api runs on port 5000
## APIs and Methods
This methods are for the web_Client:
### api/stats
GET: Return the number of laptops, desktops and total number of all computers
### api/v1/computers
GET: Return all computers in the storage
### api/v1/laptops
GET: return all laptops in the storage
### api/v1/desktops
GET: return all desktops in the storage
### api/v1/vendor
GET: return the names and id of all vendors
### api/v1/vendor/<vendor id>
GET: return a vendor matching that ID
