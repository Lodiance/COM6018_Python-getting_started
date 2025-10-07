import csv

csv_path = "./20251006/windfarm.csv"

# Open the file with csv.reader
with open(csv_path) as csvfile:

    # Attach a reader to the file
    windfarm_reader = csv.reader(csvfile, skipinitialspace=True)

    # Read each row (as a list) and store them as a list of lists.
    data = [row for row in windfarm_reader]

    print(f"[List data]\n{data}")
    print("------------------------")

# Open the file with csv.DictReader
with open(csv_path) as csvfile:

    # Attach a DictReader to the file
    windfarm_reader = csv.DictReader(csvfile, skipinitialspace=True)

    # Read each row as a dictionary and store as a list of dictionaries.
    data = [row for row in windfarm_reader]

    print(f"[Dict data]\n{data}")
    print("------------------------")


# Quote Non-Numeric data in the dict
with open(csv_path) as csvfile:
    windfarm_reader = csv.DictReader(
        csvfile, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC
    )
    # ... windfarm_reader is now a DictReader which will read each row as a dictionary
    # The line below remains exactly the same but now generates a list of dicts.
    data = [row for row in windfarm_reader]

    print(f"[Quote data]\n{data}")
    print("------------------------")
