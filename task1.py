result = {'Alice':85,'Piyush':100,'Raj':90,'Shakti':95,'Jagrut':85}
name = input("Enter the student's Name: ")
if name in result.keys():
    print(f"{name}'s marks: {result[name]}")
else:
    print("Student not found")