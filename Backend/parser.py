# Parse the HTML code
import pandas as pd
import re
course_info = {}
course_name = ""
with open('EveryCourse.html', 'r') as f:
    crnFound = False
    course_sections = f.readlines()
    crn = 0
    course_subject = ""
    course_number = 0
    # Initialize a dictionary to store course information
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
                'CRN': crn.strip(),
                'Credit Hours': 0,
                "Prerequisites": ""
            }
with open('CourseData.txt', 'r') as f:
    courses = f.readlines()
    validCourse = False
    preReqs = False
    preReqString = ""
    credits = 0
    for a in range(len(courses)):
        #If course has not been found
        section = courses[a]
        if not validCourse:
            #Checking for identifier
            match = re.search(r"'identifier': (.*)", section)
            if match:
                match = match.group(0)
                match = match.replace("\'", "")
                match = match.replace(",", "")
                l = match.split(":")
                #Found valid course
                if l[1][1:] in course_info.keys():
                    validCourse = True
                    #storing course name
                    course_name = l[1][1:]
                    #storing credits
                    matchCred = courses[a - 1]
                    matchCred = matchCred.replace(" ", "")
                    matchCred = matchCred.replace("\'", "")
                    matchCred = matchCred.split(":")
                    matchCred = matchCred[1]
                    matchCred = matchCred.split(".")
                    if "OR" in matchCred[1]:
                        credits = matchCred[1][5]
                    #storing num of credits
                    else:
                        credits = int(matchCred[0])
        else:
            #course has prereqs check
            matchPreReq = re.search(r"'prerequisites': (.*)", section)
            if matchPreReq:
                preReqs = True
                numEmbedded = 0         
            matchEnd = re.search(r"'restrictions': (.*)", section)
            if matchEnd and preReqs:
                #Update dict, reset all values
                preReqString = preReqString.replace(")(", ") and (")
                validCourse = False
                temp = ""
                if re.search(r'(.*)[A-Z]{1}(.*)', preReqString):
                    for a in range(len(preReqString) - 1):
                        if preReqString[a] == ")" and (not (preReqString[a + 1] == " " or preReqString[a + 1] == ")")):
                            temp += ") and "
                            continue
                        temp += preReqString[a]
                    temp += preReqString[len(preReqString) - 1]
                    preReqString = temp
                course_info[course_name]["Credit Hours"] = credits
                course_info[course_name]["Prerequisites"] = preReqString
                preReqs = False
                preReqString = ""
                credits = 0
                numEmbedded = 0
            elif matchEnd:
                validCourse = False
                course_info[course_name]["Credit Hours"] = credits
                credits = 0
            #if currently in prereqs section of file
            if preReqs:
                for a in range(len(section)):
                    if section[a] == "{":
                        preReqString += "("
                        numEmbedded += 1
                    if section[a] == "}":
                        preReqString += ")"
                        numEmbedded -= 1
                        if numEmbedded == 0:
                            matchEnd = True
                            break
                    if section[a].isupper() or section[a].isnumeric():
                        preReqString += section[a] 
                    #Replacing booleans with symbol to then replace it later
                    if section[a] == " " and section[a - 1].isupper():
                        preReqString += " "
                    #add course assuming there's a new
                    if section[a] == "," and section[a - 1] == "\'":
                        preReqString += str(numEmbedded) + "*"
                    #or case
                    if section[a] == "r":
                        if section[a - 1] == "o":
                           preReqString = preReqString.replace(str(numEmbedded) + "*", " or ")
                    #and case
                    if section[a] == "d":
                        if section[a - 1] == "n":
                            if section[a - 2] == "a":
                               preReqString = preReqString.replace(str(numEmbedded) + "*", " and ")
#storing it to csv file
df = pd.DataFrame.from_dict(course_info, orient="index")
df.to_csv("CourseData.csv")
df = pd.read_csv("CourseData.csv", index_col=0)