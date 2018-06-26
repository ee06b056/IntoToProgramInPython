def isIn(xstr, ystr):
    return xstr in ystr if (len(xstr) < len(ystr)) else ystr in xstr
print (isIn('libo','lil'))
