# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(5,5) == 10
        print("Add Function works fine")

if __name__ == '__main__':
        TestAdd()