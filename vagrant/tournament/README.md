# Tournament Planner
Tournament Planner is a Python module that uses a PostgreSQL database to record player information and match outcomes.  The tournament format will use the Swiss system to pair players in each round.  This tournament style will allow all participants to play in each round, pairing each match based on player records and standings.
More information about the Swiss system tournament can be found [here](https://en.wikipedia.org/wiki/Swiss-system_tournament).

## Requirements to Run Module
- Python 2.7
	- Psycopg database adapter [Install Instructions](http://initd.org/psycopg/docs/install.html#installation)
	- Bleach package: [Install Instructions](https://pypi.python.org/pypi/bleach)
- PostgreSQL

## Files
- tournament.sql - This file is used to set up the PostgreSQL database schema
- tournament.py - Python module used to access the tournament database.  Includes functions to add, delete and query player inforamtion from the database.
- tournament_test.py - Client program that will call functions in the tournament.py module.  The client program is written to test the functions in tournament.py

## Using the Tournament Planner Module
### Summary Steps
1. Build the Database Schema
2. Execute the tournament_test.py file

### Building the Database Schema
To build the database schema you will need to import the tournament.sql file.  The file will create a database named 'tournament' and the necessary tables and views to run the tournament.py module.
**Use the following steps to import the database from the command line**
1. From your terminal run `psql` to enter the psql CLI
2. Run command `\i tournament.sql` to build the database
3. Run command `\q` to exit the psql CLI

Example
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql
psql (9.3.13)
Type "help" for help.

vagrant=> \i tournament.sql
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE
CREATE VIEW
CREATE VIEW
tournament=> \q
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$
```

### Executing the tournament_test.py File
Executing the tournament_test.py file will run a series of test to validate the functionality of the tournament.py module.  The test results will be printed to the terminal screen.

Run the following command to run the test:
`python tournament_test.py`

Example of successfull test run
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```

## License
Tournament Planner is free software, and may be redistributed under the terms specified in the LICENSE file.
