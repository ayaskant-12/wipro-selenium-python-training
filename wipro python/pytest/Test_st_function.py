# function level set up and tear down
# these run before and after each test function

# set up at function level
def setup_function(function):
    print("opening the browser")

# teardown up at function level

def teardown_function(function):
    print("closing the browser")

def testcas1():
    print("testcase1 is executed")
def testcas2():
    print("testcase2 is executed")
def testcas3():
    print("testcase3 is executed")