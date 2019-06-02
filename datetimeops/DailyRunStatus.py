import os
from datetime import datetime

directory = "/home/dharani/DailyRunStatus"

try:
    directory_available = os.path.exists(directory)
    if directory_available:
        print("The directory '", directory, "' is already available. So not creating it..!")
    else:
        print("The directory '", directory, "' is not available. So creating it..!")
        os.mkdir(directory)
except Exception as e:
    print("I could not create the directory, the reason is ", repr(e))
    print("Also Exiting the application")
    SystemExit(e)


def get_file_name():
    return str(datetime.now().date())


def open_file_and_write_data(in_file_name):
    try:
        file = open(in_file_name, "a")
        to_be_appended = "Writing at : "+str(datetime.now())+"\n"
        file.write(to_be_appended)
        file.close()
        print("Appended to the file..")
    except FileNotFoundError as fne:
        raise FileNotFoundError(fne)


file_name = get_file_name()
print("The file name to be : ", file_name)

try:
    file_full_path = directory+"/"+file_name
    file_available = os.path.exists(file_full_path)
    if file_available:
        print("The file '", file_full_path, "' is available. so not creating it..!")
        open_file_and_write_data(file_full_path)
    else:
        print("The file '", file_full_path, "' is not available. so creating it..!")
        current_file = open(file_full_path, 'x')
        current_file.close()
        open_file_and_write_data(file_full_path)
except Exception as e:
    print("Could not complete the operation - reason : ", repr(e))
