import pandas as pd
filename = 'sample-log.txt'

def parse_log_line(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    df = pd.DataFrame(data, columns=['timestamp', 'IP address', 'status_code', 'endpoint'])
    df['status_code'] = df['status_code'].astype(int)
    row_tuple = df.itertuples
    return row_tuple
def get_unique_visitores(filename):
    df = parse_log_line(filename)
    n = len(pd.unique(df["IP_address"]))
    return n
def get_error_rate(filename):
    df = parse_log_line(filename)
    df["percentage"] = (df['status_code'] /
                        df['status_code'].sum()) * 100
    return df['percentage']

def get_popular_endpoints(filename):
    df = parse_log_line(filename)
    return df["endpoint"].count()




print("tuple:", parse_log_line(filename))
print("count",get_unique_visitores(filename))