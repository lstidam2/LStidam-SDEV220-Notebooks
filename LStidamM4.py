#11.1
from zoo import hours
hours()


#11.2
import zoo as menagerie
menagerie.hours()

#16.1
import csv
books= [
    ['author','book'],
    ['JRR Tolkien','The Hobbit'],
    ['Lynne Truss',"Eats, Shoots & Leaves"]
]
with open('books.csv', 'wt') as fout:
  csvout = csv.writer(fout)
  csvout.writerows(books)


#16.2
with open('books.csv', 'rt') as fin:
  cin = csv.reader(fin)
  books = [row for row in cin]

print(books)