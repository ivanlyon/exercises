'''
Encode text using Playfair algorithm

Status: Accepted
'''

###############################################################################

class Playfair():
    """Data and operations of playfair cipher"""

    def __init__(self, key_phrase=''):
        minus_q = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
        key = ''
        for glyph in key_phrase.upper():
            if glyph in minus_q and not glyph in key:
                key += glyph
        for glyph in minus_q:
            if not glyph in key:
                key += glyph
        self.key = key
        self.row, self.column, self.lut = {}, {}, {}
        for index, glyph in enumerate(key):
            self.row[glyph] = index // 5
            self.column[glyph] = index % 5
            self.lut[(index // 5, index % 5)] = glyph

    def __repr__(self):
        rows = [self.key[i:i+5] for i in range(0, 25, 5)]
        return '\n'.join(rows)

    def encode(self, plaintext):
        """Encode plain text using playfair configured at instantiation"""

        pt2 = list(plaintext.upper().replace(' ', ''))
        index = 0
        result = ''
        while index < len(pt2):
            letter1 = pt2[index]
            if index + 1 == len(pt2):
                pt2 += 'X'

            letter2 = pt2[index + 1]
            if letter1 == letter2:
                pt2 = pt2[:index + 1] + ['X'] + pt2[index + 1:]
                letter2 = 'X'

            if self.row[letter1] == self.row[letter2]:
                result += self.lut[(self.row[letter1], (self.column[letter1] + 1) % 5)]
                result += self.lut[(self.row[letter2], (self.column[letter2] + 1) % 5)]
            elif self.column[letter1] == self.column[letter2]:
                result += self.lut[((self.row[letter1] + 1) % 5, self.column[letter1])]
                result += self.lut[((self.row[letter2] + 1) % 5, self.column[letter2])]
            else:
                result += self.lut[(self.row[letter1], self.column[letter2])]
                result += self.lut[(self.row[letter2], self.column[letter1])]
            index += 2
        return result

###############################################################################

def main():
    """Read input and print output score of playfair encoding"""

    cipher = Playfair(input())
    print(cipher.encode(plaintext=input()))

###############################################################################

if __name__ == '__main__':
    main()
