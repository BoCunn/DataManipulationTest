import pandas as pd

def export_features_to_csv(features, filename='features.csv'):
    for key in features:
        df = pd.DataFrame(features[key])
        df.to_csv(f'features/{key}.csv', index=False)