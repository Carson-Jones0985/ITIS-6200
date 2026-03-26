
Levels = dict()
Levels["U"] = 1
Levels["C"] = 2
Levels["S"] = 3
Levels["TS"] = 4

class Subject:
    def __init__(self, name, max_level, start_level):
        self.name = name
        self.max_level = max_level
        self.start_level = start_level
        self.current_level = start_level

class Object:
    def __init__(self, file_name, file_level):
        self.file_name = file_name
        self.file_level = file_level

class BLPModel:
    def __init__(self):
        self.subjects = dict()
        self.objects = dict()

    def add_subject(self, name, max_level, start_level):
        if (name in self.subjects):
            print(f"Subject already in dictionary")
            return
        else:
            self.subjects[name] = Subject(name, max_level, start_level)
    
    def add_object(self, file_name, file_level):
        if (file_name in self.objects):
            print(f"Object already in dictionary")
            return
        else:
            self.objects[file_name] = Object(file_name, file_level)
        
    def validate_levels(self, subject_name, object_name):
        return Levels[self.subjects[subject_name].current_level] == Levels[self.objects[object_name].file_level]
    
    def set_level(self, subject_name, new_level):
        if (Levels[new_level] > Levels[self.subjects[subject_name].max_level]):
            print(f"DENY -- Cannot update {self.subjects[subject_name].name}'s level because the new level {new_level} cannot exceed max clearance {self.subjects[subject_name].max_level}")
            return
        elif (Levels[new_level] < Levels[self.subjects[subject_name].current_level]):
            print(f"DENY -- Cannot update {self.subjects[subject_name].name}'s level because the new level {new_level} cannot be lower than the current level {self.subjects[subject_name].current_level}")
            return
        else:
            self.subjects[subject_name].current_level = new_level
            print(f"ALLOW -- Updated {self.subjects[subject_name].name}'s level to {new_level}")
    
    def read(self, subject_name, object_name):
        
        if (Levels[self.subjects[subject_name].current_level] >= Levels[self.objects[object_name].file_level]):
            print(f"ALLOW -- {self.subjects[subject_name].name} is allowed read {self.objects[object_name].file_name} because their level {self.subjects[subject_name].current_level} is equal or greater than {self.objects[object_name].file_level} ")
            return
        elif (Levels[self.objects[object_name].file_level] <= Levels[self.subjects[subject_name].max_level]):
            self.set_level(subject_name, self.objects[object_name].file_level)
            print(f"ALLOW -- {self.subjects[subject_name].name} had their level updated and can now read {self.objects[object_name].file_name} because their level {self.subjects[subject_name].current_level} is equal or greater than {self.objects[object_name].file_level}")
            return
        else:
            print(f"DENY -- {self.subjects[subject_name].name} cannot read {self.objects[object_name].file_name} because their level {self.subjects[subject_name].current_level} is not equal or greater than {self.objects[object_name].file_level}")
            return

    def write(self, subject_name, object_name):
        if (Levels[self.subjects[subject_name].current_level] <= Levels[self.objects[object_name].file_level]):
            print(f"ALLOW -- {self.subjects[subject_name].name} is allowed to write to {self.objects[object_name].file_name} because their level {self.subjects[subject_name].current_level} equal to or less than {self.objects[object_name].file_level}")
            return
        else:
            print(f"DENY -- {self.subjects[subject_name].name} is not allowed to write to {self.objects[object_name].file_name} because their level {self.subjects[subject_name].current_level} not equal to or less than {self.objects[object_name].file_level}")
            return
        
        
