from log2d import Log

def main():
    log_show = Log("showcase", to_file=True)
    log_show("This is the first line")
    log_show("This is the second line")
    print("This is the path to the log " + log_show.path.__str__())

if __name__ == "__main__":
    main()