import pandas as pd




#Clean Data function
def get_clean_data():
  
    data=pd.read_csv("../data/data.csv")
    data = data.drop(['Unnamed: 32','id'],axis=1)
    #map values in daignosis to 1 and 0 , Malicious to 1 and other to 0
    data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
    return data






def main():
    data=get_clean_data()
    
    model=create_model(data)


if __name__ == '__main__':
    main()  