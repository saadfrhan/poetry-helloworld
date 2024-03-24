from poetry_helloworld import main

# Check if it returns "Hello, World!"
def test_myFunction():
  result: str = main.myFunction()
  assert result == "Hello, World!"
  
# Check if it doesn't returns "Hello, Sun!"
def test_myFunction2():
  result: str = main.myFunction()
  assert result != "Hello, Sun!"  
