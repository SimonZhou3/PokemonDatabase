# project_n7z5j_r0b7x_x7g3b

# References
> Our database fetched data from https://pokeapi.co/ 
> PG_DUMP was used to export dynamic data into one SQL file (FOR postgreSQL)


# Project Setup
## Requirements
- Flask must be installed (https://flask.palletsprojects.com/en/2.2.x/)
- Python must be installed (https://www.python.org/downloads/)
- PostgreSQL must be installed (https://www.postgresql.org/download/)
- NodeJS must be installed (https://nodejs.org/en/)
- npm must be installed (https://www.npmjs.com/)

## Database Installation
**Note: PostgreSQL must be installed**
```
There is a single SQL file that handles creating and inserting all the data into the datatable at backend/src/init_DB/ExportedDatabase.sql.
1. Go to init_DB directory by using: cd backend/src/init_DB
2. Export data into database using: psql -d <database name> -U <user> -f ExportedDatabase.sql
```

## Running Backend
```
1. Go to the backend folder using: cd backend
2. Install all dependencies by using: pipenv install
3. Go to the backend/src directory by using: cd src
4. In the src directory, create a .env file. This file will be used to store database information locally. See below to configure .env file
5. To run the backend, run the command: flask --app app run
```
 ### Dotenv File
The following template should be inserted into the .env file 
>**NOTE: SSLMODE, HOST, and PORT are optional arguments. Local port is defaulted at 5432**
```
DBNAME=<Database Name>
DBUSER= <User>
PASSWORD= <Password>
SSLMODE= [Require | Optional]  
HOST=[<Host Name> | Optional]
PORT=[<Port> | Optional]
```

## Running Frontend
```
1. On another terminal, Go to the backend folder using: cd frontend
2. Install all dependencies by using: npm install
3. Go to the backend/src directory by using: cd src
4. To run the frontend, run the command: npm run dev
```

# Task:

    1. Frontend Development (using Vue.js)
        - Initial framework
        - Home page
        - Query result page
        - Bridging frontend and backend
    2. Backend Development (using Flask)
        - Initial REST API bridging between DBMS
        -  Build API:
            - Area
            - Generation
            -  Item
            - Location
            - Move
            - Region
            - Trainer
            - 
    3. DBMS (using Postgres)
        - Intialize and populate tables and database

# Timeline

     Note: Every groupmate will meet up during specified dates to work on and complete tasks together

     October 30th, 2022 - November 5th, 2022: Set up Postgres and create Empty tables
     November 5th, 2022 - November 7th, 2022: Link Database to Flask
     November 7th, 2022 - November 15th, 2022: Complete API endpoints and populate data into tables
     November 7th, 2022 - November 15th, 2022: Complete GUI Template
     November 15th, 2022 - November 21st, 2022: Bridge Frontend and backend together
     November 21st, 2022 - November 25th, 2022: Test and polish project

# GUI Template
 **NOTE MORE SCREENSHOTS WILL BE PROVIDED**

Home Search Page
![alt text](https://cdn.discordapp.com/attachments/1023670708779356220/1036388287251742730/unknown.png)

Information Page
![alt text](https://cdn.discordapp.com/attachments/1023670708779356220/1036397617841705060/unknown.png)
