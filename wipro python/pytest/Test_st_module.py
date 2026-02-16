# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection

def setup_module(module):
    print("open the db connection")
def teardown_module(module):
    print("clossing the db connection")
def test_read():
    print("reading the db")
def test_write():
    print("writing the db")
def test_update():
    print("Updating the db")