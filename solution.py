def v(b, s, p):
    if (b == 3 and s == 2):
        return (4 * p) / (1 + 4 * p)
    else:
        E = expected_value(b, s + 1, p)
        return (p * (E - 4)) / (p * E + E - 4 * p - 1)


def expected_value(b, s, p):
    if b == 4:
        return 1
    elif s == 3:
        return 0
    elif (b == 3 and s == 2):
        return (4 * p) / (1 + 4 * p)
    else:
        ball = expected_value(b + 1, s, p)
        strike = expected_value(b, s + 1, p)
        v_prob = v(b, s, p)
        return (
            (v_prob ** 2) * ball
            + 2 * strike * v_prob * (1 - v_prob)
            + 4 * (1 - v_prob) ** 2 * p
            + strike * (1 - v_prob) ** 2 * (1 - p)
        )


def probability_ball(b, s, p):
    v_prob = v(b, s, p)
    return v_prob ** 2


def probability_strike(b, s, p):
    v_prob = v(b, s, p)
    swing_throw = v_prob * (1 - v_prob)
    wait_strike = v_prob * (1 - v_prob)
    strike_swing = (1 - v_prob) ** 2 * (1 - p)
    return swing_throw + wait_strike + strike_swing


def probability_reaching(b, s, p):
    if b < 0 or s < 0:
        return 0
    if (b, s) == (0, 0):
        return 1
    from_ball = probability_reaching(b - 1, s, p) * probability_ball(b - 1, s, p)
    from_strike = probability_reaching(b, s - 1, p) * probability_strike(b, s - 1, p)
    return from_ball + from_strike


q = probability_reaching(3, 2, 0.7)
eps = 10**-5
p = 0
while 0 <= p <= 1:
    print(probability_reaching(3, 2, p))
    p += eps
print(q)

