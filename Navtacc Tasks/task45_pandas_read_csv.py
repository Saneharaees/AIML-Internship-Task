import pandas as pd
# CSV file read karna (Data loading)
# Note: Is code ko chalane ke liye folder mein 'data.csv' hona chahiye
try:
    # Aap kisi bhi online CSV ka link bhi de sakti hain
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    print("CSV loaded successfully!")
    print(df.head()) # Pehli 5 rows dikhata hai
except Exception as e:
    print("Error reading CSV:", e)
