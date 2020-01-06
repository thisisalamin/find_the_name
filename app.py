import csv

total_salary = []
with open("sample.csv", 'r') as df:
    read_data = csv.reader(df)
    next(read_data)
    names = []
    for row in read_data:
        names.append(( f"{row[2]} {row[3]} {row[4]}"))

    def find_the_person(input_latter , name_list):
        upeer_latter = input_latter.upper()
        found_name = []
        for name in name_list:
            if name[0] == upeer_latter:
                found_name.append(name)
        return found_name

    given_latter = input("Enter your latter : ")
    given_names = names
    find_the_result = find_the_person(given_latter,given_names)
    
    for name in find_the_result:
        print(name)