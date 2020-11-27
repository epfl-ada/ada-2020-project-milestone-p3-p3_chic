import sqlite3
import pandas as pd

# this code will read the SQL databases from 'mysql://localhost' server. 
# user of this shell ('arthur' in my case) must have write access
# the database must exist (of course...) so one must open the .sql with mysql shell and lunch the following lnes
# mysql: "CREATE DATABASE diplo" ; 
# mysql: "USE diplo" ; 
# terminal: "mysql diplo < diplomacy.sql"

games = pd.read_sql_table("games", "mysql://arthur@localhost/diplo")
orders = pd.read_sql_table("orders", "mysql://arthur@localhost/diplo")
players = pd.read_sql_table("players", "mysql://arthur@localhost/diplo")
turns = pd.read_sql_table("turns", "mysql://arthur@localhost/diplo")
units = pd.read_sql_table("units", "mysql://arthur@localhost/diplo")

games.to_pickle("games.pkl")
orders.to_pickle("orders.pkl")
players.to_pickle("players.pkl")
turns.to_pickle("turns.pkl")
units.to_pickle("units.pkl")

