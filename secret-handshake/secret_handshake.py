def commands(number):
    events = {
        1: 'wink', 
        2: 'double blink', 
        4: 'close your eyes', 
        8: 'jump'
    }
    result = []
    for i in events.keys():
        if number & i != 0:
            result.append(events[i])
    if number & 16 != 0:
        return result[::-1]
    return result

