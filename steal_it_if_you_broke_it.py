import csv
import os
import subprocess
import sqlite3

app_data = os.getenv('APPDATA')

##### Convert the streamrip downloads database to a csv file
import_choice = input("Do you want to convert the Streamrip db to a .csv? (y/n): ").strip().lower()

if import_choice == 'y':

    db_path = f'{app_data}/streamrip/downloads.db'
    csv_db_path = f'{app_data}/streamrip/output.csv'

    sql_query = 'SELECT id FROM downloads'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    # Write the results to a CSV file
    with open(csv_db_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header
        csv_writer.writerow(['sequence_column'])
        # Write the data
        csv_writer.writerows(rows)

    conn.close()

    print(f"Data successfully written to {csv_db_path}")

##### download all the files from the .csv
import_choice = input("Do you want to download all previously downloaded Streamrip files? (y/n): ").strip().lower() # note: you will need to move the Streamrip .db manually otherwise it will just say already in database

if import_choice == 'y':

    csv_path = f'{app_data}/streamrip/output.csv'

    with open(csv_path, mode='r') as csv_file:
        # csv_reader = csv.reader(reversed(csv_file.readlines()))
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    middle_index = len(rows) // 2

    for row in rows[middle_index:]:
        sequence = row[0]
        url = f'https://tidal.com/browse/track/{sequence}?u'
        command = f'rip url {url}'
        
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the command: {e}")

print("All commands executed.")
