print("francis musyoka")


# keyword is def


def username():
  print("francis")

  # passing arguments in my functions

  def full_name(fname, lname):
    print(fname + " " + lname)

    full_name("francis", "musyoka")
    full_name("franK", "muka")
    full_name("sylvester", "sam")


def calcit(x):
  return 9 * x


print(calcit(9))
print(calcit(20))
print(calcit(3))


# return to give value of rwo numbers

def addition(x, y):
  return (x + y)


name = str(input("what is your name ? "))
weight = int(input("enter the weight here : "))
height = float(input("enter the height here : "))


def bmic(name, weight, height):
  bmi = weight / (height * height)
  if (bmi <= 20):
    return f"{name} is underweight", bmi
  elif (bmi <= 30):
    return f"{name} is overweight", bmi
  elif (bmi <= 40):
    return f"{name} is obese", bmi
  else:
    return f"{name} is overweight", bmi

    bmi = bmicalc(name, weight, height)
    print(f"bmi")


x = int(input("Enter value of x :"))
y = int(input("Enter value of y :"))
z = x * y

if z < 200:
  print("Ideal weight")
elif z > 200:
  print("Overfed baby")

name = input("Enter first name ")

if name == "Francis":
  print("Student already exists")
else:
  print("New student")

# Build a grading system for students

stdname = input("Students name")
grades = int(input("Total score"))


# Accept name and print name
# A - 85 , B  - 70 , C - 60 ,D - 50 , E- 40

# functions to grade
def avg_grade(marks):
  tots = len(marks)
  total_score = sum(marks)
  avg = total_score / tots
  return avg


def grading(avg):
  if avg >= 85:
    grade = "A"
  elif avg >= 70:
    grade = "B"
  elif avg >= 60:
    grade = "C"
  elif avg >= 50:
    grade = "D"
  elif avg <= 40:
    grade = "E"
  else:
    print("Value below entry points")


marks = [80, 73, 78, 21, 89, 59, 49]
avg = avg_grade(marks)
print("Francis average grade is ", avg)
