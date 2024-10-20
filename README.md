# Rule Engine with Abstract Syntax Tree (AST)

## Overview

This project implements a 3-tier rule engine application with a simple UI, API, and backend. The rule engine determines user eligibility based on attributes such as age, department, salary, and experience by creating and evaluating rules dynamically using an **Abstract Syntax Tree (AST)**. The system allows dynamic creation, combination, and modification of rules, stored in a database, and exposed through a set of APIs.

---

## Features

- **Create Rules**: Dynamically create eligibility rules based on user attributes.
- **Combine Rules**: Combine multiple rules into a single AST, optimizing for efficiency.
- **Evaluate Rules**: Evaluate the rule against user data to determine eligibility.
- **AST Structure**: Represent rules using AST for flexibility in creation, modification, and combination.
- **Error Handling**: Handle invalid rule strings and data formats gracefully.

---

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/).
- **Flask**: For the API implementation.
- **PostgreSQL**: Used as the database for storing rules.
- **Docker**: Optional, but useful for setting up the database.
- **Git**: For cloning the project.

---

## Project Structure

```bash
.
├── src
│   ├── app.py                    # Flask API for rule creation and evaluation
│   ├── ast.py                     # AST definition and rule creation logic
│   ├── rule_evaluator.py          # Rule evaluation logic
│   ├── db.py                      # Database interaction and rule storage
│   └── tests
│       ├── test_ast.py            # Unit tests for AST creation
│       ├── test_rule_evaluator.py # Unit tests for rule evaluation
├── README.md
├── requirements.txt               # Python dependencies
└── Dockerfile                     # Docker setup for PostgreSQL
```

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rule-engine-ast.git
cd rule-engine-ast
```

### 2. Create Virtual Environment
It's recommended to use a virtual environment to manage Python dependencies:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Set up the Database
You can either run PostgreSQL locally or use Docker to set it up.

**Option 1: PostgreSQL (Docker)**

Run PostgreSQL as a container using Docker:
```bash
docker run --name rule_db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
```

**Option 2: PostgreSQL Local Setup**

Install PostgreSQL and set up the database locally.

```bash
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres createuser admin -P
sudo -u postgres createdb rule_engine_db
```

### 5. Set up the Environment Variables
Create a `.env` file to store database connection details:
```bash
DB_URL=postgresql://admin:password@localhost:5432/rule_engine_db
```

### 6. Initialize Database Tables
Run the following script to set up the database schema:
```bash
python db.py
```

### 7. Run the Application
Start the Flask API:
```bash
python app.py
```

The API will now be available at `http://localhost:5000/`.

---

## API Endpoints

1. **Create Rule**

   - **URL**: `/create_rule`
   - **Method**: POST
   - **Description**: Create a rule from a rule string.
   - **Body**: 
     ```json
     {
       "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
     }
     ```

2. **Combine Rules**

   - **URL**: `/combine_rules`
   - **Method**: POST
   - **Description**: Combine multiple rules into a single AST.
   - **Body**:
     ```json
     {
       "rules": [
         "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))",
         "(salary > 50000 OR experience > 5)"
       ]
     }
     ```

3. **Evaluate Rule**

   - **URL**: `/evaluate_rule`
   - **Method**: POST
   - **Description**: Evaluate the rule against user data.
   - **Body**:
     ```json
     {
       "rule_ast": { ... },
       "data": {
         "age": 35,
         "department": "Sales",
         "salary": 60000,
         "experience": 3
       }
     }
     ```

---

## Data Structure (AST Representation)

The AST is represented as a tree of `Node` objects, where each `Node` can be an operator (`AND`, `OR`) or an operand (condition).

Example:
```python
class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type        # "operator" or "operand"
        self.value = value      # Value of the operand (e.g., age > 30)
        self.left = left        # Left child (for operators)
        self.right = right      # Right child (for operators)
```

Sample rule (`((age > 30 AND department = 'Sales') OR (salary > 50000))`):
```plaintext
              OR
            /    \
          AND    salary > 50000
         /    \
    age > 30 department = 'Sales'
```

---

## Test Cases

1. **Create Individual Rules**: Create rules from strings and validate their AST representation.
2. **Combine Rules**: Combine rules and ensure the resulting AST represents the combined logic.
3. **Evaluate Rule**: Test the evaluation logic against different user data scenarios.
4. **Error Handling**: Ensure the system handles invalid rules and data gracefully.

### Running Tests
```bash
pytest
```

---

## Example Scenarios

### Rule Example 1:
```bash
rule_string = "((age > 30 AND department = 'Sales') OR (salary > 50000))"
data = {"age": 35, "department": "Sales", "salary": 60000}
# Result: True (eligible)
```

### Rule Example 2:
```bash
rule_string = "(age < 25 AND department = 'Marketing') AND (experience > 5)"
data = {"age": 22, "department": "Marketing", "experience": 3}
# Result: False (not eligible)
```

---

## Bonus Features

- **Error Handling**: Proper handling for missing operators, invalid comparisons, or malformed rule strings.
- **Rule Modification**: Modify existing rules by changing operators or conditions dynamically.
- **Validations**: Implement attribute validations to ensure valid data is provided for evaluation.

---

## Dependencies

- **Flask**: Web framework for API development.
- **SQLAlchemy**: ORM for database interaction.
- **PostgreSQL**: Database for rule storage.
- **pytest**: For unit testing.

---

## Future Improvements

- Extend the system to support more complex conditions and user-defined functions.
- Implement more advanced optimizations when combining rules.
- Enhance visualizations and UI for managing rules.

---

## License

This project is licensed under the MIT License.

---

## Contributors

- Swaraj Ravindra Purarkar

---
