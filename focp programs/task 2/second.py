import sys
import statistics as st

def read_file(path):
    """
    Read the contents of a file and return a list of lines.

    Args:
        path (str): The path to the file.

    Returns:
        list: A list containing lines from the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        with open(path, "r") as f:
            elements = f.readlines()
            elements.pop()  # Remove the last element (assumed to be an empty line)
        return elements
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")

def process_log_data(elements):
    """
    Process log data to count visits by our cat and other cats, and calculate total time.

    Args:
        elements (list): List of log entries.

    Returns:
        tuple: A tuple containing the count of visits by our cat, count of visits by other cats,
               and a list of total time spent during each visit.
    """
    our_cat = 0
    other_cat = 0
    total_time = []

    for x in elements:
        value = x.strip().split(",")
        first, second, third = value
        if first.lower() == "ours":
            minutes_spent = int(third) - int(second)
            total_time.append(minutes_spent)
            our_cat += 1
        else:
            other_cat += 1

    return our_cat, other_cat, total_time

def print_results(our_cat, other_cat, total_time):
    """
    Print the results of the log file analysis.

    Args:
        our_cat (int): Count of visits by our cat.
        other_cat (int): Count of visits by other cats.
        total_time (list): List of total time spent during each visit.
    """
    total_minute = sum(total_time)
    print(f"Cat visits: {our_cat}")
    print(f"Other cats: {other_cat}\n")
    print(f"Total time in house: {total_minute//60} hours, {total_minute%60} minutes\n")
    print(f"Average visit length: {st.mean(total_time):.0f} minutes")
    print(f"Longest visit: {max(total_time):9d} minutes")
    print(f"Shortest visit: {min(total_time):8d} minutes")

def main():
    """
    Main function to execute the log file analysis.

    Command-line argument:
        sys.argv[1] (str): Path to the log file.

    Prints the results of the analysis.
    """
    try:
        path = sys.argv[1]
    except IndexError:
        print("Missing command line argument")
        return

    try:
        elements = read_file(path)
    except FileNotFoundError as e:
        print(e)
        return

    log_analysis_title = "Log file analysis"
    print("\n{}\n{}\n".format(log_analysis_title, '=' * len(log_analysis_title)))

    our_cat, other_cat, total_time = process_log_data(elements)
    print_results(our_cat, other_cat, total_time)

if __name__ == "__main__":
    main()
