from numpy import sqrt

def x_independent(x_1, y_1, x_2, y_2, x_3, y_3, r_1, r_2, r_3, sigma_x1, sigma_y1, sigma_x2, sigma_y2, sigma_x3, sigma_y3, sigma_r1, sigma_r2, sigma_r3):
    return 1/2*sqrt(sigma_y3**2*((r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2 + 2*(y_1 - y_2)*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + (y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(x_1 - x_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_y2**2*((r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2 + 2*y_1*y_2 - 2*y_2*y_3 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + (y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(x_1 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_y1**2*((r_2**2 - r_3**2 - x_2**2 + x_3**2 + 2*y_1*y_2 - y_2**2 - 2*y_1*y_3 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + (y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(x_2 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_x2**2*(2*(x_2*y_1 - x_2*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - (y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(y_1 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_x3**2*(2*(x_3*y_1 - x_3*y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - (y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(y_1 - y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_x1**2*(2*(x_1*y_2 - x_1*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - (y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(y_2 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + 4*(r_1*y_2 - r_1*y_3)**2*sigma_r1**2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2 + 4*(r_2*y_1 - r_2*y_3)**2*sigma_r2**2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2 + 4*(r_3*y_1 - r_3*y_2)**2*sigma_r3**2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)

def y_independent(x_1, y_1, x_2, y_2, x_3, y_3, r_1, r_2, r_3, sigma_x1, sigma_y1, sigma_x2, sigma_y2, sigma_x3, sigma_y3, sigma_r1, sigma_r2, sigma_r3):
    return 1/2*sqrt(sigma_y1**2*(2*(x_2 - x_3)*y_1/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + (x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(x_2 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_y2**2*(2*(x_1 - x_3)*y_2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + (x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(x_1 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_y3**2*(2*(x_1 - x_2)*y_3/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + (x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(x_1 - x_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_x3**2*((r_1**2 - r_2**2 - x_1**2 + x_2**2 + 2*(x_1 - x_2)*x_3 - y_1**2 + y_2**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - (x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(y_1 - y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_x2**2*((r_1**2 - r_3**2 - x_1**2 + 2*x_1*x_2 - 2*x_2*x_3 + x_3**2 - y_1**2 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - (x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(y_1 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + sigma_x1**2*((r_2**2 - r_3**2 + 2*x_1*x_2 - x_2**2 - 2*x_1*x_3 + x_3**2 - y_2**2 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - (x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(y_2 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)**2 + 4*(r_1*x_2 - r_1*x_3)**2*sigma_r1**2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2 + 4*(r_2*x_1 - r_2*x_3)**2*sigma_r2**2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2 + 4*(r_3*x_1 - r_3*x_2)**2*sigma_r3**2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)

def x_upper(x_1, y_1, x_2, y_2, x_3, y_3, r_1, r_2, r_3, sigma_x1, sigma_y1, sigma_x2, sigma_y2, sigma_x3, sigma_y3, sigma_r1, sigma_r2, sigma_r3):
    return sigma_y3*abs(-1/2*(r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2 + 2*(y_1 - y_2)*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - 1/2*(y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(x_1 - x_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_y2*abs(1/2*(r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2 + 2*y_1*y_2 - 2*y_2*y_3 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + 1/2*(y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(x_1 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_y1*abs(-1/2*(r_2**2 - r_3**2 - x_2**2 + x_3**2 + 2*y_1*y_2 - y_2**2 - 2*y_1*y_3 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - 1/2*(y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(x_2 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_r2*abs((r_2*y_1 - r_2*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)) + sigma_r3*abs((r_3*y_1 - r_3*y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)) + sigma_x2*abs((x_2*y_1 - x_2*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - 1/2*(y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(y_1 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_x3*abs(-(x_3*y_1 - x_3*y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + 1/2*(y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(y_1 - y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_r1*abs((r_1*y_2 - r_1*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)) + sigma_x1*abs(-(x_1*y_2 - x_1*y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + 1/2*(y_1*y_2**2 - (y_1 - y_2)*y_3**2 - (r_2**2 - r_3**2 - x_2**2 + x_3**2)*y_1 + (r_1**2 - r_3**2 - x_1**2 + x_3**2 - y_1**2)*y_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2 - y_1**2 + y_2**2)*y_3)*(y_2 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2)

def y_upper(x_1, y_1, x_2, y_2, x_3, y_3, r_1, r_2, r_3, sigma_x1, sigma_y1, sigma_x2, sigma_y2, sigma_x3, sigma_y3, sigma_r1, sigma_r2, sigma_r3):
    return sigma_y1*abs((x_2 - x_3)*y_1/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + 1/2*(x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(x_2 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_y2*abs(-(x_1 - x_3)*y_2/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - 1/2*(x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(x_1 - x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_y3*abs((x_1 - x_2)*y_3/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + 1/2*(x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(x_1 - x_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_x3*abs(1/2*(r_1**2 - r_2**2 - x_1**2 + x_2**2 + 2*(x_1 - x_2)*x_3 - y_1**2 + y_2**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - 1/2*(x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(y_1 - y_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_x2*abs(-1/2*(r_1**2 - r_3**2 - x_1**2 + 2*x_1*x_2 - 2*x_2*x_3 + x_3**2 - y_1**2 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) + 1/2*(x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(y_1 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_x1*abs(1/2*(r_2**2 - r_3**2 + 2*x_1*x_2 - x_2**2 - 2*x_1*x_3 + x_3**2 - y_2**2 + y_3**2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3) - 1/2*(x_1*x_2**2 - (x_1 - x_2)*x_3**2 - (x_2 - x_3)*y_1**2 + (x_1 - x_3)*y_2**2 - (x_1 - x_2)*y_3**2 - (r_2**2 - r_3**2)*x_1 + (r_1**2 - r_3**2 - x_1**2)*x_2 - (r_1**2 - r_2**2 - x_1**2 + x_2**2)*x_3)*(y_2 - y_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)**2) + sigma_r2*abs((r_2*x_1 - r_2*x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)) + sigma_r3*abs((r_3*x_1 - r_3*x_2)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3)) + sigma_r1*abs((r_1*x_2 - r_1*x_3)/((x_2 - x_3)*y_1 - (x_1 - x_3)*y_2 + (x_1 - x_2)*y_3))
    
    
# Forgive me lord, for I have sinned. 
# Early draft, will fix soon 
def trilateration_error(pods_in_range, pods_in_range_error, range_of_pods_in_range, error_of_range_of_pods_in_range):
    x_independent_error = x_independent(
        pods_in_range[0][0], # x_1
        pods_in_range[0][1], # y_1
        pods_in_range[1][0], # x_2
        pods_in_range[1][1], # y_2
        pods_in_range[2][0], # x_3
        pods_in_range[2][1], # y_3
        range_of_pods_in_range[0], #r_1
        range_of_pods_in_range[1], #r_2
        range_of_pods_in_range[2], #r_3
        pods_in_range_error[0][0], # sigma_x1
        pods_in_range_error[0][1], # sigma_y1
        pods_in_range_error[1][0], # sigma_x2
        pods_in_range_error[1][1], # sigma_y2
        pods_in_range_error[2][0], # sigma_x3
        pods_in_range_error[2][1], # sigma_y3
        error_of_range_of_pods_in_range[0], #sigma_r1
        error_of_range_of_pods_in_range[1], #sigma_r2
        error_of_range_of_pods_in_range[2], #sigma_r3
        )
        
    y_independent_error = y_independent(
        pods_in_range[0][0], # x_1
        pods_in_range[0][1], # y_1
        pods_in_range[1][0], # x_2
        pods_in_range[1][1], # y_2
        pods_in_range[2][0], # x_3
        pods_in_range[2][1], # y_3
        range_of_pods_in_range[0], #r_1
        range_of_pods_in_range[1], #r_2
        range_of_pods_in_range[2], #r_3
        pods_in_range_error[0][0], # sigma_x1
        pods_in_range_error[0][1], # sigma_y1
        pods_in_range_error[1][0], # sigma_x2
        pods_in_range_error[1][1], # sigma_y2
        pods_in_range_error[2][0], # sigma_x3
        pods_in_range_error[2][1], # sigma_y3
        error_of_range_of_pods_in_range[0], #sigma_r1
        error_of_range_of_pods_in_range[1], #sigma_r2
        error_of_range_of_pods_in_range[2], #sigma_r3
        )
        
    x_upper_error = x_upper(
        pods_in_range[0][0], # x_1
        pods_in_range[0][1], # y_1
        pods_in_range[1][0], # x_2
        pods_in_range[1][1], # y_2
        pods_in_range[2][0], # x_3
        pods_in_range[2][1], # y_3
        range_of_pods_in_range[0], #r_1
        range_of_pods_in_range[1], #r_2
        range_of_pods_in_range[2], #r_3
        pods_in_range_error[0][0], # sigma_x1
        pods_in_range_error[0][1], # sigma_y1
        pods_in_range_error[1][0], # sigma_x2
        pods_in_range_error[1][1], # sigma_y2
        pods_in_range_error[2][0], # sigma_x3
        pods_in_range_error[2][1], # sigma_y3
        error_of_range_of_pods_in_range[0], #sigma_r1
        error_of_range_of_pods_in_range[1], #sigma_r2
        error_of_range_of_pods_in_range[2], #sigma_r3
        )
        
    y_upper_error = y_upper(
        pods_in_range[0][0], # x_1
        pods_in_range[0][1], # y_1
        pods_in_range[1][0], # x_2
        pods_in_range[1][1], # y_2
        pods_in_range[2][0], # x_3
        pods_in_range[2][1], # y_3
        range_of_pods_in_range[0], #r_1
        range_of_pods_in_range[1], #r_2
        range_of_pods_in_range[2], #r_3
        pods_in_range_error[0][0], # sigma_x1
        pods_in_range_error[0][1], # sigma_y1
        pods_in_range_error[1][0], # sigma_x2
        pods_in_range_error[1][1], # sigma_y2
        pods_in_range_error[2][0], # sigma_x3
        pods_in_range_error[2][1], # sigma_y3
        error_of_range_of_pods_in_range[0], #sigma_r1
        error_of_range_of_pods_in_range[1], #sigma_r2
        error_of_range_of_pods_in_range[2], #sigma_r3
        )
    return x_independent_error, y_independent_error, x_upper_error, y_upper_error

