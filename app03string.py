course = "Python for beginners" #course is a string object
print(course.upper())
print(course) #will be as original not uppercase
#we have also: lower;
print(course.find("y")) #find("y"):it will gie us the index of y in the str;if there is no y we get -1
print("Python" in course) #same as find: do we have Python in course? but when we run we get True not the index
print(course.replace("for", "4")) # we get Python 4 beginners