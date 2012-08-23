import os,unittest,subprocess

class CastorCli(unittest.TestCase):

  def setUp(self):
    self.devnull = open(os.devnull, 'w')

  def test_nsls1(self):
    a = subprocess.call(['nsls','/castor/cern.ch'], stdout=self.devnull)
    self.assertEqual(a, 0)

  def test_nsls2(self):
    b = subprocess.call(['nsls','/castor/path/does/not/exist'], stderr=self.devnull)
    self.assertEqual(b, 1)


if __name__ == '__main__':
  unittest.main()
