import json
import psycopg2

def connect_db():
    # Connect to PostgreSQL (change credentials as needed)
    return psycopg2.connect(
        host="localhost",
        database="rule_engine",
        user="user",
        password="password"
    )

def store_rule(rule_string, ast):
    conn = connect_db()
    cursor = conn.cursor()
    rule_ast_json = json.dumps(ast, default=lambda o: o.__dict__)  # Convert AST to JSON
    cursor.execute("INSERT INTO rules (rule_string, rule_ast) VALUES (%s, %s)", (rule_string, rule_ast_json))
    conn.commit()
    cursor.close()
    conn.close()

def get_rule_ast(rule_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT rule_ast FROM rules WHERE id = %s", (rule_id,))
    rule_ast_json = cursor.fetchone()[0]
    conn.close()
    return json.loads(rule_ast_json)

def get_rules(rule_ids):
    conn = connect_db()
    cursor = conn.cursor()
    rule_ids_str = ','.join(map(str, rule_ids))
    cursor.execute(f"SELECT rule_ast FROM rules WHERE id IN ({rule_ids_str})")
    rules = cursor.fetchall()
    conn.close()
    return [json.loads(rule[0]) for rule in rules]
