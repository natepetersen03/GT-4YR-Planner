# Parse the HTML code
import pandas as pd
con = msql.connect("localhost", "natepetersen", "Nateyp123!", "4YRPlanner")
import re
with open('EveryCourse.html', 'r') as f:
    print("hey")
    crnFound = False
    course_sections = f.readlines()
    course_name = ""
    crn = 0
    course_subject = ""
    course_number = 0
    # Initialize a dictionary to store course information
    course_info = {}
    # Iterate through each course section
    for section in course_sections:
    # Extract the course name, course subject, and course number using regex
        #Matches strings in the ">ANYSTRING - 5*(0-9) - 2-4UPPER (1-4)(3*0-9)" format that is used in the html file
        match = re.search(r'>[A-Z]{1}.+ - \d{5} - [A-Z]{2,4} [1-4]\d{3}', section)
        if match:
            match = match.group(0)
            match = match.replace(" - ", "* ")
            match = match.replace(">", "")
            match = match.replace("  ", " ")
            l = match.split("* ")
            if len(l) > 3:
                l[0] = l[0] + " " + l[1]
                temp = l[2]
                l[2] = l[3]
                l[1] = temp
            if l[1] in course_sections:
                continue
            cSubjAndNum = l[2].split(" ")
            l[2] = cSubjAndNum[0]
            l.append(cSubjAndNum[1])
            #Split the string into a list by removing unnecessary characters
            course_name = l[0]
            crn = l[1]
            course_subject = l[2]
            course_number = l[3]
            course_info[course_subject + " " + course_number] = {
                'Course Name': course_name.strip(),
                'CRN': crn.strip()
            }
            
df = pd.DataFrame.from_dict(course_info, orient="index")
df.to_csv("CourseData.csv")
df = pd.read_csv("CourseData.csv", index_col=0)