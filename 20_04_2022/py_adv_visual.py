
import seaborn as sns;

datasets=sns.get_dataset_names();

print(datasets);

flowerset=sns.load_dataset("iris");

print(flowerset);

scatter=sns.scatterplot(x="petal_length",y="petal_width",data=flowerset,hue="species");

print(scatter);

"""

skew represetnts on a value of -1 to 1 
whtether the data trend skews left (positive 1)
or right (negative -1)


"""