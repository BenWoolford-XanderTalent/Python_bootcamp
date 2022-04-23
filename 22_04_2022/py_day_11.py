import seaborn as sns;
import sklearn;
import pandas as pd;

datasets=sns.get_dataset_names();

othername=pd.DataFrame(sns.load_dataset("iris"));
print(othername);
print("no?");
#othername.il



#split the iris dataframe in 2- one is data as input and the other is expected output
#uppercase should be inputs
#lowercase should be expected result
#X= iris.iloc([:,:-1]);#


















