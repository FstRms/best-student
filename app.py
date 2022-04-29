"""Show me the best student in the class"""

import argparse


def find_best_student(sorted_data: list) -> list:
    """Find the best student in the class from sorted data"""
    best_students = [sorted_data[0]]
    # If more than one student has the highest score, let's append them all
    for student in sorted_data[1:]:
        if student[2] == best_students[0][2]:
            best_students.append(student)
    # We no longer need the score, so let's remove it
    for each in best_students:
        each.pop(2)
    return best_students


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", type=str, help="The input file")
    parser.add_argument("out_file", type=str, help="The output file")
    all_lines = []
    # Open file and append each line to all_lines list
    with open(parser.parse_args().in_file, "r") as in_file:
        for line in in_file:
            all_lines.append(line.replace("\n", "").split(","))
    # We don´t need the first line
    all_lines.pop(0)
    # Sort each nested list by the third element in descending order
    sorted = sorted(all_lines, key=lambda x: x[2], reverse=True)
    best_students = find_best_student(sorted)
    # Open output file and write the best students
    with open(parser.parse_args().out_file, "w") as out_file:
        for student in best_students:
            out_file.write(" ".join(student) + "\n")
