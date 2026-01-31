# Sequence Diagrams for Real Estate Portal

## Overview
Sequence diagrams show the interaction between objects over time for specific user stories. They illustrate the flow of messages in the MVC architecture.

Using PlantUML for text-based representation.

## Sequence Diagram 1: User Registration

**User Story**: "As a potential buyer or seller, I want to register an account so that I can access the portal."

```
@startuml Sequence Diagram - User Registration

actor User
participant Browser
participant FlaskApp
participant UserModel
participant Database

User -> Browser: Open registration page
Browser -> FlaskApp: GET /register
FlaskApp -> Browser: Render register.html

User -> Browser: Fill form (name, email, password)
Browser -> FlaskApp: POST /register
FlaskApp -> FlaskApp: Hash password
FlaskApp -> UserModel: Create User instance
UserModel -> Database: Save user
Database -> UserModel: Confirm save
UserModel -> FlaskApp: Success
FlaskApp -> Browser: Redirect to /login

@enduml
```

**Description**: User interacts with browser, Flask handles request, creates model, saves to DB.

## Sequence Diagram 2: Write Review for Seller

**User Story**: "As a buyer who purchased land/house, I want to write a review for the seller so that future buyers can see feedback."

```
@startuml Sequence Diagram - Write Review

actor Buyer
participant Browser
participant FlaskApp
participant ReviewModel
participant Database

Buyer -> Browser: Navigate to seller profile or property
Browser -> FlaskApp: GET /property/<id> or /user/<id>
FlaskApp -> Browser: Render page with review form

Buyer -> Browser: Fill review (rating, comment)
Browser -> FlaskApp: POST /review
FlaskApp -> FlaskApp: Validate input
FlaskApp -> ReviewModel: Create Review instance
ReviewModel -> Database: Save review
Database -> ReviewModel: Confirm save
ReviewModel -> FlaskApp: Success
FlaskApp -> Browser: Redirect to profile/page

@enduml
```

**Description**: Buyer submits review, Flask validates and saves via model to DB.

These diagrams can be visualized using PlantUML online or integrated into Azure Boards.