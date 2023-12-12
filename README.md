# Kartify
This is a flask web application that is intended to provide a one-stop browsing point for desktop and laptops across different sites.
There is also an api that runs alongside the application.

You can filter the results by vendor or price. Once You have found the item, the web app will direct you to the seller site where a purchase can be completed
![Kartify Screen Short](https://github.com/bion-slmn/Kartify/assets/122830539/a5c3874e-f48d-45de-9b68-dc00e7b1775a)

The application scrapes specific website at given intervals and stores the data in a mysql database. 
This allows ease on manipulation of data, reducing the number of requests and preventing the app from being blocked but also makes the application faster

The backend uses flask to create api and template for somepages
 The application runs on port 5001 and the api runs on port 5000
## APIs and Methods
This methods are for the web_Client:
### api/v1/laptop/vendor
GET: Return the all laptops from a specific vendor
### api/v1/desktop/vendor
GET: Return all the desktop from a specific vendor
### api/v1/all
GET: Return all computers both laptops and desktops in the storage
### api/v1/all/vendor
GET: Return all items from the specified vendor
### api/v1/laptops
GET: return all laptops in the storage
### api/v1/desktops
GET: Return all desktops  in storage
### api.v1/search/name/vendor
GET: Return all items  whose name has the value name match the name specified in the api from the vendor specified
### api.v1/search/name/
GET: Return all items whose name has the value name match the name specified in the api from all vendors

## How to Install and Run the Project
The application was built with ubuntu 20.04 , python3.8, sqlachemy version 2.0.21,
MySQLdb module version 2.2.0 and MySQL 8.0


### Installing MySQL 8.0
$ ```sudo apt update```

$ ```sudo apt install mysql-server```

### Installing MySQLdb
$ ```sudo apt-get install python3-dev```

$ ```sudo apt-get install libmysqlclient-dev```

$ ```sudo apt-get install zlib1g-dev```

$ ```sudo pip3 install mysqlclient```

### Installing SQLALchemy
$ ```sudo pip3 install SQLAlchemy```

### Installing requests and BeautifulSoup
$ ```pip install requests```

$ ```pip3 install beautifulsoup4```

### Starting Mysql database
$ ```sudo service mysql start```

$ ```cat setup_db.sql | mysql -u root -p```

### set environmental variable for DABATABASE
$ ```export PROJECT_USER="name of the user that was set in setup_db.sql"```

$ ```export PROJECT_PWD="password of the user that was set in setup_db.sql"```

$ ```export PROJECT_USER="bion_dev" PROJECT_PWD="bion_dev_pwd"```

### Scrape data and Load the database.
$ ```python3 load_data.py```

### START THE FLASK APP AND API
$ ```python3 -m flask_app.views```

$ ```python3 -m api.v1.app```

The application will be running on http://localhost:5001.
