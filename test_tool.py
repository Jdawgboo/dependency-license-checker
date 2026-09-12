import unittest
from tool import check
class LicenseTests(unittest.TestCase):
 def test_policy(self):
  report=check([{'name':'a','license':'MIT'},{'name':'b','license':'GPL-3.0'},{'name':'c'}],['MIT'],['GPL-3.0']);self.assertEqual(len(report['issues']),2);self.assertEqual(report['issues'][0]['issue'],'denied license')
if __name__=='__main__':unittest.main()
