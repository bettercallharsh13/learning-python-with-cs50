
results = ["harsh", "amit", "krishna"]


results.append("aman sir")
results.append("arpit sir")


results.insert(0, "arpit sir" )

results.insert(1, "aman sir" )
for i in range(len(results)):
    print(i + 1, results[i])
