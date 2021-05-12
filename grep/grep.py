def grep(pattern, flags, files):
    output = ''

    for f in files:
        with open(f) as file:
            data = file.read()

        if '-v' in flags:
            if '-l' in flags:
                if pattern not in data:
                    output += f + '\n'
            else:
                data = data.splitlines()
                if '-x' in flags:
                    for i in range(len(data)):
                        if '-i' in flags:
                            if pattern.lower() != data[i].lower():
                                if len(files) > 1:
                                    output += f + ':'
                                if '-n' in flags:
                                    output += str(i + 1) + ':'                                    
                                output += data[i] + '\n'
                        elif pattern != data[i]:
                            if len(files) > 1:
                                output += f + ':'
                            if '-n' in flags:
                                output += str(i + 1) + ':'                                
                            output += data[i] + '\n'
                else:
                    for i in range(len(data)):
                        if '-i' in flags:
                            if pattern.lower() not in data[i].lower():
                                if len(files) > 1:
                                    output += f + ':'
                                if '-n' in flags:
                                    output += str(i + 1) + ':'
                                output += data[i] + '\n'
                        elif pattern not in data[i]:
                            if len(files) > 1:
                                output += f + ':'
                            if '-n' in flags:
                                output += str(i + 1) + ':'
                            output += data[i] + '\n'
        else:
            if '-l' in flags:
                if pattern in data:
                    output += f + '\n'
            else:
                data = data.splitlines()
                if '-x' in flags:
                    for i in range(len(data)):
                        if '-i' in flags:
                            if pattern.lower() == data[i].lower():
                                if len(files) > 1:
                                    output += f + ':'
                                if '-n' in flags:
                                    output += str(i + 1) + ':'                                    
                                output += data[i] + '\n'
                        elif pattern == data[i]:
                            if len(files) > 1:
                                output += f + ':'
                            if '-n' in flags:
                                output += str(i + 1) + ':'                                
                            output += pattern + '\n'
                else:
                    for i in range(len(data)):
                        if '-i' in flags:
                            if pattern.lower() in data[i].lower():
                                if len(files) > 1:
                                    output += f + ':'
                                if '-n' in flags:
                                    output += str(i + 1) + ':'
                                output += data[i] + '\n'
                        elif pattern in data[i]:
                            if len(files) > 1:
                                output += f + ':'
                            if '-n' in flags:
                                output += str(i + 1) + ':'
                            output += data[i] + '\n'
    return output


#############