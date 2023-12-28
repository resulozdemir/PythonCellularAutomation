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

    def test_set_baudrate(self):
        self.modem.set_baudrate(9600)
        self.assertEqual(self.modem.baudrate, 9600)
        
    #def test_set_parity(self):
    #    self.modem.set_parity(serial.PARITY_ODD)
    #    self.assertEqual(self.modem.parity, serial.PARITY_ODD)
        
    def test_set_stopbits(self):
        self.modem.set_stopbits(serial.STOPBITS_ONE)
        self.assertEqual(self.modem.stopbits, serial.STOPBITS_ONE)
        
    def test_set_bytesize(self):
        self.modem.set_bytesize(serial.EIGHTBITS)
        self.assertEqual(self.modem.bytesize, serial.EIGHTBITS)
        
    def test_set_flowcontrol(self):
        self.modem.set_flowcontrol('software')
        self.assertEqual(self.modem.flowcontrol, 'software')
        
    def test_set_flowcontrol(self):
        self.modem.set_flowcontrol('hardware')
        self.assertEqual(self.modem.flowcontrol, 'hardware')
        
    def test_parse_at_response_for_CSQ(self):
        with patch('builtins.print') as mock_print:
            self.modem.parse_at_response('AT+CSQ', '\r\n+CSQ: 15,99\r\n\r\nOK\r\n')
            mock_print.assert_called_with('15,99')

    def test_parse_at_response_for_CGSN(self):
        with patch('builtins.print') as mock_print:
            self.modem.parse_at_response('AT+CGSN', '\r\n35978707000515\r\n\r\nOK\r\n')
            mock_print.assert_called_with('35978707000515')

    def test_parse_at_response_for_CREG(self):
        with patch('builtins.print') as mock_print:
            self.modem.parse_at_response('AT+CREG?', '\r\n+CREG: 0,1\r\n\r\nOK\r\n')
            mock_print.assert_called_with('0,1')

    def test_parse_at_response_for_COPS(self):
        with patch('builtins.print') as mock_print:
            self.modem.parse_at_response('AT+COPS?', '\r\n+COPS: 0,0,"Vodafone"\r\n\r\nOK\r\n')
            mock_print.assert_called_with('Vodafone')



if __name__ == '__main__':
    unittest.main()
