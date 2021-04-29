def to_str(n, base):
    conStr = '0123456789ABCDEF'
    if n < base:
        return conStr[n]
    else:
        return to_str(n//base, base) + conStr[n % base]
