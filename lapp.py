import numpy as np


def pprint(*args, **kwargs):

    # The bracket "parts" include padding spaces
    LEFTTOP = chr(0x23A1) + ' '    # ⎡
    LEFTMID = chr(0x23A2) + ' '    # ⎢
    LEFTBOT = chr(0x23A3) + ' '    # ⎣
    LEFTONE = '[ '
    RIGHTTOP = ' ' + chr(0x23A4)   # ⎤
    RIGHTMID = ' ' + chr(0x23A5)   # ⎥
    RIGHTBOT = ' ' + chr(0x23A6)   # ⎦
    RIGHTONE = ' ]'
    MATRIX_SPACING = 2


    def get_matrix_widths(array):
        # Returns a list of maximum widths needed for each column
        max_widths = [0] * array.shape[1]
        for row in array:
            for i, element in enumerate(row):
                width = len(str(element))
                if width > max_widths[i]:
                    max_widths[i] = width
        return max_widths


    def print_matrix_row(array, row, widths):
        # Just print spaces if matrix has fewer rows than total rows printed
        last_row = array.shape[0] - 1
        if row > last_row:
            blank_len = sum(widths) + (len(widths)-1) * MATRIX_SPACING + 4
            print(' ' * blank_len, end='')
            return
        # Left bracket
        if row == 0:
            if last_row == 0:
                print(LEFTONE, end='')
            else:
                print(LEFTTOP, end='')
        elif row == last_row:
            print(LEFTBOT, end='')
        else:
            print(LEFTMID, end='')
        # Values
        for i, element in enumerate(array[row]):
            print(f'{array[row, i]:{widths[i]}}', end='')
            if i < len(array[row])-1:
                print(' ' * MATRIX_SPACING, end='')
        # Right bracket
        if row == 0:
            if last_row == 0:
                print(RIGHTONE, end='')
            else:
                print(RIGHTTOP, end='')
        elif row == last_row:
            print(RIGHTBOT, end='')
        else:
            print(RIGHTMID, end='')
    
    
    def print_string_row(s, row, width, str_row):
        if row == str_row:
            print(s, end='')
        else:
            print(' ' * width, end='')
        
        
    # Cycle through args to build print_items list
    #
    # Along the way:
    #
    #    * Determine how many rows we'll need to print everything
    #    * Figure out the maximum width(s) of each item
    #    * Count the number of 1D/2D array objects (vectors/matrices) passed
    
    print_items = []
    max_rows = 0
    max_widths = []
    num_arrays = 0

    for i, arg in enumerate(args):
        # Is it a vector or matrix?
        if isinstance(arg, np.ndarray):
            # Ignore higher than two dimensions
            if arg.ndim > 2:
                continue
            num_arrays += 1
            if arg.shape[0] > max_rows:
                max_rows = arg.shape[0]
            # Convert vectors into Nx1 matrices
            if arg.ndim == 1:
                arg = arg.reshape(-1, 1)
            max_widths.append(get_matrix_widths(arg))
            print_items.append(arg)
        else:
            # Not an array, so treat like a regular string
            s = str(arg)
            max_widths.append(len(s))
            print_items.append(s)

    # If no vectors or matrices were passed, treat like regular print
    if num_arrays == 0:
        print(*args, **kwargs)
        return

    # Figure out which row we'll use to print the string items
    str_row = int(max_rows/2)

    # Print each row of each print item
    for row in range(max_rows):
        for i, item in enumerate(print_items):
            if isinstance(item, np.ndarray):
                print_matrix_row(item, row, max_widths[i])
            else:
                print_string_row(item, row, max_widths[i], str_row)
        # Final newline of each row
        print()
