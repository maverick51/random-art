import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr_list = []
    expr1 = lambda x, y: 3.14 * math.sin(3.14) * x**10 * y**20 + y + x * math.cos(x/2) * \
            math.sin(3.14 / 2) + x**3 + y**3 * random.random() * math.tan(x) + math.tan(y) * \
            (math.sin(math.cos(x)) / math.cos(math.sin(y)))**20 * math.sin(random.uniform(-1, 1))
    expr2 = lambda x, y: 3.14 * math.sin(3.14) * x**10 * y**20 + y + x * math.cos(x/2) * \
            math.sin(3.14 / 2) + x**3 + y**3 * random.random() * math.tan(x) + \
            math.tan(y**2) * (math.sin(math.cos(x**3)) / math.cos(math.sin(y)))**20 * \
            math.sin(random.uniform(-1, 1))
    expr3 = lambda x, y: math.sin(math.cos(x) + math.sin(y) + x**2 * y**3)
    expr4 = lambda x, y: math.tan((x + y) * x**3 * y**4 + math.sin(y**2) + math.cos(x**2))
    expr5 = lambda x, y: math.cos(math.cos(y) * math.tan(x) * math.sin(x))

    expr_list.append(expr1)
    expr_list.append(expr2)
    expr_list.append(expr3)
    expr_list.append(expr4)
    expr_list.append(expr5)

    expr = random.choice(expr_list)
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)

    # KEEPERS
    # expr = lambda x, y: 3.14 * math.sin(3.14) * x**10 * y**20 + y + x * math.cos(x/2) * math.sin(3.14 / 2) + x**3 + y**3\
    #* random.random() * math.tan(x) + math.tan(y) * (math.sin(math.cos(x)) / math.cos(math.sin(y)))**20 * math.sin(random.uniform(-1,1))
