from csv import DictReader, DictWriter

with open('demo.csv','r') as rf:
    with open('file2.csv','w') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['name','age','salary'])
        csv_writer.writeheader()
        for row in csv_reader:
            name, age, salary = row['name'],row['age'],row['salary']
            csv_writer.writerow({
                'name':name.upper(),
                'age':age.upper(),
                'salary':salary.upper()
            })