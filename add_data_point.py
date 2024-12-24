import os
import time
import re
from create_example_data import create_pixel

def add_single_point(date, quantity):
    token = os.environ.get('SECRET_KEY')
    username = 'raimonvibe'
    graph_id = 'coding-hours'
    
    try:
        result = create_pixel(token, username, graph_id, date, quantity, None)
        print(f'Adding pixel for {date} with {quantity} hours: {result}')
        return result
    except Exception as e:
        print(f'Error adding pixel for {date}: {str(e)}')
        return {'isSuccess': False, 'message': str(e)}

def process_todo_list(todo_file):
    try:
        with open(todo_file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f'Error reading todo file: {str(e)}')
        return

    total = len([l for l in lines if '- [ ]' in l])
    processed = 0
    successful = 0
    
    for line in lines:
        if '- [ ]' not in line:  # Skip already processed or invalid lines
            continue
            
        try:
            # Extract date using regex
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
            quantity_match = re.search(r'quantity=(\d+)', line)
            
            if not date_match or not quantity_match:
                print(f'Invalid line format: {line.strip()}')
                continue
                
            date = date_match.group(1).replace('-', '')  # Convert YYYY-MM-DD to YYYYMMDD
            quantity = quantity_match.group(1)
            
            processed += 1
            print(f'\nProcessing point {processed}/{total}:')
            result = add_single_point(date, quantity)
            
            if result.get('isSuccess'):
                successful += 1
                print(f'Progress: {successful}/{total} points added successfully')
            
            time.sleep(1)  # Rate limiting to avoid API issues
            
        except Exception as e:
            print(f'Error processing line: {line.strip()}\nError: {str(e)}')
            continue
    
    print(f'\nFinal Results:')
    print(f'Total points processed: {processed}')
    print(f'Successfully added: {successful}')
    print(f'Failed: {processed - successful}')

if __name__ == '__main__':
    todo_file = '../todo.txt'
    process_todo_list(todo_file)
