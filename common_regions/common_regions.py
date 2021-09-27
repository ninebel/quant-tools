
def average (data):

    summ = 0

    for i in range (len(data)):

        summ += data[i]

    return summ/len(data)

def scan (data, margin=5, minPointsPercentage=5):

    regions = []

    minPoints = round(len(data)*(minPointsPercentage/100))
    

    for i in range (0, len(data), 1):

        validPoints = []

        for j in range (0, len(data), 1):

            if data[j] <= (1 + margin/100)*data[i] and data[j] >= (1 - margin/100)*data[i]:

                validPoints.append(data[j])
                
        if len(validPoints) >= minPoints and len(validPoints) > 0:

            avg = average(validPoints)

            canInsert = True

            for j in range (0, len(regions), 1):

                if avg <= (1 + margin/100)*regions[j] and avg >= (1 - margin/100)*regions[j]:

                    canInsert = False
                    break

            if canInsert == True:
            
                regions.append(average(validPoints))


    return regions
