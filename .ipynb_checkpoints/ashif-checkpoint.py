with open("ashif.txt","w") as f:
    f.write("hello everybody \n i am ashif ali\n i am learn pytho for data science")

with open("ashif.txt","r") as f:
    data = f.read()
    print(data)
    