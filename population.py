import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("data.csv")

datalist = df["readingscore"].tolist()


mean = sum(datalist)/len(datalist)
std_dev = statistics.stdev(datalist)
median = statistics.median(datalist)
mode = statistics.mode(datalist)

print(mean)
print(mode)
print(std_dev)
print(median)

firstStandardDeviationStart,firstStandardDeviationEnd = mean-std_dev,mean+std_dev
secondStandardDeviationStart,secondStandardDeviationEnd = mean-(2*std_dev),mean+(2*std_dev)
thirdStandardDeviationStart,thirdStandardDeviationEnd = mean-(3*std_dev),mean+(3*std_dev)

fig = ff.create_distplot([datalist],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[firstStandardDeviationStart,firstStandardDeviationStart],y=[0,0.17],mode="lines",name="FirstStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[firstStandardDeviationEnd,firstStandardDeviationEnd],y=[0,0.17],mode="lines",name="FirstStandardDeviationEnd"))

fig.add_trace(go.Scatter(x=[secondStandardDeviationStart,secondStandardDeviationStart],y=[0,0.17],mode="lines",name="SecondStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[secondStandardDeviationEnd,secondStandardDeviationEnd],y=[0,0.17],mode="lines",name="secondStandardDeviationEnd"))

fig.add_trace(go.Scatter(x=[thirdStandardDeviationStart,thirdStandardDeviationStart],y=[0,0.17],mode="lines",name="thirdStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[thirdStandardDeviationEnd,thirdStandardDeviationEnd],y=[0,0.17],mode="lines",name="ThirdStandardDeviationEnd"))


listofDatain1stSD = [result for result in datalist if result>firstStandardDeviationStart and result<firstStandardDeviationEnd]
listofDatain2ndSD = [result for result in datalist if result>secondStandardDeviationStart and result<secondStandardDeviationEnd]
listofDatain3rdSD = [result for result in datalist if result>thirdStandardDeviationStart and result<thirdStandardDeviationEnd]

print("% of data in the first StandardDeviation",len(listofDatain1stSD)/len(datalist)*100)
print("% of data in the second StandardDeviation",len(listofDatain2ndSD)/len(datalist)*100)
print("% of data in the third StandardDeviation",len(listofDatain3rdSD)/len(datalist)*100)



fig.show()

