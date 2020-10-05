def greet(*names):
    """This function greets all
   the person in the names tuple."""

    print(type(names))
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")
