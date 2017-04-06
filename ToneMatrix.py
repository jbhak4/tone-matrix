# John B. Hannan, 4/30/2014
# This file contains the ToneMatrix class.  When run from the command line with
# arguments in the form of pitch-class integers, the matrix will be generated
# and printed.

# This class is initialized with a list of integers which represent a tone row.
# There is no minimum length for this row.
class ToneMatrix:
    # Initialize the class by generating the matrix
    def __init__(self, row):
        # Initialize data members
        # Uncomment to transpose given row to start on 0
        #row = self.zero_t(row)
        self.row = row
        self.list = []

        # Generate the tone row matrix
        self.__generate()

    # This is called when printing or converting the object to a string
    def __str__(self):
        out_str = ''

        # Add each row to the output string
        for t in range(len(self.list)):
            out_str += self.format(self.list[t])

            # Do not include newline on final row
            if t < len(self.list) - 1:
                out_str += '\n'

        return out_str

    # Create a row string suitable for printing, with <> to indicate an ordered
    # pc set and with each pc separated by a comma and a space for readability
    def format(self, row):
        out_str = '<'
        # Convert to string with no formmatting
        row_str = self._to_string(row)
        # Add all but final pc to output string
        for pc in row_str[:-1]:
            out_str += pc + ', '

        # Add final pc to output string
        out_str += row_str[-1] + '>'

        return out_str

    # Transpose tone row to start on 0
    def zero_t(self, row):
        first_pitch = row[0]
        # Calculate index of transposition
        diff = (0 - first_pitch) % 12

        # Transpose row by diff
        new_row = [(pc + diff) % 12 for pc in row]
        
        return new_row

    # Invert tone row
    def invert(self, row):
        inverted = []
        target = (row[0] * 2) % 12

        for n in row:
            inverted.append((target - n) % 12)

        return inverted

    # Search for ordered pc set
    def search(self, opc_set):
        result = []
        opc_str = self._to_string(opc_set)

        # check row forms
        for n in range(len(self.list)):
            column = [row[n] for row in self.list]
            if opc_str in self._to_string(self.list[n]):
                result.append('P {}'.format(self.list[n][0]))

            if opc_str in self._to_string(self.list[n])[::-1]:
                result.append('R {}'.format(self.list[n][0]))

            if opc_str in self._to_string(column):
                result.append('I {}'.format(self.list[0][n]))

            if opc_str in self._to_string(column)[::-1]:
                result.append('RI {}'.format(self.list[0][n]))

        return result

    # Return specified transposition
    def P(self, pc):
        index = None
        for n in range(len(self.list)):
            if self.list[n][0] == pc:
                index = n
                break

        return self.format(self.list[index])

    # Return specified retrograde
    def R(self, pc):
        index = None
        for n in range(len(self.list)):
            if self.list[n][0] == pc:
                index = n
                break

        return self.format(self.list[index][::-1])

    # Return specified inversion
    def I(self, pc):
        index = None
        for n in range(len(self.list[0])):
            if self.list[0][n] == pc:
                index = n
                break

        return self.format([row[index] for row in self.list])

    # Return specified retrograde inversion
    def RI(self, pc):
        index = None
        for n in range(len(self.list[0])):
            if self.list[0][n] == pc:
                index = n
                break

        return self.format([row[index] for row in self.list][::-1])

    # Convert row to string
    def _to_string(self, row):
        row_str = ''
        for pc in row:
            if pc == 10:
                row_str += 'T'
            elif pc == 11:
                row_str += 'E'
            else:
                row_str += str(pc)

        return row_str

    # Create tone row matrix
    def __generate(self):
        # Create inverted row
        inverted = self.invert(self.row)

        self.list.append([])
        # Add initial row to matrix
        for pc in self.row:
            self.list[0].append(pc)

        # Add each row, with starting values in order of initial inversion
        for index in range(1, len(inverted)):
            # Add initial pc of inversion to row
            self.list.append([inverted[index]])

            # Calculate adjacent intervals and add new pcs to row
            diff = (self.list[index][0] - self.list[index - 1][0]) % 12
            for sub_index in range(1, len(inverted)):
                new_pc = (self.list[index - 1][sub_index] + diff) % 12
                self.list[index].append(new_pc)

if __name__ == '__main__':
    import sys

    try:
        tm = ToneMatrix([int(n) for n in sys.argv[1:]])
    except (ValueError, IndexError):
        print("Incorrect argument provided")
    else:
        print(tm)
