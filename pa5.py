def bisection_root(func, x1, x2):
    # Evaluate the function at the initial x-values
    f_x1 = func(x1)
    f_x2 = func(x2)

    # Check if the initial guesses already approximate a root
    if abs(f_x1) < 0.001:
        return x1
    elif abs(f_x2) < 0.001:
        return x2

    # Check if the initial guesses have the same sign
    if f_x1 * f_x2 > 0:
        raise ValueError("Initial guesses do not bracket a root")

    # Define a recursive function to perform bisection
    def bisection_recursive(x1, x2):
        # Calculate the midpoint
        x_mid = (x1 + x2) / 2
        f_mid = func(x_mid)

        # Check if the midpoint is close enough to zero
        if abs(f_mid) < 0.001:
            return x_mid

        # Update the interval based on the sign of the function value at the midpoint
        if f_mid * f_x1 < 0:
            return bisection_recursive(x1, x_mid)
        else:
            return bisection_recursive(x_mid, x2)

    # Start the recursion
    return bisection_recursive(x1, x2)
