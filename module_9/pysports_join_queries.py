import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    
    cursor=db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    teams = cursor.fetchall()
    print(" -- DISPLAYING PLAYER RECORDS -- ")
    for team in teams:
        print("Player ID: {}".format(team[0]))
        print("First Name: {}".format(team[1]))
        print("Last Name: {}".format(team[2]))
        print("Team Name: {}".format(team[3]))
        print("\n")




except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)
finally:
    db.close()