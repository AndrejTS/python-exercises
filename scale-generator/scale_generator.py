class Scale:
    CHROMATIC_SCALE = [
    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    ]
    FLAT_CHROMATIC_SCALE = [
    "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"
    ]
    FLAT_KEYS = [
    'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb'
    ]

    def __init__(self, tonic):
        if tonic in self.FLAT_KEYS:
            self.scale = self.FLAT_CHROMATIC_SCALE
        else:
            self.scale = self.CHROMATIC_SCALE
        self.tonic = tonic.capitalize()

    def chromatic(self):
        return self.scale

    def interval(self, intervals):
        index = self.scale.index(self.tonic)
        scale = self.scale[index:] + self.scale[:index] 
        result = [self.tonic]
        actual = 0
        for i in intervals[:-1]:
            if i == 'm':
                result.append(scale[actual+1])
                actual += 1
            elif i == 'M':
                result.append(scale[actual+2])
                actual += 2
            elif i == 'A':
                result.append(scale[actual+3])
                actual += 3
        return result
