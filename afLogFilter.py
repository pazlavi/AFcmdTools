# script for filtering logs files and extract only appsflyer related logs
# pass files path as command line arguments.
# after the file is filtered, select if you want to print the result to the console or save it as a new file
import sys


# for each path filter the logs
def filter_logs_file(argv):
    if len(argv) > 1:
        for args in argv[1::]:
            filter_one_file(args)  # filter file
    else:
        print("no file")


# filter file
def filter_one_file(file):
    print("\n\nfiltering file: " + file)
    filters_logs = ""  # filtering result
    f = open(file, "r")  # open the input file
    lines = f.readlines()  # read all lines as list of lines
    for line in lines:  # perform for each line
        if "appsflyer" in line.lower():  # if line contains "appsflyer"
            filters_logs += line  # add the line to the result
    print_or_save(filters_logs)  # print or save the filtering result


# print or save the filtering result
def print_or_save(logs):
    print("\nSave to file or print to console?\nenter [f] file or [c] console (default is console)")
    c = input()  # get output method
    if c.lower() == "f":  # if selected file
        print("\nenter save path (keep empty for current directory)")
        path = input().strip()  # get save directory. empty for current directory
        print("\nenter file name")
        name = input().strip()  # enter file name
        if "." not in name:  # if file without extension, save as txt file
            name += ".txt"
        file_path = name if path == "" else path + "/" + name  # build the file path
        try:
            f = open(file_path, "w")  # open the new file
            f.write(logs)  # write the results
            f.close()  # cole the file
            print("file save: " + file_path)
        except Exception as e:  # if file creation failed
            print(e)
            print("try again? [y]/[n]")  # ask the user if try to save/print again or skip the results
            c = input()
            if c.lower() == "y":  # if try again, call this method again with the same logs (recursive call)
                print_or_save(logs)
            else:
                print("skipping this file")

    else:
        print(logs)


if __name__ == '__main__':
    filter_logs_file(sys.argv)  # filter files
