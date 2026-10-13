# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 and row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break
        if not ok:
                break
       

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
    

# Lab 2.5.11 - Sudoku
#
# Purpose:
# Check whether a completed 9x9 Sudoku board is valid.
#
# Assumptions:
# 1. The user enters 9 rows of Sudoku.
# 2. Each row must contain exactly 9 digits.
# 3. Each digit must be between 1 and 9.
# 4. Each row must contain digits 1 through 9 exactly once.
# 5. Each column must contain digits 1 through 9 exactly once.
# 6. Each 3x3 sub-square must contain digits 1 through 9 exactly once.
# 7. Invalid row input will prompt the user to enter the row again.
# 8. The program prints "Yes" for a valid Sudoku and "No" otherwise.
#
# Tracing:
# 1. Define the checkset() function to verify digits 1 through 9.
# 2. Create an empty list called rows to store the Sudoku board.
# 3. Use a for loop to read 9 rows from the user.
# 4. Use a while loop to validate the length and characters of each row.
# 5. If the input is invalid, ask the user to enter the row again.
# 6. Append each valid input row to the rows list.
# 7. Initialize ok = True before checking the Sudoku board.
# 8. Check every row using the checkset() function.
# 9. If any row is invalid, set ok = False and stop checking.
# 10. If all rows are valid, check every column.
# 11. Create a list containing the digits of each column.
# 12. Use checkset() to verify each column.
# 13. If all columns are valid, check the nine 3x3 sub-squares.
# 14. Use nested loops to select each 3x3 sub-square.
# 15. Combine the digits of each sub-square into a string.
# 16. Use checkset() to verify each sub-square.
# 17. If any row, column, or sub-square is invalid, set ok = False.
# 18. Print "Yes" if ok is True; otherwise, print "No".

