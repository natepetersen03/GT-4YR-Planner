class Schedule:
    def __init__ (self, schedule = {}, credits = 0):
        self.schedule = schedule
        self.credits = credits
    def addCourse(self, c, t):
        #Case where course is added with 1+ prereqs
        if not len(c.preReqs) == 0:
            for preReq in c.preReqs:
                if not preReq in self.schedule:
                    raise("Missing PreReq(s)!")
        #Any course that reaches this point can be added, so we add it to the schedule
        if self.schedule[t] == None:
            self.schedule[t] = [c]
        else:
            self.schedule[t].append(c)
        self.credits += c.creditHours
class Course:
    def __init__ (self, name, prefix, number, preReqs, creditHours):
        self.name = name
        self.prefix = prefix
        self.number = number
        self.preReqs = preReqs
        self.creditHours = creditHours




