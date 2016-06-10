-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- Table with list of unique player ids and player names

-- If exists, delete the tournament database
DROP DATABASE IF EXISTS tournament;

-- Create the tournament database
CREATE DATABASE tournament;

-- Connect to the tournament database
\c tournament

CREATE TABLE players ( id SERIAL PRIMARY KEY, name TEXT);

-- table with list of unique match ids, the id of the winning player and the id of the losing player
CREATE TABLE matches ( id_match SERIAL PRIMARY KEY,
						id_winner INTEGER REFERENCES players(id),
						id_loser INTEGER REFERENCES players(id)
						);

--- View that aggregates the number matches played and groups the count by player id
CREATE VIEW matches_played AS SELECT players.id,
						players.name,
						COUNT(matches.id_match)::int AS played
						from players LEFT JOIN matches
						on players.id = matches.id_winner
						or players.id = matches.id_loser
						GROUP BY players.id;

-- View that counts the number of wins a player has in the matches table and groups the count by player id
CREATE VIEW wins AS SELECT players.id::int,
						players.name,
						COUNT(matches.id_winner)::int AS wins
						FROM players LEFT JOIN matches
						ON players.id = matches.id_winner
						GROUP BY players.id;