import pandas as pd

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of 3 marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 85:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 50:
            return 'C'
        else:
            return 'Fail'


# ---------- Collect Student Data ----------
students = []

print("📘 Enter student data (type 'done' to finish):")
while True:
    name = input("Enter name: ")
    if name.lower() == 'done':
        break
    try:
        marks = [
            int(input("Enter mark 1: ")),
            int(input("Enter mark 2: ")),
            int(input("Enter mark 3: "))
        ]
        students.append(Student(name, marks))
    except ValueError:
        print("❌ Invalid input! Please enter numeric marks.")

# ---------- Save to CSV ----------
data = []
for s in students:
    data.append({
        'Name': s.name,
        'Total': s.total(),
        'Average': s.average(),
        'Grade': s.grade()
    })

df = pd.DataFrame(data)
df.to_csv("student_results.csv", index=False)
print("\n✅ Results saved to student_results.csv!\n")

# ---------- Analysis ----------
print("📊 Top Performers:")
print(df.sort_values(by='Average', ascending=False).head(3), "\n")

print("🏆 Grade Count:")
print(df['Grade'].value_counts())
