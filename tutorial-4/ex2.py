

total = 0 
count = 0 

score = int(input("Enter score, (Enter -9 to end): ") )

if score != -9:
    while score != -9:
        total += score
        count += 1
        score = int(input("Enter next score, (Enter -9 to end): ") )
        
    average = float( total ) / count
    print("Class average is", average)
else:
    print("Please enter a score first")