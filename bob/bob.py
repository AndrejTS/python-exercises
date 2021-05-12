def response(hey_bob):
    hey_bob = hey_bob.split()
    hey_bob = ''.join(hey_bob)
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"  
        else:     
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
        
    return "Whatever."
