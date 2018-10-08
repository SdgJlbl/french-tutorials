def calculer_distances(dataset, eval_point):
    distances = []
    for train_point in dataset:
        distances.append({'label': train_point['label'], 
                          'distance': distance(eval_point, train_point['variables']) 
                         })
    return distances
