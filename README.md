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

This reads data dynamically for scraped websites and stores is a database.
You have install mysql server and database like this in ubuntu
$ sudo apt update
$ sudo apt install mysql-server

and 
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient

the you run the file that setup the sql server
cat setup_db.sql | mysql -u root -p

Load the database.
python3 -m load_data.py


Finally you have to setuo environmental variables for the name and password to the database

and run both the api and app.


