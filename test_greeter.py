from greeter import Greeter


# Test that greet() returns "Good morning, Alice!"
# when the hour is 9 and the user_id is 1 (Alice).
def test_greet_morning(mocker):
    pass


# Test that greet() returns "Good afternoon, Bob!"
# when the hour is 14 and the user_id is 2 (Bob).
def test_greet_afternoon(mocker):
    pass


# Test that greet() returns "Good evening, Guest!"
# when the hour is 21 and the user_id is 99 (unknown user).
def test_greet_evening_unknown_user(mocker):
    pass


# Stretch goal
# Add a test that checks greet() still works correctly at
# exactly hour=5 (the boundary between "evening" and "morning").
# What does the greeting say? Is that the right behaviour?

#Requirements#
#1. Complete Set Up follow 4 steps listed. -DONE
#2. Open test_greeter.py and examine 3 test functions.
#3. Create a mock test for test_greet_morning that follows three rules.
    #Create a Greeter instance.
    #Use mocker.patch.object to mock both helper methods.
    #Call greet() and assert the result.
#4. Create a mock test for test_greet_afternoon that follows three rules.
     #Create a Greeter instance.
    #Use mocker.patch.object to mock both helper methods.
    #Call greet() and assert the result.   
#4. Create a mock test for test_greet_evening_unknown_use that follows three rules.
    #Create a Greeter instance.
    #Use mocker.patch.object to mock both helper methods.
    #Call greet() and assert the result.
#5 Confirm that all three test pass & -v glag prints each test name.
#6 Create a fourth Add a fourth test that checks the boundary at hour 5 — the exact point where "evening" ends and "morning" begins.