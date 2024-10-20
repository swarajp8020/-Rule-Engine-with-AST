# -Rule-Engine-with-AST

## Overview

This project implements a 3-tier rule engine application to determine user eligibility based on attributes such as age, department, salary, and experience. The system uses an Abstract Syntax Tree (AST) to represent, create, combine, and evaluate dynamic rules. Users can define conditional rules through an API, which the engine can then evaluate against incoming data to determine eligibility.

---

## Features

- **Rule Creation**: Define conditional rules as strings and parse them into AST nodes.
- **Rule Combination**: Combine multiple rules efficiently by minimizing redundant checks and optimizing operator usage.
- **Rule Evaluation**: Evaluate a rule's AST against user data to determine eligibility.
- **Dynamic Modification**: Modify existing rules by updating operators, operand values, or adding/removing sub-expressions.
- **Error Handling**: Handle invalid rule strings or data formats gracefully.
- **Validation**: Ensure attribute validity through a catalog system.

---

## Prerequisites

- **Java 11+**: The system is built using Java.
- **Maven**: For building the project and managing dependencies.
- **PostgreSQL (or any other preferred database)**: To store rule definitions and metadata.
- **Docker**: For easy database setup (optional).
- **Git**: For cloning the project.

---

## Project Structure

```
.
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com.ruleengine.ast
│   │   │       └── Main.java
│   │   │       └── RuleParser.java
│   │   │       └── ASTNode.java
│   │   │       └── RuleEvaluator.java
│   │   ├── resources
│   └── test
│       └── java
│           └── com.ruleengine.ast
├── README.md
├── pom.xml
└── Dockerfile
```

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rule-engine-ast.git
cd rule-engine-ast
```

### 2. Set up Environment Variables
Create a `.env` file in the root directory to manage database connections:
```env
DB_URL=jdbc:postgresql://localhost:5432/ruleengine
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
```

### 3. Build the Project
Use Maven to build the project:
```bash
mvn clean install
```

### 4. Set up PostgreSQL Database (Docker)
The application uses PostgreSQL to store rules and metadata. You can run PostgreSQL using Docker:
```bash
docker run --name ruleengine-db -e POSTGRES_USER=your_db_username -e POSTGRES_PASSWORD=your_db_password -d -p 5432:5432 postgres
```

### 5. Run the Application
Run the application using Maven:
```bash
mvn spring-boot:run
```

Alternatively, you can run the jar:
```bash
java -jar target/rule-engine-ast-1.0.jar
```

---

## API Endpoints

### 1. **Create Rule**: `/create_rule`
   - **Method**: `POST`
   - **Request Body**: 
     ```json
     {
       "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
     }
     ```
   - **Response**: A JSON representation of the AST.

### 2. **Combine Rules**: `/combine_rules`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "rules": [
         "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
         "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
       ]
     }
     ```
   - **Response**: A JSON representation of the combined AST.

### 3. **Evaluate Rule**: `/evaluate_rule`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "rule_ast": {/* AST representation */},
       "user_data": {
         "age": 35,
         "department": "Sales",
         "salary": 60000,
         "experience": 3
       }
     }
     ```
   - **Response**: `true` or `false` depending on whether the rule conditions are met.

---

## AST Representation

The system represents rules using an Abstract Syntax Tree (AST). Here's a sample structure:

```java
class ASTNode {
    String type; // "operator" for AND/OR, "operand" for conditions
    ASTNode left; // Left child node
    ASTNode right; // Right child node
    String value; // Value for operand nodes, e.g., comparison condition
}
```

- **Operators**: AND, OR
- **Operands**: Conditions such as `age > 30`, `salary > 50000`

---

## Rule Combination Strategy

When combining multiple rules, the system optimizes the process by:
- Removing redundant operators
- Prioritizing frequent operators to minimize re-checking of conditions
- Returning a single AST that represents the combined logic of all rules

---

## Rule Evaluation

The `evaluate_rule` function takes in:
- A JSON AST representation of the rule
- User data as a dictionary
It evaluates the rule against the user’s data and returns `true` or `false` based on whether the conditions are met.

Example:
```json
{
  "rule_ast": { /* AST structure for rule1 */ },
  "user_data": {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
  }
}
```

The system will return `true` if the user satisfies the rule conditions, otherwise `false`.

---

## Sample Test Cases

### 1. **Create Rule**
- Test the creation of individual rules from strings.
- Verify the AST representation matches the expected structure.

### 2. **Combine Rules**
- Test combining two or more rules.
- Ensure that the combined AST accurately represents the logical combination.

### 3. **Evaluate Rule**
- Test the evaluation of a rule using sample user data.
- Verify the correct outcome (true/false) based on the conditions.

---

## Data Storage

The system stores rules and metadata in a PostgreSQL database. Here's a sample schema:

```sql
CREATE TABLE rules (
  id SERIAL PRIMARY KEY,
  rule_string TEXT,
  ast_json JSONB,
  created_at TIMESTAMP
);

CREATE TABLE rule_metadata (
  id SERIAL PRIMARY KEY,
  rule_id INT REFERENCES rules(id),
  attribute_name TEXT,
  operator TEXT,
  value TEXT
);
```

---

## Error Handling

- Invalid rule strings are handled with appropriate error messages.
- If user data is incomplete or in an invalid format, the system returns an error.
  
Example:
- **Invalid Rule**: `"age => 30"`
- **Error Message**: `Invalid operator "=>" in rule`

---

## Bonus Features 

- **Rule Modification**: Users can modify existing rules by updating the operators or operands.
- **User-defined Functions**: Extend the rule engine to support user-defined functions for advanced conditions.

---

## Dependencies

- Java 11+
- Maven
- PostgreSQL
- Docker (for database setup)
- OpenWeatherMap API

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributors

- Swaraj Ravindra Purarkar

---

This README outlines the key aspects of the project, making it easy for others to understand how to set up, run, and extend the rule engine application.

Request: {"rules": ["age > 30 AND department = 'Sales'", "salary > 50000"]} POST /evaluate_rule: Evaluates the rule AST against the provided user attributes.

Request: {"rule": {...AST...}, "attributes": {"age": 35, "department": "Sales", "salary": 60000}} 6. Running Unit Tests To ensure the functionality of the rule engine, unit tests are provided in test_rule_engine.py. To run the tests:

bash Copy code python -m unittest test_rule_engine.py 7. Customization and Extensibility Custom Rules: Users can define more complex rules through the web interface or modify rule_engine.py to extend supported conditions. Error Handling: Basic error handling is included, but you can enhance it for better validation of rules and conditions. 8. Future Improvements Extend support for additional weather parameters (e.g., humidity, wind speed) for enhanced rule evaluation. Improve the user interface for a better user experience. Implement persistent storage (e.g., SQLite) to store and retrieve rules and user data. Example Interaction Create a Rule:

Input: age > 30 AND department = 'Sales' Result: The rule is converted to an AST and displayed in JSON format. Combine Rules:

Input: java Copy code age > 30 AND department = 'Sales' salary > 50000 Result: A combined AST using the AND operator. Evaluate Rule:

Rule: {"type": "AND", "left": {...}, "right": {...}} User Data: {"age": 35, "department": "Sales", "salary": 60000} Result: {"result": true} indicating the conditions are satisfied.
