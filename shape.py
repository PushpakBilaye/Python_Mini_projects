'''
2d shapes
1.square
perimeter of square=4*a            (where a=sides)
area of square= a*a

2.Triangle
perimeter of Triangle=a+b+c        (where a=side,b=base,c=side.)
area of Triangle=0.5*b*h           (where b=base,h=height.)

3.Rectangle
perimeter of rectangle=2(l+b)      (where l=length ,b=breadth.)
area of rectangle=l*b              (where l=length and b=breadth)

4.Circle
perimeter of circle=2*pi*r         (where r=radius.)
area of circle=pi*r*r              (where r= radius)

'''

import math

def psquare(a):
    posq= 4*a
    return posq

def asquare(a):
    aosq= a*a
    return aosq


def ptri(a,b,c):
    potri= a+b+c
    return potri

def atri(b,h):
    aotri= 0.5*b*h
    return aotri


def prect(l,b):
    porect= 2*l + 2*b
    return porect

def arect(l,b):
    aorect= l*b
    return aorect


def acircle(r):
    aocir= math.pi*r*r
    return aocir

def pcircle(r):
    pocir= 2*math.pi*r
    return pocir



'''
3d shapes:
cube
pcube= 12*a
acube= 6*a*a 

cuboid
pcuboid= 4*(l+b+h)
acuboid= 2*l*w + 2*l*h + 2*h*w (h=height,w=width,l=length)

sphere
asphere= 4*pi*r*r
psphere= 2*pi*r

cylinder
acylinder= 2*pi*r*h + 2*pi*r**2
pcylinder=4*r + 2*h

'''

def pcube(a):
    poc= 12*a
    return poc

def acube(a):
    aoc= 6*a*a
    return aoc


def pcuboid(l,b,h):
    pocu= 4*l + 4*b + 4*h
    return pocu

def acuboid(l,w,h):
    aocu= 2*l*w + 2*l*h + 2*h*w
    return aocu


def psphere(r):
    posph= 2*pi*r
    return posph

def asphere(r):
    aosph= 4*pi*r*r
    return aosph


def pcylinder(r,h):
    pocy= 4*r + 2*h
    return pocy

def acylinder(r,h):
    aocy= 2*pi*r*h + 2*pi*r**2
    return aocy













