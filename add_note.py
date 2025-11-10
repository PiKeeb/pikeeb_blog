import os
from datetime import datetime, timedelta

def add_note():
    root_folder = os.path.dirname(os.path.realpath(__file__))
    notes_folder = os.path.join(root_folder, 'notes')
    if not os.path.exists(notes_folder):
        os.makedirs(notes_folder, exist_ok=True)
        print('Notes folder created successfully!')
    else:
        print('Notes folder already exists!')
    now = datetime.now()
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    timestamp_date = now + timedelta(days=days_to_add)
    timestamp = timestamp_date.strftime('%d_%m_%Y')   
    note_path = os.path.join(notes_folder, f'{timestamp}.md')
    if os.path.exists(note_path):
        print('Note ' + note_path + ' already exists!')
    else:
        with open(note_path, 'w') as f:
            f.write(f'# {timestamp}\n\n')
        print('Note ' + note_path + ' created successfully!')

if __name__ == '__main__':
    add_note()
