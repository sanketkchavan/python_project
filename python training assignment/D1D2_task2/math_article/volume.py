def volume_of_sphere(radius):
    volume = (4*3.14*radius**3)/3
    return volume


def volume_of_cylinder(radius, height):
    volume = 3.14*(radius**2)*height
    return volume


def volume_of_pyramid(base, height):
    volume = (base*base*height)/3
    return volume


def volume_of_cone(radius, height):
    volume = (3.14*(radius**2)*height)/3
    return volume


def volume_of_cuboid(length, height, width):
    volume = length*height*width
    return volume


def volume_of_hemisphere(radius):
    volume = (2*3.14*(radius**3))/3
    return volume
