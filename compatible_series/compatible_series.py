

def scan (data_y , dataset_x , dataset_y , margin=5, wrong_points_percentage=25):

        if len(dataset_x) != len(dataset_y):
            print('dataset_x is not the same size as dataset_y, they must have the same length!')
            return [],[]

        max_wrong_points = round((wrong_points_percentage/100)*len(data_y))

        compatible_series_x = [] # X values for the series found (result or return)
        compatible_series_y = [] # Y values for the series found (result or return)

        # Scan the database in order to search for compatible points with the given data

        values_x = []
        
        for i in range (len(dataset_x) - len(data_y) + 1):

            right_points = 0
            wrong_points = 0

            for j in range (len(data_y)):
                    
                if dataset_y[i + j] < data_y[j]*(1 + margin/100) and dataset_y[i + j] > data_y[j]*(1 - margin/100):

                    right_points += 1
                    
                else:
                    
                    wrong_points += 1

                if right_points >= len(data_y) - max_wrong_points:
                            
                    for k in range (i, i + len(data_y)):

                        if dataset_x[k] not in values_x: # Check for repeated X values
                           
                            values_x.append(dataset_x[k])
                            
                    break


        # Format and generate the Y data based on values_x
        values_x.sort()

        values_y = []
        # Generates the Y values
        for i in range (len(values_x)):

            values_y.append(dataset_y[dataset_x.index(values_x[i])])
    

        # Separates the values into small series
        for i in range (0, len(values_x), len(data_y)):
            serie_x = values_x[i:(i+len(data_y))]
            serie_y = values_y[i:(i+len(data_y))]
            compatible_series_x.append(serie_x)
            compatible_series_y.append(serie_y)
            
        
        return compatible_series_x, compatible_series_y

