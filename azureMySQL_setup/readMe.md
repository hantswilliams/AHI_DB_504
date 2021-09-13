# Notes 

- When initially cloning, need to add in the db_password.txt and db_root_password.txt to include for docker-compose

- Once docker-compose is up and running, can connect via: 
`mysql -u ahi -p -h 20.62.193.224 --port=3305` 
    - note that the port is change from standard port 3305 to 3306 to cause confusion
    - the `ahi` user is the default user set by docker-compose, and uses the password set by the config file 

- If deploying on cloud, need to remember to open up ports 3305 (or 3306), whichever port you want to use 




## Enable logging 

```
SET global general_log = 1;
SET global log_output = 'table';
```

- View log: `select * from mysql.general_log;` 
- Disable Query logging on the database: `SET global general_log = 0;`
- Clear query logs without disabling: `TRUNCATE mysql.general_log` 




## Running remote script 
- Try this: 
```mysql -u root -p -h 20.62.193.224 --port=3305  < "userCreation.sql"```



## ENV file within pythonScripts_dataCreation
- .env == 
    ```
        mysqluser=
        mysqlpassword=
    ```