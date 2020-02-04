

def fn1(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
fn1('Hi', '2nd', '3rd')


def fn2(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
fn2(name='Peter', age=10)   