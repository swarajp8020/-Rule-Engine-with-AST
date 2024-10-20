import re
from models import Node

def create_rule(rule_string):
    # Simplified rule parsing
    tokens = re.findall(r'\w+|\S', rule_string)

    def parse_expression(tokens):
        if 'AND' in tokens:
            index = tokens.index('AND')
            return Node('operator', left=parse_expression(tokens[:index]), right=parse_expression(tokens[index+1:]), value='AND')
        elif 'OR' in tokens:
            index = tokens.index('OR')
            return Node('operator', left=parse_expression(tokens[:index]), right=parse_expression(tokens[index+1:]), value='OR')
        else:
            return parse_condition(tokens)

    def parse_condition(tokens):
        field, op, val = tokens[0], tokens[1], tokens[2]
        return Node('operand', value={"field": field, "op": op, "val": int(val) if val.isdigit() else val})

    return parse_expression(tokens)

def combine_rules(rules, operator="AND"):
    combined_ast = None
    for rule in rules:
        if combined_ast is None:
            combined_ast = rule
        else:
            combined_ast = Node('operator', left=combined_ast, right=rule, value=operator)
    return combined_ast

def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        return evaluate_condition(ast.value, data)
    elif ast.node_type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    return False

def evaluate_condition(condition, data):
    field, op, val = condition["field"], condition["op"], condition["val"]
    if field not in data:
        return False
    if op == ">":
        return data[field] > val
    elif op == "<":
        return data[field] < val
    elif op == "=":
        return data[field] == val
    return False
