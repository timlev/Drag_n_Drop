import csv

with open("words.csv", "r") as fp:
  csvreader = csv.reader(fp.readlines())

masterlist = []

for row in csvreader:
  for item in row:
    masterlist.append(item)

#print(masterlist)

COLS = 3
REMAINDER = len(masterlist) % COLS
REGULAR_ROWS = int(len(masterlist) / COLS)

print("Words:", len(masterlist))
print("Columns:", COLS)
print("Regular Rows:", REGULAR_ROWS)
print("Remainder:", REMAINDER)


cursor = 0
for r in range(REGULAR_ROWS):
  row = []
  for col in range(COLS):
    row.append(masterlist[cursor])
    cursor += 1
  print(row)
if REMAINDER != 0:
  row = []
  for i in range(REMAINDER):
    row.append(masterlist[cursor])
    cursor += 1
  print(row)
print(cursor)
