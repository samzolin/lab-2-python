# Author: Samantha Zolin saz5193@psu.edu
# Collaborator: Christian Davis ckd5367@psu.edu
# Collaborator: Samarth Tehri sqt5555@psu.edu
# Collaborator: Bryce Graf bag5620@psu.edu
# Section: 10
# Breakout: 3

def run():
  score = input("Enter your CMPSC 131 grade: ")
  score = float(score)
  grade = getLetterGrade(score)
  print(f"Your letter grade for CMPSC 131 is {grade}.")

def getLetterGrade(n):
  if n >= 93.0 and n >= 100.0:
    return "A"
  elif n >= 90.0 and n < 93.0:
    return "A-"
  elif n >= 87.0 and n < 90.0:
    return "B+"
  elif n >= 83.0 and n < 87.0:
    return "B"
  elif n >= 80.0 and n < 83.0:
    return "B-"
  elif n >= 77.0 and n < 80.0:
    return "C+"
  elif n >= 70.0 and n < 77.0:
    return "C"
  elif n >= 60.0 and n < 70.0:
    return "D"
  else:
    return "F"

if __name__ == "__main__":
  run()

    
