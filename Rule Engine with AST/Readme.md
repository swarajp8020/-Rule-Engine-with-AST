This rule engine application allows users to create, combine, and evaluate rules using an Abstract Syntax Tree (AST). The system dynamically generates rules from user input, enabling flexible decision-making based on various attributes like age, department, salary, and experience.

Features
Create Rule: Users can input rule strings to generate an AST representation.
Combine Rules: Multiple rules can be combined into a single logical rule.
Evaluate Rule: Rules can be evaluated against user-provided attributes (e.g., age, department).
User-Friendly Interface: A simple web interface for interacting with the rule engine.
Project Structure
plaintext
Copy code
rule-engine/
├── app.py # Main Flask application (API routes)
├── rule_engine.py # Core rule engine logic (AST creation, combination, evaluation)
├── templates/
│ └── index.html # Frontend UI (HTML + JavaScript)
├── requirements.txt # Python dependencies
├── test_rule_engine.py # Unit tests for the rule engine
└── README.md # Project documentation
Prerequisites
Python 3.x: Ensure you have Python installed on your machine.
Flask: The web framework used for building the API.
Setup Instructions

1. Clone the Repository
   bash
   Copy code
   git clone <repository_url>
   cd rule-engine
2. Install Dependencies
   Use the following command to install all required Python libraries:

bash
Copy code
pip install -r requirements.txt 3. Run the Application
Start the Flask server:

bash
Copy code
python app.py
The server will run at http://127.0.0.1:5000/. You can access the web interface by navigating to this URL in your browser.

4. Interact with the Rule Engine
   Open your browser and go to http://127.0.0.1:5000/.
   You will see options to:
   Create Rule: Enter a rule string (e.g., age > 30 AND department = 'Sales') and create a rule.
   Combine Rules: Input multiple rules separated by new lines to combine them.
   Evaluate Rule: Provide a rule AST and user attributes in JSON format to evaluate if the rule holds true for the provided data.
   Example Rule Strings
   Rule 1: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))
   Rule 2: ((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)
5. API Endpoints
   The backend exposes the following API endpoints:

POST /create_rule: Creates an AST from a rule string.

Request: {"rule_string": "age > 30 AND department = 'Sales'"}
POST /combine_rules: Combines multiple rule ASTs into a single rule.

Request: {"rules": ["age > 30 AND department = 'Sales'", "salary > 50000"]}
POST /evaluate_rule: Evaluates the rule AST against the provided user attributes.

Request: {"rule": {...AST...}, "attributes": {"age": 35, "department": "Sales", "salary": 60000}} 6. Running Unit Tests
To ensure the functionality of the rule engine, unit tests are provided in test_rule_engine.py. To run the tests:

bash
Copy code
python -m unittest test_rule_engine.py 7. Customization and Extensibility
Custom Rules: Users can define more complex rules through the web interface or modify rule_engine.py to extend supported conditions.
Error Handling: Basic error handling is included, but you can enhance it for better validation of rules and conditions. 8. Future Improvements
Extend support for additional weather parameters (e.g., humidity, wind speed) for enhanced rule evaluation.
Improve the user interface for a better user experience.
Implement persistent storage (e.g., SQLite) to store and retrieve rules and user data.
Example Interaction
Create a Rule:

Input: age > 30 AND department = 'Sales'
Result: The rule is converted to an AST and displayed in JSON format.
Combine Rules:

Input:
java
Copy code
age > 30 AND department = 'Sales'
salary > 50000
Result: A combined AST using the AND operator.
Evaluate Rule:

Rule: {"type": "AND", "left": {...}, "right": {...}}
User Data: {"age": 35, "department": "Sales", "salary": 60000}
Result: {"result": true} indicating the conditions are satisfied.
