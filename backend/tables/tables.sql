CREATE DATABASE IF NOT EXISTS PyGame;

USE PyGame;

CREATE TABLE Users (
    User_id int NOT NULL AUTO_INCREMENT,
    Name VARCHAR(80) NOT NULL,
    Password VARCHAR(300) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Phone_number CHAR(8) NOT NULL,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (User_id)
);

CREATE TABLE ReactionTime (
    RT_Score_Id int NOT NULL AUTO_INCREMENT,
    User_id int,
    Reaction_Time_ms int NOT NULL,
    Score_set TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (RT_Score_Id),
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);