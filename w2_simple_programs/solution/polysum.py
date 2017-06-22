from math import tan, pi


def polysum(n, s):
    """
    A regular polygon has 'n' number of sides. Each side has length 's'.

    * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    * The perimeter of a polygon is: length of the boundary of the polygon

    :param n: the number of sides of the target regular polygon
    :param s: the length of each side of the target polygon.
    :return: the sum of the area and square of the perimeter of the regular polygon, rounded to 4 decimal places.
    """
    area = (0.25 * n * (s ** 2)) / tan(pi / n)
    perimeter = n * s
    the_sum = area + perimeter ** 2
    return round(the_sum, 4)