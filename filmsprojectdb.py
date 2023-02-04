import sqlite3, os

os.system('cls' if os.name == 'nt' else 'clear')


con = sqlite3.connect('films.db')
cur = con.cursor()

# Table w/ Column Titles

cur.execute('''CREATE TABLE IF NOT EXISTS films
                     (
                        film_id INT NOT NULL,
                        movie_name VARCHAR(20) NOT NULL,
                        director VARCHAR(20) NOT NULL, 
                        writer VARCHAR(20) NOT NULL,
                        stars VARCHAR(25) NOT NULL, 
                        duration VARCHAR(4) NULL, 
                        rating VARCHAR(5) NULL, 
                        category VARCHAR(25) NOT NULL,
                        PRIMARY KEY (film_id) );''')

# Table w/ Values

cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('001', 'The Matrix', 'Lana Wachowski', 'Lilly Wachowski','Keanu Reeves' ,  '2.16', '8.7', 'Action')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('002', 'Labyrinth', 'Jim Henson', 'Dennis Lee','Jennifer Connelley' ,  '1.41', '7.3', 'Fantasy')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('003', 'The Batman', 'Matt Reeves', 'Matt Reeves','Robert Pattinson' ,  '2.56', '7.8', 'Thriller')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('004', 'Scream', 'Wes Craven', 'Kevin Williamson','Neve Campbell' ,  '1.51', '7.4', 'Horror')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('005', 'Dune', 'Denis Villeneuv', 'Jon Spaihts','Timothee Chalamet' ,  '2.35', '8.0', 'Adventure')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('006', 'Terminator 2: Judgement Day', 'James Cameron', 'James Cameron','Arnold Schwarzenegger' ,  '2.17', '8.6', 'Action')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('007', 'Skyfall', 'Sam Mendes', 'Robert Wade','Daniel Craig' ,  '2.23', '7.8', 'Action')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('008', 'Pathaan', 'Siddharth Anand', 'Siddharth Anand','Shah Rukh Khan' ,  '2.26', '6.7', 'Action')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('009', 'Alien', 'Ridley Scott', 'Ronald Shusett','Sigourney Weaver' ,  '1.57', '8.5', 'Horror')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('010', 'Prey', 'Dan Trachtenber', 'Dan Trachtenber','Amber Midthunder' ,  '1.40', '7.2', 'Horror')''')
cur.execute('''INSERT OR IGNORE INTO films 
                    VALUES ('011', 'Dilwale Dulhania Le Jayenge', 'Aditya Chopra', 'Aditya Chopra','Shah Rukh Khan' ,  '3.10', '8.0', 'Romance')''')


con.commit() 

# * Selects everything in table
print ('\n############################################################ Movies ############################################################ ')
for row in cur.execute('''SELECT * FROM films'''):
        print(row)
print('##################################################################################################################################')

# Sorts by highest rated at top (decending order)
print ('\n###### Highest Rated Movies ###### ')
for row in cur.execute('''SELECT movie_name, rating FROM films
                          ORDER BY rating DESC;'''):
        print(row)
print('##################################')

# Sorts by lowest rated at top (ascending order)
print ('\n###### Lowest Rated Movies ###### ')
for row in cur.execute('''SELECT movie_name, rating FROM films
                          ORDER BY rating ASC;'''):
        print(row)
print('##################################')

# Selects a chosen catergory 
print ('\n########## Action Movies ########## ')
for row in cur.execute('''SELECT movie_name, category FROM films
                          WHERE category = 'Action' '''):
        print(row)
print('##################################')

print ('\n########## Horror Movies ########## ')
for row in cur.execute('''SELECT movie_name, category FROM films
                          WHERE category = 'Horror' '''):
        print(row)
print('##################################')