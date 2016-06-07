import unittest
import orderDayToVendor as odv


class MyTest(unittest.TestCase):
  
  def test_day_conversion(self):
    self.assertEqual(odv.calculate_order_day_to_vendor([0,1,0,0,0,1,0]), [0,4,0,0,0,3,0])
    self.assertEqual(odv.calculate_order_day_to_vendor([0,1,0,0,0,1,0]), [0,4,0,0,0,3,0])
	
  def pass_test(self):
    self.assertTrue(True)
	
  def fail_test(self):
    self.assertFalse(False)