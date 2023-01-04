# project_n7z5j_r0b7x_x7g3b

# References
> - Our database fetched data from https://pokeapi.co/ <br>
> - PG_DUMP was used to export dynamic data into one SQL file (FOR postgreSQL)


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
