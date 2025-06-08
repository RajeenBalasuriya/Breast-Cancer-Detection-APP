import pandas as pd

#Clean Data function
def get_clean_data():
  
    data=pd.read_csv("../data/data.csv")
    print(data.head())
    return data
   

def main():
    data=get_clean_data()


if __name__ == '__main__':
    main()  