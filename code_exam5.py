class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"
        
    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName==course:
                if (0<=grade) and (grade<=100):
                    self.myCourses[i].setGrade=grade
        #pass

    def getGrade(self, course):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName==course:
               return self.myCourses[i].grade
            elif self.myCourses[i].courseName!=course:
                return -1
        
        #pass

    def setPset(self, pset, score, course):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName==course:     
                self.myCourses[i].psetsDone.append((pset, score))
        #pass

    def getPset(self, pset, course):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName==course:
                for (p, score) in self.myCourses[i].psetsDone:
                    if p == pset:
                        return score
                    else:
                        return -1
                        
        #pass
'''        
edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setGrade(100, "6.00x")
edX.setGrade(90, "6.01x")
edX.setGrade(80, "6.02x")
edX.getGrade("6.00x")
100
edX.getGrade("6.01x")
90
edX.getGrade("6.02x")
80


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setGrade(100, "6.00x")
edX.setGrade(90, "6.01x")
edX.setGrade(80, "6.02x")
edX.setGrade(50)
edX.getGrade("6.00x")
100
edX.getGrade("6.01x")
90
edX.getGrade("6.02x")
80
edX.getGrade()
80


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setGrade(100, "2.01x")
edX.getGrade("2.01x")
-1

edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(2, 100,"6.02x")
edX.setPset(2, 90,"6.02x")
edX.setPset(3, 95,"6.02x")
edX.getPset(2, "6.02x")
100
edX.getPset(3, "6.02x")
95
edX.getPset(4, "6.02x")
None

edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(2, 100,"6.02x")
edX.setPset(2, 90,"6.02x")
edX.setPset(3, 95,"6.02x")
edX.setPset(4, 100)
edX.getPset(2, "6.02x")
100
edX.getPset(3, "6.02x")
95
edX.getPset(4)
100


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(2, 100,"6.02x")
edX.setPset(2, 100,"2.01x")
edX.getPset(2, "6.02x")
100
edX.getPset(3, "6.02x")
None
edX.getPset(2, "2.01x")
-1


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1,100)
edX.setPset(2,100,"6.00x")
edX.setPset(2,90,"6.00x")

edX.setGrade(100)

for c in ["6.00x","6.01x","6.02x"]:
    edX.setGrade(90,c)
'''