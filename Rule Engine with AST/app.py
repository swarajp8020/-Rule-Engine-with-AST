from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule
from database import store_rule, get_rules

app = Flask(__name__)

# Create Rule API
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule')
    if not rule_string:
        return jsonify({"error": "Rule string is required"}), 400

    ast = create_rule(rule_string)
    store_rule(rule_string, ast)  # Store the rule in DB
    return jsonify({"ast": str(ast)}), 200

# Combine Rules API
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rule_ids = request.json.get('rule_ids')
    if not rule_ids:
        return jsonify({"error": "Rule IDs are required"}), 400

    rules = get_rules(rule_ids)  # Fetch ASTs from DB
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": str(combined_ast)}), 200

# Evaluate Rule API
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')
    
    if not rule_id or not data:
        return jsonify({"error": "Rule ID and data are required"}), 400
    
    ast = get_rule_ast(rule_id)  # Fetch AST from DB
    result = evaluate_rule(ast, data)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
