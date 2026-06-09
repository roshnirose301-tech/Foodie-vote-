🍽️ FoodieVote – Smart Food Feedback System

Overview

FoodieVote is a web-based food feedback management system designed for college canteens and food service environments. The system allows students to rate food items, submit reviews, and share their dining experiences. The collected feedback helps administrators analyze food quality and improve services based on student opinions.

---

Problem Statement

Traditional food feedback collection methods are often manual, time-consuming, and difficult to manage. Paper-based feedback forms can lead to data loss and inefficient analysis.

FoodieVote provides a digital platform that enables students to submit ratings and feedback easily while helping administrators make informed decisions to improve food quality and customer satisfaction.

---

Requirement Gathering

Stakeholders

- Students
- Canteen Management
- System Administrator

Student Requirements

- Register and log in securely.
- View available food items.
- Rate food items.
- Submit comments and feedback.
- View previously submitted feedback.

Admin Requirements

- Add, update, and remove food items.
- View student feedback and ratings.
- Analyze food quality based on reviews.
- Generate reports for decision-making.

Non-Functional Requirements

- User-friendly interface
- Secure data storage
- Fast response time
- Reliable system performance
- Easy maintenance and scalability

---

Project Objectives

- Digitize food feedback collection.
- Improve food quality through feedback analysis.
- Reduce manual paperwork.
- Store feedback securely in a database.
- Generate reports for administrators.
- Increase student satisfaction.

---

Modules

1. Student Module

- Student Registration
- Student Login
- View Food Items
- Submit Ratings
- Submit Feedback
- View Feedback History

2. Admin Module

- Admin Login
- Manage Food Items
- View Ratings and Reviews
- Generate Reports
- Monitor Food Quality

3. Food Management Module

- Add Food Items
- Update Food Information
- Delete Food Items
- Categorize Food Items

4. Feedback Management Module

- Collect Ratings
- Store Feedback
- Analyze Reviews
- Generate Statistics

---

Technology Stack

Frontend

- HTML
- CSS
- JavaScript

Backend

- Java
- Spring Boot

Database

- MySQL

---

System Architecture

Student → Frontend → Backend → MySQL Database

Workflow

1. Student logs into the system.
2. Student views available food items.
3. Student submits ratings and feedback.
4. Feedback is stored in the database.
5. Administrator reviews ratings and comments.
6. Reports are generated for analysis.

---

Database Design

STUDENT

Field Name| Description
Student_ID| Unique Student Identifier
Name| Student Name
Email| Student Email
Password| Login Password

ADMIN

Field Name| Description
Admin_ID| Unique Admin Identifier
Username| Admin Username
Password| Admin Password

FOOD_ITEM

Field Name| Description
Food_ID| Unique Food Identifier
Food_Name| Name of Food Item
Category| Food Category
Price| Food Price

FEEDBACK

Field Name| Description
Feedback_ID| Unique Feedback Identifier
Student_ID| Student Reference
Food_ID| Food Reference
Rating| Rating Score
Comment| Student Review
Feedback_Date| Date of Submission

---

ER Diagram

The ER Diagram for the FoodieVote system is provided below:

"FoodieVote ER Diagram" (ER_Diagram.png)

---

Advantages

- Easy and convenient feedback collection.
- Reduces paperwork and manual processing.
- Secure data management.
- Faster report generation.
- Better food quality monitoring.
- Improved student engagement.
- Supports data-driven decision making.

---

Future Enhancements

- Mobile Application Support
- AI-Based Sentiment Analysis
- Food Recommendation System
- Analytics Dashboard
- Real-Time Feedback Monitoring

---

Conclusion

FoodieVote is an efficient and user-friendly food feedback management system that simplifies the process of collecting and analyzing food reviews. The system enables students to share their opinions while helping administrators improve food quality through meaningful insights and data analysis.
