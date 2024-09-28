from flask import Flask, request, jsonify
import json
import re

app = Flask(__name__)

def parse_input(markdown_tables):
    labs = []
    for table in markdown_tables:
        rows = table.strip().split('\n')[2:]  # Skip the header rows
        lab_data = []
        for row in rows:
            columns = row.split('|')
            lab_id = int(columns[1].strip())
            cell_counts = list(map(int, columns[2].strip().split()))
            increment = columns[3].strip()
            condition = list(map(int, columns[4].strip().split()))
            lab_data.append({
                "lab_id": lab_id,
                "cell_counts": cell_counts,
                "increment": increment,
                "condition": condition
            })
        labs.append(lab_data)
    return labs

def evaluate_expression(count, increment):
    if 'count *' in increment:
        operand = increment.split('count * ')[1].strip()
        if operand.isdigit():
            return count * int(operand)
        else:
            return count * count
    elif 'count +' in increment:
        operand = increment.split('count + ')[1].strip()
        return count + int(operand)

@app.route('/lab_work', methods=['POST'])
def lab_work():
    input_data = request.get_json()
    markdown_tables = input_data.get('tables', [])
    labs = parse_input(markdown_tables)

    results = []

    for lab_data in labs:
        days_results = {}
        petri_dishes_count = [0] * len(lab_data)

        for day in range(1, 10001):
            for lab in lab_data:
                lab_id = lab['lab_id']
                for i, cell_count in enumerate(lab['cell_counts']):
                    updated_count = evaluate_expression(cell_count, lab['increment'])
                    condition = lab['condition']

                    if updated_count % condition[0] == 0:
                        next_lab_id = condition[1]
                    else:
                        next_lab_id = condition[2]

                    # Pass the dish to the appropriate lab
                    petri_dishes_count[next_lab_id] += 1
                    lab['cell_counts'][i] = updated_count  # Update count for the next iteration

            if day % 1000 == 0:
                days_results[day] = petri_dishes_count.copy()

        results.append(days_results)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)