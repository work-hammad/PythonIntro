#Raising Custom Error
"""Sometimes we by our intent want to raise an error(built in) or we can also raise a custom made error in our program at certain
line to avoid uncontrolled or unwanted behaviour in the execution of further code """
class MyCustomError(Exception):
    def __init__(self, message="This is a custom error."):
        self.message = message
        super().__init__(self.message)

# Using the custom error
try:
    raise MyCustomError("An error occurred!")
except MyCustomError as e:
    print(f"Caught an exception: {e}")
