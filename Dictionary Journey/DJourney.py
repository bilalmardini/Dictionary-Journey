def merging_dictionary (dic1, dic2):
    dic3 = {**dic1, **dic2}
    print(dic3)
dict1 = {"a":1, "b":2, "c":3}
dict2 = {"b":10,"d":4}
merging_dictionary(dict1,dict2)


sentence = input("enter a sentence and repeat some words: ")
sentenceSplit = sentence.split()
uniqueWords = set(sentenceSplit)

for word in uniqueWords:
    counter = sentenceSplit.count(word)
    print(word+": "+str(counter)+" ") 


companyEngineering = {
    "engineering ":{
        "alice":{"age":30, "role":"software engineer"},
        "bob":{"age":28, "role":"devOps engineer"}
    },
    "HR":{
        "charlie":{"age":35, "role":"HR manager"}
    }
}
print(companyEngineering)
companyEngineering["engineering "]["david"] = {"age":27,"role":"data science"} 

def totalEmp (companyEngineer):
    count = 0
    for department in companyEngineer.values():
        count += len(department)
    return count

print("the total number of employees is: "+str(totalEmp(companyEngineering)))