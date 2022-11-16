# In this project you are going to evaluate the admissions data of over 1,000 colleges.
# The file "output.txt" is a sample output that I produced to show you what we expect
# your program's output to look like.

# One clarification on the definitions at play here:
#   - Applications refer to the number of students that submitted an application to the college.
#   - Admissions refer to the number of applications that the college accepted to be students.
#   - Enrollments refer to the number of students that enrolled to attend the college.

# The information about these colleges is provided to you in a .json file called "colleges.json".
# In order to load this information, you will need a "College" class that has the following variables:
#   - _name: a string that holds the name of the college.
#   - _applications: an integer that holds the number of applications that the college received.
#   - _admissions: an integer that holds the number of applications that the college accepted.
#   - _enrollments: an integer that holds the number of students that ultimately enrolled at the college.
# For each of these variables, you will want to make it a property with a getter method (you can make a
# a setter method, though we won't use it in this project).
# Write your "College" class here:


# Now that you have a "College" class, use json and jsonpickle below to load in the list of colleges to
# a variable:


# Go through this list and determine the colleges that had the most applications and the fewest applications.
# Print out your results in nice statements (see "output.txt" lines 1-2 for an example).


# Go through this list and determine the colleges that had the most admissions and the fewest admissions.
# Print out your results in nice statements (see "output.txt" lines 4-5 for an example).


# Go through this list and determine the colleges that had the most enrollments and the fewest enrollments.
# Print out your results in nice statements (see "output.txt" lines 7-8 for an example).


# Often when evaluating college admissions, we look at an admission rate, which is the percentage of applications
# that are accepted as admissions (what percentage of students get in).
# Create a method in your "College" class above that calculates the admission rate and returns it by dividing
# admissions by applications (admissions/applications).
# Utilizing that method, determine which colleges had the highest and lowest rates of admissions, and cite
# how many applications and admissions they had.
# Print out your results in nice statements (see "output.txt" lines 10-11 for an example).


# We can check a similar rate by comparing admissions and enrollments, which is what percentage of students that
# were accepted into the college ultimately decided to attend college there.
# Create a method in your "College" class above that calculates the enrollment rate and returns it by dividing
# enrollments by admissions (enrollments/admissions).
# Utilizing that method, determine which colleges had the highest and lowest rates of enrollments, and cite
# how many admissions and enrollments they had.
# Print out your results in nice statements (see "output.txt" lines 13-14 for an example).


# Now we will print detailed information about a particular college. Ask the user to enter a college name and save
# it to a variable. (see "output.txt" line 16 for an example)


# Go through the list and find the college that matches the name the user entered. Save that college to a new
# variable to work with further.


# Write an __str__ function for the "College" class above that succinctly provides all information about a college.
# Use that to print out information about the user's selected college (see "output.txt" line 18 for an example).


# Use the methods you wrote earlier to make statements about the chosen college's admission rate and enrollment
# rate (see "output.txt" lines 19-20 for an example).
