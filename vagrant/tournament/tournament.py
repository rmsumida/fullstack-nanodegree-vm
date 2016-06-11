#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


# def connect():
#     """Connect to the PostgreSQL database.  Returns a database connection."""
#     return psycopg2.connect("dbname=tournament")


def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = "DELETE FROM matches"
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query = "DELETE FROM players"
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    # SQL query to count the number of ids from the players table,
    # returned as an integer
    query = "SELECT count(players.id)::int AS num FROM players"
    cursor.execute(query)
    count = cursor.fetchone()
    db.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    # Sanitize strings used in the 'name' variable
    # before inserting it into the database
    name = bleach.clean(name)
    query = "INSERT INTO players (name) VALUES (%s)"
    parameter = (name,)
    cursor.execute(query, parameter)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or
    a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    # SQL query to count the number of ids from the players table,
    # returned as an integer
    query = "SELECT * FROM player_standings"
    cursor.execute(query)
    standings = cursor.fetchall()
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Sanitize strings used in the 'winner' and 'loser' variable
    # before inserting it into the database
    winner = bleach.clean(winner)
    loser = bleach.clean(loser)
    db, cursor = connect()
    # SQL query to record the match winner and loser into the matches table
    query = "INSERT INTO matches (id_winner, id_loser) VALUES (%s, %s)"
    parameter = (winner, loser)
    cursor.execute(query, parameter)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, cursor = connect()
    # Get table with id and name sorted by total wins in descending order
    query = ("SELECT id, name FROM wins")
    cursor.execute(query)
    standings = cursor.fetchall()
    # print 'Print standings'
    # print standings
    num_players = countPlayers()
    # print 'Print Number of Players'
    # print num_players
    player_list = [player[0:2] for player in standings]
    # print 'Print Player List'
    # print player_list
    pairings = []
    i = 0
    while i < num_players:
        # Create list of tuples, each with a pair of players
        match_pair = player_list[i] + player_list[i + 1]
        # Append pair tuple to the pairings list
        pairings.append(match_pair)
        # Jump to first player in next pair
        i += 2
    # print 'Print Pairings'
    # print pairings
    db.close()
    return pairings
