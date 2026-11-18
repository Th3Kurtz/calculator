from calculator import add, subtract, multiply, divide

def test_add():
  assert add(2, 3) == 5

def test_divide():
  assert divide(6, 2) == 3

def test_subtract():
  assert subtract(5, 1) == 4

def test_multiply():
  assert multiply(6, 7) == 42

def test_multiply_zero():
  a, b = 0, 5 #arrange
  result = multiply(a, b) #act
  assert result  == 0 #assert

def test_divide_uneven():
  # a, b = 5, 2
  #result = divide(a, b)
  assert divide(5, 2) == 2.5

def test_add_negative():
  assert add(-5, -2) == -7

def test_circleArea():
  assert CircleArea(-4) == "Error"

