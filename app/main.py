from db import total, average

def run():
    print("=== Marks Calculator ===")

    marks = []

    n = int(input("How many subjects? "))

    for i in range(n):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    print("\n--- Result ---")
    print("Marks:", marks)
    print("Total:", total(marks))
    print("Average:", average(marks))


if __name__ == "__main__":
    run()