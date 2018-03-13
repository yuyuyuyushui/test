import unittest, os
base_path = os.path.dirname(os.path.abspath(__file__))
data_base = os.path.join(base_path,'test_case')
print(data_base)
def all_case():
    case_dir = data_base
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    testcase.addTest(discover)
    print(testcase)
    return testcase
if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())