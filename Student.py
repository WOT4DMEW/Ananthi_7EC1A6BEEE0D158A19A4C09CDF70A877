class student():
  def __init__(self,name,roll,cgpa):
       self.name=name
       self.roll=roll
       self.cgpa=cgpa

def sortcgpa(sortlist):
  sortedstu=sorted(sortlist, key=lambda x: x.cgpa, reverse=True)
  return sortedstu

stuobj=[student("Jeevitha","22CS2139",8.8),student("Aishwarya","22CS2136",8.0),student("Sujitha","22CS2147",7.5),student("Sabila","22CS2143",9.8)]
sortedstu=sortcgpa(stuobj)

for stu in sortedstu:
  print(f"Name: {stu.name}   Roll.no: {stu.roll}    CGPA: {stu.cgpa}")