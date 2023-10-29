import csv

prev_title = None
with open('pg.csv', 'r') as csvfile, open('output.txt', 'w') as txtfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        cur_title = row['essay_title']
        if cur_title != prev_title:
            txtfile.write(f'\n{cur_title}\n')
        txtfile.write(f"{row['content']}\n")
        prev_title = cur_title
