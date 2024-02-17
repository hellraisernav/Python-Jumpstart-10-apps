import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("------------------------------")
    print("\t Journal App")
    print("------------------------------")


def run_event_loop():
    print("what do you want to do with your Journal?")
    cmd = 'Empty'
    journal_name = "default"
    journal_data = journal.load(journal_name)
    
    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries,[A]dd an entry, E[x]it:')
        if cmd.lower().strip() == "l":
            list_entries(journal_data)
        elif cmd.lower().strip() == 'a':
            add_entry(journal_data)
        elif cmd.lower().strip() != "x" and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
    print("Done, Goodbye")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("your journal entries:")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("{}- {}".format(idx+1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to Exit:')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()