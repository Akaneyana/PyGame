# 🎮 PyGame Minigames

<i>A simple and intuitive gaming platform designed to play various games.</i>

---

## 💡 Features & Ideas

### User Management
- 🔒 User registration and login with password encryption.
- 🖼️ Profile management, including tracking scores and user stats.
- 🔁 Seamless session persistence for ongoing gameplay.

### Game Functionality
- ⚡ **Reaction Time Game**: Test your reflexes with a fast-paced challenge.
- 🎮 Modular game architecture for easy addition of new games.

### UI Features
- 🎨 Consistent and reusable UI components, including input boxes, buttons, and labels.
- 📱 Optimized layouts for different screen sizes.
- 🖱️ Interactive hover and click animations for buttons.

### Backend Integration
- 🗄️ Database connection for storing user data (e.g., scores, profiles).
- 📊 Scalable database schema for future expansion.

---

# 🗄️ Database Schema

This document outlines the database schema for managing user data, game scores, and session information. The schema is designed for scalability, allowing future enhancements like additional games, leaderboards, and profile customization.

---

## 📋 Tables Overview

1. **Users Table**: Stores user account details.
2. **Games Table**: Lists available games and metadata.
3. **HighScores Table**: Tracks user scores for each game.
4. **Sessions Table**: Manages active user sessions for continuity.

---

## 🛢️ Schema Details

### **Users Table**
Stores user account information, including secure password storage.

```sql
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
### Columns:

- **user_id**: Primary key, unique identifier.
- **username**: Unique username for login.
- **password**: Encrypted user password.
- **email**: Optional, used for notifications or password recovery.
- **created_at**: Timestamp of account creation.
- **last_login**: Automatically updates on each login.

---

### 🎮 ReactionTime Table

The `ReactionTime` table is designed to track users' scores in the Reaction Time game. It records reaction times in milliseconds and associates each score with a user via a foreign key relationship.

```sql
CREATE TABLE ReactionTime (
    RT_Score_Id INT NOT NULL AUTO_INCREMENT,
    User_Id INT NOT NULL,
    Reaction_Time_ms INT NOT NULL,
    Score_Set TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (RT_Score_Id),
    FOREIGN KEY (User_Id) REFERENCES Users(User_Id)
);
```
### Columns:

- **RT_Score_Id**: Primary key, auto-incremented, unique identifier for each reaction time score entry.
- **User_Id**: Foreign key, references the `User_Id` from the `Users` table. Identifies the user who achieved the reaction time score.
- **Reaction_Time_ms**: Stores the user's reaction time in milliseconds. Represents how fast the user responded during the reaction test.
- **Score_Set**: Timestamp of when the reaction time score was recorded. Defaults to the current timestamp when the score is submitted.
- **Primary Key**: `RT_Score_Id`, ensures that each record is unique and can be queried efficiently.
- **Foreign Key**: `User_Id`, links each score to a specific user in the `Users` table, ensuring the validity of the relationship.

---

### ⌨️ TypingGame Table

The `TypingGame` table stores data related to the Typing Speed game, tracking how fast a user can type in words per minute (WPM). Each entry is tied to a specific user and timestamped.

```sql
CREATE TABLE TypingGame (
    TG_Score_Id INT NOT NULL AUTO_INCREMENT,
    User_Id INT NOT NULL,
    Words_Per_Minute INT NOT NULL,
    Score_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (TG_Score_Id),
    FOREIGN KEY (User_Id) REFERENCES Users(User_Id)
);
```
### Columms:

- **TG_Score_Id**: Primary key, auto-incremented unique identifier for each typing score entry.
- **User_Id**: Foreign key referencing the`1User_Id` in the `Users` table. Identifies the user who completed the typing test.
- **Words_Per_Minute**: Number of words typed per minute, representing the user's typing speed.
- **Score_Time**: Number of words typed per minute, representing the user's typing speed.
- **Primary Key**: `TG_Score_Id`, ensures uniqueness of score entries.
- **Foreign Key**: Ensures only valid users can have associated scores.
---

## 🚀 Future Plans

- **Leaderboard Integration**: 
  - Add a global leaderboard to compare scores across all users. The leaderboard could show the top 10 fastest reaction times.
  
- **User Profile and Stats**: 
  - Create user profiles where players can view their average reaction time, past scores, and progress.

- **Multi-User Support**: 
  - Allow multiple users to compete in the same session or challenge each other.

## 🙏 Acknowledgments

- **Pygame**: 
  - The game was built using [Pygame](https://www.pygame.org/), an excellent library for developing 2D games in Python.

- **MySQL**: 
  - We use [MySQL](https://www.mysql.com/) for the database to store user data and scores efficiently.

- **Open Source Community**: 
  - A huge thanks to the open-source community for their contributions and support. This project wouldn't be possible without the contributions of countless developers.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Akaneyana/PyGame/tree/main?tab=MIT-1-ov-file#MIT-1-ov-file) file for details.

