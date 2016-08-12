import unittest
from exercises import hexdec

###############################################################################

class ValidInput(unittest.TestCase):
    pair = ( (1,'1'),
             (2,'2'),
             (3,'3'),
             (4,'4'),
             (5,'5'),
             (6,'6'),
             (7,'7'),
             (8,'8'),
             (9,'9'),
             (10,'A'),
             (11,'B'),
             (12,'C'),
             (13,'D'),
             (14,'E'),
             (15,'F'),
             (16,'10'),
             (30,'1E'),
             (127,'7F'),
             (255,'FF'),
             (500,'1F4'),
             (1024,'400'),
             (5100,'13EC'),
             (65535,'FFFF'),
             (65536,'10000') )

    def testToHex(self):
        for d, h in self.pair:
            self.assertEqual(hexdec.toDec(h), str(d))
            self.assertEqual(hexdec.toHex(str(d)), h)

###############################################################################

class InvalidInput(unittest.TestCase):
    def testToHexNegative(self):
        '''toHex should fail when the input < 0'''
        self.assertRaises(hexdec.NotIntegerError, hexdec.toHex, str(-1))

    def testToHexNonInteger(self):
        '''toHex should fail with non-integer input'''
        self.assertRaises(hexdec.NotIntegerError, hexdec.toHex, str(0.5))

    def testToDecNegative(self):
        '''toDec should fail when the input < 0'''
        self.assertRaises(hexdec.NotHexadecimalError, hexdec.toDec, str(-1))

    def testToDecNonInteger(self):
        '''toDec should fail with non-integer input'''
        self.assertRaises(hexdec.NotHexadecimalError, hexdec.toDec, str(0.5))

###############################################################################

if __name__ == '__main__':
    unittest.main()
