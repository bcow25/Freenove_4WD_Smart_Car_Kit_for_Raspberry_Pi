import numpy
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_big_matrix():
    bigmatrix=numpy.loadtxt(os.path.join(__location__, 'big_matrix.csv'))

    return bigmatrix

def read_small_matrix():
    smallmatrix=numpy.loadtxt(os.path.join(__location__, 'small_matrix.csv'))

    return smallmatrix