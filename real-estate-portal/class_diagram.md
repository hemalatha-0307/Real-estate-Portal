# Class Diagram for Real Estate Portal

## UML Class Diagram

The class diagram represents the static structure of the system, showing classes, attributes, methods, and relationships.

### Classes Overview:
- **User**: Represents buyers and sellers.
- **Property**: Represents land/houses for sale.
- **Review**: Represents feedback from buyers on sellers.

### Text-Based UML Diagram (PlantUML Style):

```
@startuml Class Diagram

class User {
    +id: Integer
    +name: String
    +email: String
    +password: String
    --
    +__init__(name, email, password)
    +__repr__(): String
    +is_authenticated(): Boolean
    +is_active(): Boolean
    +is_anonymous(): Boolean
    +get_id(): String
}

class Property {
    +id: Integer
    +title: String
    +price: Integer
    +location: String
    +user_id: Integer
    --
    +__init__(title, price, location, user_id)
    +__repr__(): String
}

class Review {
    +id: Integer
    +reviewer_id: Integer
    +reviewed_user_id: Integer
    +rating: Integer
    +comment: Text
    +date_posted: DateTime
    --
    +__init__(reviewer_id, reviewed_user_id, rating, comment)
    +__repr__(): String
}

User ||--o{ Property : lists
User ||--o{ Review : gives (as reviewer)
User ||--o{ Review : receives (as reviewed)

@enduml
```

### Detailed Description:

#### User Class
- **Attributes**:
  - `id`: Primary key (Integer)
  - `name`: User's full name (String, 100 chars)
  - `email`: Unique email address (String, 100 chars)
  - `password`: Hashed password (String, 100 chars)
- **Methods**:
  - `__init__(name, email, password)`: Constructor
  - `__repr__()`: String representation
  - `is_authenticated()`: Check if user is logged in (from UserMixin)
  - `is_active()`: Check if user account is active
  - `is_anonymous()`: Check if user is anonymous
  - `get_id()`: Get user ID as string

#### Property Class
- **Attributes**:
  - `id`: Primary key (Integer)
  - `title`: Property title (String, 200 chars)
  - `price`: Property price (Integer)
  - `location`: Property location (String, 200 chars)
  - `user_id`: Foreign key to User (seller)
- **Methods**:
  - `__init__(title, price, location, user_id)`: Constructor
  - `__repr__()`: String representation

#### Review Class
- **Attributes**:
  - `id`: Primary key (Integer)
  - `reviewer_id`: Foreign key to User (buyer)
  - `reviewed_user_id`: Foreign key to User (seller)
  - `rating`: Rating 1-5 (Integer)
  - `comment`: Optional comment (Text)
  - `date_posted`: Timestamp (DateTime)
- **Methods**:
  - `__init__(reviewer_id, reviewed_user_id, rating, comment)`: Constructor
  - `__repr__()`: String representation

### Relationships:
- **User to Property**: One-to-Many (One user can list many properties)
- **User to Review (as Reviewer)**: One-to-Many (One user can give many reviews)
- **User to Review (as Reviewed)**: One-to-Many (One user can receive many reviews)

This diagram can be rendered using PlantUML or tools like Visual Paradigm for a graphical view.

## SOLID Principles Application
- **Single Responsibility**: Each class has one responsibility (User for auth, Property for listings, Review for feedback).
- **Open/Closed**: Classes are open for extension (e.g., add new attributes) but closed for modification.
- **Liskov Substitution**: Subclasses (if any) can replace base classes without issues.
- **Interface Segregation**: Not directly applicable here, but methods are minimal and focused.
- **Dependency Inversion**: High-level modules (Flask routes) depend on abstractions (models), not concretions.

This class diagram provides a blueprint for the system's object-oriented design.