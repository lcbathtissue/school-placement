import numpy, GaleShapley
# GALESHAPLEY MATCHING ==> Joey Whelan , https://github.com/joeywhelan/gale-shapley/blob/main/gs.py

def read_data_from_files():
    global schools, school_preferences, students, student_preferences
    f = open("school-preferences.txt", "r")
    school_preferences = f.read().split("\n")
    schools = school_preferences[0]
    schools = schools.split(",")
    school_preferences.pop(0)  # removes header from data
    school_preferences.pop(len(school_preferences)-1)  # removes header from data

    f = open("student-preferences.txt", "r")
    student_preferences = f.read().split("\n")
    students = student_preferences[0]
    students = students.split(",")
    student_preferences.pop(0)  # removes header from data
    student_preferences.pop(len(student_preferences)-1)  # removes header from data

# reads the data into memory from the provided text files
read_data_from_files()

def get_school_ID(school_name):
    global schools
    for index, school in enumerate(schools):
        if school_name == school:
            return index
    return None

# looks up the index/ID of a school based off their school name
# used in print_entities() and convert_preferences_to_ints()

def get_student_ID(student_name):
    global students
    for index, student in enumerate(students):
        if student_name == student:
            return index
    return None

# looks up the index/ID of a student based off their student name
# used in print_entities() and convert_preferences_to_ints()

def print_entities():
    global schools, students
    print("SCHOOLS")
    for school in schools:
        print(f"[{get_school_ID(school)}] {school}")

    print("\nSTUDENTS")
    for student in students:
        print(f"[{get_student_ID(student)}] {student}")
    print()

# prints the entities involved (headers of both files, ie: school & student names)
print_entities()

def print_preferences():
    global school_preferences, student_preferences
    print("SCHOOL-PREFERENCES")
    for school_preference in school_preferences:
        prefs = school_preference.replace(",", "', '")
        print(f"'['{prefs}']"[1:])
    print("\nSTUDENT-PREFERENCES")
    for student_preference in student_preferences:
        prefs = student_preference.replace(",", "', '")
        print(f"'['{prefs}']"[1:])

# prints the preferences as is, formatted like a multidimensional array (but not converted)
print_preferences()

def convert_preferences_to_ints():
    global school_preferences, student_preferences
    global converted_school_preferences, converted_student_preferences

    converted_school_preferences = []
    for sub_array in school_preferences:
        converted_sub_array = []
        sub_array = sub_array.split(",")
        for student in sub_array:
            converted_sub_array.append(get_student_ID(student))
        converted_school_preferences.append(converted_sub_array)

    converted_student_preferences = []
    for sub_array in student_preferences:
        converted_sub_array = []
        sub_array = sub_array.split(",")
        for school in sub_array:
            converted_sub_array.append(get_school_ID(school))
        converted_student_preferences.append(converted_sub_array)

    print("\nSCHOOL-PREFERENCES (AS INTEGERS)")
    for school_preference in converted_school_preferences:
        print(school_preference)

    print("\nSTUDENT-PREFERENCES (AS INTEGERS)")
    for student_preference in converted_student_preferences:
        print(student_preference)

# converts the preference matrices into matrices containing index values
# (rather than string values ie: UofO -> 0, Sara -> 1)
convert_preferences_to_ints()

def convert_to_array_and_transpose():
    global sch_prefs, school_preferences, stu_prefs, student_preferences
    sch_prefs = []
    for ele in school_preferences:
        ele = ele.split(",")
        sch_prefs.append(ele)
    sch_prefs = numpy.transpose(sch_prefs).tolist()

    stu_prefs = []
    for ele in student_preferences:
        ele = ele.split(",")
        stu_prefs.append(ele)
    stu_prefs = numpy.transpose(stu_prefs).tolist()

# converts the arrays containing string values representing choices
# from the original text files into a pair of two-dimensional arrays
# then performs a transposition on the data using the numpy library
convert_to_array_and_transpose()

def convert_preferences_to_dict():
    global pref_dict, sch_prefs, schools, stu_prefs, students
    pref_dict = {}
    for index, school in enumerate(schools):
        values = sch_prefs[index]
        pref_dict[school] = values
    for index, student in enumerate(students):
        values = stu_prefs[index]
        pref_dict[student] = values

# formats all preferences for all entities into a python dictionary to
# be passed to the GaleShapley.gale_shapley(prefs, proposers) as args
convert_preferences_to_dict()


def find_matches_and_print():
    matches = GaleShapley.gale_shapley(pref_dict, schools)
    print("\nBEST MATCHES:")
    for match in matches:
        print(match)

# runs GaleShapley.gale_shapley(prefs, proposers) and returns a
# a list of matches when given a dictionary of all preferences
# for all entities and a list of 'proposers', *SEE CREDIT AT TOP
find_matches_and_print()
