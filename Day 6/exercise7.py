# Find players who play both games
team1 = ["Jake", "Allan", "Nick", "Alex", "Dave"]
team2 = ["David", "John", "Chris", "Alex", "Nick"]

for aplayer in team1:
    if aplayer in team2:
        print("%s also plays for team2." % (aplayer))
