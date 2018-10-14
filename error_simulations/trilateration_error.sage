import ConfigParser

def trilateration_eqn_npods(n):
    if n < 3:
        return "You can't TRIlaterate with less than 3, dummy"
    
    x, y = var('x', 'y')
    
    x_loc = list(var('x_{}'.format(i)) for i in range(1, n + 1))
    y_loc = list(var('y_{}'.format(i)) for i in range(1, n + 1))
    r = list(var('r_{}'.format(i)) for i in range(1, n + 1))
    
    # https://math.stackexchange.com/questions/884807/find-x-location-using-3-known-x-y-location-using-trilateration
    if n == 3:
        distance_equations = []
    
        for i in range(1, n):
            distance_equations.append(-2 * x * (x_loc[i - 1] - x_loc[i]) \
                                      -2 * y * (y_loc[i - 1] - y_loc[i]) == \
                                      r[i - 1] ** 2 - r[i] ** 2\
                                      - x_loc[i - 1] ** 2 + x_loc[i] ** 2 \
                                      - y_loc[i - 1]** 2 + y_loc[i] ** 2)

        res = solve(distance_equations, x, y)
        x_func = res[0][0].right()
        y_func = res[0][1].right()
        
        return x_func.simplify_full(), y_func.simplify_full()
        
    if n > 3:
        A = matrix(SR, n - 1, 2)
        b = matrix(SR, n - 1, 1)
        
        for i in range(1, n):
            A[i-1] = (-2 * (x_loc[i - 1] - x_loc[i]), - 2 * (y_loc[i - 1] - y_loc[i]))
            b[i-1] = r[i - 1] ** 2 - r[i] ** 2 - x_loc[i - 1]** 2 \
                     + x_loc[i] ** 2 - y_loc[i - 1]** 2 + y_loc[i] ** 2
        
        x_hat = (A.T * A).inverse() * A.T * b
        
        return x_hat[0].simplify_full(), x_hat[1].simplify_full()
        
# Equation from Taylor Error Analysis
def error_function_worst(expr, n):
    x_loc = list(var('x_{}'.format(i)) for i in range(1, n + 1))
    y_loc = list(var('y_{}'.format(i)) for i in range(1, n + 1))
    r = list(var('r_{}'.format(i)) for i in range(1, n + 1))
    
    sigma_x = list(var('sigma_x{}'.format(i)) for i in range(1, n + 1))
    sigma_y = list(var('sigma_y{}'.format(i)) for i in range(1, n + 1))
    sigma_r = list(var('sigma_r{}'.format(i)) for i in range(1, n + 1))

    error_expr = 0
    
    for x_index in range(n):
        error_expr += abs(diff(expr, x_loc[x_index])) * sigma_x[x_index]
        
    for y_index in range(n):
        error_expr += abs(diff(expr, y_loc[y_index])) * sigma_y[y_index]

    for r_index in range(n):
        error_expr += abs(diff(expr, r[r_index])) * sigma_r[r_index]

    return error_expr

# Equation from Taylor Error Analysis
def error_function_independent(expr, n):
    x_loc = list(var('x_{}'.format(i)) for i in range(1, n + 1))
    y_loc = list(var('y_{}'.format(i)) for i in range(1, n + 1))
    r = list(var('r_{}'.format(i)) for i in range(1, n + 1))
    
    sigma_x = list(var('sigma_x{}'.format(i)) for i in range(1, n + 1))
    sigma_y = list(var('sigma_y{}'.format(i)) for i in range(1, n + 1))
    sigma_r = list(var('sigma_r{}'.format(i)) for i in range(1, n + 1))

    error_expr = 0
    
    # Doing exp in this way b/c of weird error
    # I _think_ it's b/c n>3 returns vector
    for x_index in range(n):
        tmp_expr = diff(expr, x_loc[x_index]) * sigma_x[x_index]
        try:
            error_expr += pow(tmp_expr[0], 2)
        except:
            error_expr += pow(tmp_expr, 2)
        
    for y_index in range(n):
        tmp_expr = diff(expr, y_loc[y_index]) * sigma_y[y_index]
        try:
            error_expr += pow(tmp_expr[0], 2)
        except:
            error_expr += pow(tmp_expr, 2)

    for r_index in range(n):
        tmp_expr = diff(expr, r[r_index]) * sigma_r[r_index]
        try:
            error_expr += pow(tmp_expr[0], 2)
        except:
            error_expr += pow(tmp_expr, 2)

    return error_expr ** (1/2)
    
def evaluate_error(expr, n, pod_locations, pods_error, ranges, range_errors):
    error_expr = expr

    x_loc = list(var('x_{}'.format(i)) for i in range(1, n + 1))
    y_loc = list(var('y_{}'.format(i)) for i in range(1, n + 1))
    r = list(var('r_{}'.format(i)) for i in range(1, n + 1))
    
    sigma_x = list(var('sigma_x{}'.format(i)) for i in range(1, n + 1))
    sigma_y = list(var('sigma_y{}'.format(i)) for i in range(1, n + 1))
    sigma_r = list(var('sigma_r{}'.format(i)) for i in range(1, n + 1))
    
    for index in range(n):
        error_expr = error_expr.subs(x_loc[index] == pod_locations[index][0])
        error_expr = error_expr.subs(y_loc[index] == pod_locations[index][1])
        
        error_expr = error_expr.subs(sigma_x[index] == pods_error[index][0])
        error_expr = error_expr.subs(sigma_y[index] == pods_error[index][1])
        
        error_expr = error_expr.subs(r[index] == ranges[index])
        error_expr = error_expr.subs(sigma_r[index] == range_errors[index])

    return error_expr

# Writes all the error functions and partials to a config instead of regening every time
# Shouldn't need to be rerun very often
def write_config():
    trilat_config = ConfigParser.RawConfigParser()
    
    for n in range(3, 11):
        config_section_name = 'TRILAT{}'.format(n)
        trilat_config.add_section(config_section_name)
    
        x_func, y_func = trilateration_eqn_npods(n)
        # x, y independent error functions 
        trilat_config.set(config_section_name, 'X_INDEPENDENT', error_function_independent(x_func, n))
        trilat_config.set(config_section_name, 'Y_INDEPENDENT', error_function_independent(y_func, n))
        
        # x, y upper bounds error functions
        trilat_config.set(config_section_name, 'X_UPPER', error_function_worst(x_func, n))
        trilat_config.set(config_section_name, 'Y_UPPER', error_function_worst(y_func, n))
    
    with open('trilateration.cfg', 'w+') as f:
        trilat_config.write(f)
        
def load_functions_from_config(n):
    config_section_name = 'TRILAT{}'.format(n)

    trilat_config = ConfigParser.RawConfigParser()
    trilat_config.read('trilateration.cfg')
    
    x_loc = list(var('x_{}'.format(i)) for i in range(1, n + 1))
    y_loc = list(var('y_{}'.format(i)) for i in range(1, n + 1))
    r = list(var('r_{}'.format(i)) for i in range(1, n + 1))
        
    sigma_x = list(var('sigma_x{}'.format(i)) for i in range(1, n + 1))
    sigma_y = list(var('sigma_y{}'.format(i)) for i in range(1, n + 1))
    sigma_r = list(var('sigma_r{}'.format(i)) for i in range(1, n + 1))
    
    var_dict = {}
    for val in x_loc + y_loc + r + sigma_x + sigma_y + sigma_r:
        var_dict[str(val)] = val
        
    def retrieve_section(section_name):
        section = trilat_config.get(config_section_name, section_name)
        return sage_eval(section, locals=var_dict)
    
    x_independent = retrieve_section('X_INDEPENDENT')
    y_independent = retrieve_section('Y_INDEPENDENT')
    
    x_upper = retrieve_section('X_UPPER')
    y_upper = retrieve_section('Y_UPPER')
    
    return x_independent, y_independent, x_upper, y_upper
    
n = 3

x_func, y_func = trilateration_eqn_npods(n)

x_loc = list(var('x_{}'.format(i)) for i in range(1, n + 1))
y_loc = list(var('y_{}'.format(i)) for i in range(1, n + 1))
r = list(var('r_{}'.format(i)) for i in range(1, n + 1))

sigma_x = list(var('sigma_x{}'.format(i)) for i in range(1, n + 1))
sigma_y = list(var('sigma_y{}'.format(i)) for i in range(1, n + 1))
sigma_r = list(var('sigma_r{}'.format(i)) for i in range(1, n + 1))

print(latex(x_func))

for x_index in range(n):
    expr = (diff(x_func, x_loc[x_index]) * sigma_x[x_index]) ** 2
    print(latex(x_loc[x_index]) + '=' + latex(expr))

#from ast import literal_eval as eval
#with open('trilateration.parameters', 'r') as f:
#    lines = f.read()
#    lines = lines.split('\n\n')
    
#    pod_locations = eval(lines[0])
#    pods_error = eval(lines[1])
#    ranges = eval(lines[2])
#    range_errors = eval(lines[3]) 

#n = len(pod_locations)

# Rerun this if something changes with the trilateration/error funcs
# write_config()

#x_error_independent, y_error_independent, x_error_worst, y_error_worst = load_functions_from_config(n)

#x_error_independent = evaluate_error(x_error_independent, n, pod_locations, pods_error, ranges, range_errors)
#y_error_independent = evaluate_error(y_error_independent, n, pod_locations, pods_error, ranges, range_errors)

#x_error_worst = evaluate_error(x_error_worst, n, pod_locations, pods_error, ranges, range_errors)
#y_error_worst = evaluate_error(y_error_worst, n, pod_locations, pods_error, ranges, range_errors)

#print([x_error_worst, y_error_worst], [x_error_independent, y_error_independent])

