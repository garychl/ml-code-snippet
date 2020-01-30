try:
    test = 'abc'
    if test == 'abc':
        raise Exception
except FileNotFoundError:
    pass
except NameError as e:
    print('Name error')
except Exception as e:
    print('abc is not allowed.')
else:
    # run if try succeed
    print('Succeed.')
finally:
    # run it no matter succeed or failure
    # e.g. useful for closing resources
    print('Executing finally.')
    
    
