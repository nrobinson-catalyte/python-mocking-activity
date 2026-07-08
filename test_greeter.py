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
#2. Open test_greeter.py and examine 3 test functions.-DONE
#3. Create a mock test for test_greet_morning that follows three rules.-DONE
    #Create a Greeter instance.
    #Use mocker.patch.object to mock both helper methods.
    #Call greet() and assert the result.
def test_greet_morning(mocker):
    greeter = Greeter()

    mocker.patch.object(greeter, "get_current_hour", return_value=9)
    mocker.patch.object(greeter, "get_username", return_value="Alice")

    result = greeter.greet(1)

    assert result == "Good morning, Alice!"
#4. Create a mock test for test_greet_afternoon that follows three rules.-DONE
     #Create a Greeter instance.
    #Use mocker.patch.object to mock both helper methods.
    #Call greet() and assert the result.  
def test_greet_afternoon(mocker):
    greeter = Greeter()

    mocker.patch.object(greeter, "get_current_hour", return_value=14)
    mocker.patch.object(greeter, "get_username", return_value="Bob")

    result = greeter.greet(2)

    assert result == "Good afternoon, Bob!" 
#4. Create a mock test for test_greet_evening_unknown_use that follows three rules.-DONE
    #Create a Greeter instance.
    #Use mocker.patch.object to mock both helper methods.
    #Call greet() and assert the result.
def test_greet_evening_unknown_user(mocker):
    greeter = Greeter()

    mocker.patch.object(greeter, "get_current_hour", return_value=21)
    mocker.patch.object(greeter, "get_username", return_value="Guest")

    result = greeter.greet(99)

    assert result == "Good evening, Guest!"
#5 Confirm that all three test pass & -v flag prints each test name.-Done
#6 Create a fourth Add a fourth test that checks the boundary at hour 5 — the exact point where "evening" ends and "morning" begins.-DONE
def test_greet_boundary_hour_five(mocker):
    greeter = Greeter()

    mocker.patch.object(greeter, "get_current_hour", return_value=5)
    mocker.patch.object(greeter, "get_username", return_value="Alice")

    result = greeter.greet(1)

    assert result == "Good morning, Alice!"