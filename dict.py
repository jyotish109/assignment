# d={}
# print(type(d))
# d1={'key' :"sudh" }
# print(d1)
# d3={123:"jyotish",'l_wer':"kumar",True:24234}
# print(d3)
# print(d3[123])
# print(d3[True])
# print(d3[1])
d4={"name":"jyotish","email":"jyotishkushwaha1008","name":"kushwaha"}
print(d4["name"])
d5={"compamy":"pwskills","courses":["web dev", "data science","java with dsa"]}
print(d5["courses"][2])
d6={"number":[1,2,3,4,5,6],"assignment":(1,2,3,4,45,6),"launch-date":(28,12,2023),"class-timing":{"web_dev":8,"data_master science":9,"java with dsa":10}}
 
print(d6)
print(d6["class-timing"]["data_master science"])
d6["mentor"]=["sudhanshu","krish","anurag"]


del d6["number"]
print(d6.keys())
print(d6.values())
print(d6.items())
d6.pop("assignment")



print(d6)
