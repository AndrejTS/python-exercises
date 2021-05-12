class School:
    def __init__(self):
        self.school = {}

    def add_student(self, name, grade):
        if grade not in self.school:
            self.school[grade] = [name]
        else:
            self.school[grade].append(name)

    def roster(self):
        return [k for i in sorted(self.school) for k in sorted(self.school[i])]
            
    def grade(self, grade_number):
        if grade_number in self.school:
            return sorted(self.school[grade_number])
        return []
