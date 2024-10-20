# Test Case 1: Create individual rules from examples and verify AST
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
ast1 = create_rule(rule1)
ast2 = create_rule(rule2)
print("AST1:", ast1)
print("AST2:", ast2)

# Test Case 2: Combine rules and verify the combined AST
combined_ast = combine_rules([ast1, ast2], operator="AND")
print("Combined AST:", combined_ast)

# Test Case 3: Evaluate rule with sample data
data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
data2 = {"age": 24, "department": "Marketing", "salary": 30000, "experience": 6}
result1 = evaluate_rule(combined_ast, data1)
result2 = evaluate_rule(combined_ast, data2)
print("Data1 Eligibility:", result1)  # Expected: True
print("Data2 Eligibility:", result2)  # Expected: True
