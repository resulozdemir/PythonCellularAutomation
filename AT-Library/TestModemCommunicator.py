import unittest
from unittest.mock import Mock, patch
import serial
from ModemCommunicator import ModemCommunicator

class TestModemCommunicator(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('serial.Serial')
        self.mock_serial = self.patcher.start()
        self.modem = ModemCommunicator()

    def tearDown(self):
        self.patcher.stop()


    #Will be updated soon.
    

if __name__ == '__main__':
    unittest.main()
