with open('v2.py', mode='r') as rf:
    for i in rf.readlines():
        d1=i.replace('\n', ',')
        print(d1)

        with open('d2.py', mode='a') as wf:
          wf.write(d1)