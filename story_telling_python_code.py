"""
This is a Story telling project by Group 3 that helps a user tell his/her 
story of his/her journey so far at Azubi Africa
"""
answer = "y" #Initialize the variable to 'y' to run the loop until answer changes to any other character
while answer  == "y":
	name = input("What is your name?: ") 
	institution = input("Where are you having your training?: ")
	cohort = input("Which cohort do you belong to?: ")
	specialization = input("Which Tech Programme are signed up for?: ")
	courses = [] # Initialize an empty list to hold the courses the user has done at Azubi Africa
	course=""
	while course!="E":
		course = input("Enter Course Name or enter 'E' if you have no other course to list: ")
		
		if course!="E":
			instructor = input(f"Enter the name of the instructor for the {course} course: ")
			course_info=[course.capitalize(),instructor.capitalize()]
			courses.append(course_info)
	print("Welcome to Azubi Africa Cloud Engineering 'Story theling by Group 3 Members '\n")
	print(f"I am {name.capitalize()} a  {specialization.capitalize()} student of {institution.capitalize()} and my cohort is {cohort}.'\n")
	print(f"I have taken the following Technical courses: '\n")
	for course in courses:
		print(f"{course[0]} handled by an Instuctor by name {course[1]}, '")
	print(".We have also had Career Lab sessions that have been insightful and amazing.'\n Its been an awesome experience so far.")
	answer = input("Do you wish to try it again? If yes type 'y' else type any other key to exit the program ")
	if answer != 'y':
		print("You decided not to try again so Good bye")