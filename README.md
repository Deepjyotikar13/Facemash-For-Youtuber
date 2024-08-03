# Facemash-For-Youtuber
So in this project i made a website from the movie social network called "Facemash" that was originally build by mark zukerberg to rank women based on there lookS using the Elo algorithm but I made it for youtubers where you will chose your favourit youtuber.

This project is inspired by the movie 'The Social Network,' where Mark Zuckerberg created his infamous website to rank people based on their looks.But in my version of Facemash, you will rank your favorite YouTubers based on your preference. As I took on the challenge to make the website within 2 days, it was really challenging to fix all the issues. And as my experience about database is near about 0 so i tried to learn about databases(SQLALCHAMY Python sql toolkit) but didn't understand a single thing. With time running out, I made the most stupid decision to use a Python file as a database, and oh my god, it was way worse then i thought and a small advise based on my experience please don’t use any text-based file as your database its not that scalable and usefull but definetly it will help you to loose some of your brain cells while fixing the issues. Anyway, let’s look at all of the files and code to see how it works."

server.py: This is the main Python script that runs the Flask application. It defines routes, handles logic, and interacts with other files.
All_Youtubers_name.py: This file stores a list of YouTube names as there filenames (ex:-["Zach King.jpeg", "Matthew Beem.jpeg"]).
give_match_of_a_player.py: This file defines a function that selects two players who haven't played each other for the next match.
name_and_score_db.py: This file stores a dictionary where keys are YouTube image filenames and values are their corresponding scores.
player_ind_with_total_game.py: This file stores a list of lists where each sub-list contains a player's index and the total number of matches they've played.
ranking_algorithm.py: This file defines a function that calculates the expected win probability for two players based on the Elo rating system.
total_num_of_player.py: This file stores an integer representing the total number of YouTubers in the game.
index.html: This is the main HTML template for the game. It displays two YouTube images side-by-side and allows users to click on the image they think will win.
TopRanks.html: This HTML template displays the top-ranked YouTubers based on their scores.
style.css and style_for_top.css: These files likely contain styling information for the webpages.
Functionalities:

Match selection: The give_match_of_a_player.py function ensures that players are paired who haven't played against each other yet.
Image display and user interaction: The index.html template displays two YouTube images side-by-side. Clicking an image sends a POST request to the /image_clicked route in server.py.
Score update: When a user clicks an image, the /image_clicked route in server.py updates the scores of both YouTubers in the name_and_score_db.py file based on who have won or lost implemented in ranking_algorithm.py. It also updates the total number of matches played for the winning player in player_ind_with_total_game.py
Top rankings: The top route in server.py renders the TopRanks.html template, which displays the top-ranked YouTubers based on their scores in name_and_score_db.py

So I hope you might like the project. I know it could have been done more simply, but I overcomplicated it; sorry for that. Still, I had fun while making the website, and I really learned a lot spacially to never use a python file as a database I will definitely learn about databases next time.And Please don’t get demotivated if you can’t understand my code; it doesn’t mean you are a bad programmer. that means the code is messy—I couldn’t even understand it myself when I was trying to fix the issue the other day. But anyway, if you are reading upto this line, thank you so much for your time. I really appreciate it :)
