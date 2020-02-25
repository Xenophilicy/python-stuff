symbolList = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
elementNames = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Florine","Neon","Sodium","Magnesium","Aluminum","Silicon","Phosphorus","Sulfer","Chlorine","Argon"]
electronConfigList = ["1s1","1s2","2s1","2s2","2p1","2p2","2p3","2p4","2p5","2p6","3s1","3s2","3p1","3p2","3p3","3p4","3p5","3p6","4s1","4s2","3d1","3d2","3d3","3d4","3d5","3d6","3d7","3d8","3d9","3d10","4p1","4p2","4p5","4p6","5s1","5s2","1f2","1f3","1f4","1f5","1f6","1f7","1f8","1f9","1f10","1f11","1f12","1f13","1f14","4d1","4d2","4d3","4d5","4d6","4d7","4d8","4d9","4d10","5p1","5p2","5p3","5p4","5p5","5p6","6s1","6s2",""]
request = input("Type in an element to get electron config for...\n>>")
requestNum = 0

def checkRequest(request):
  if (request not in symbolList and request not in elementNames):
    return "FALSE"
  if (len(request) <= 3):
    indexSort = symbolList.index(request)
  else:
    indexSort = elementNames.index(request)
  return indexSort

requestNum = checkRequest(request)
if (request == ""):
  request = "NULL"
if (requestNum == "FALSE"):
  print(f"Invalid input element: {request}\nBe sure you are spelling the element accurately or using the correct symbol!")
else:
  if (requestNum == 1):
    electronPrefix = "1s1"
  if (requestNum >= 2):
    electronPrefix = "1s2"
  if (requestNum > 4):
    electronPrefix = f"{electronPrefix} 2s2"
  if (requestNum > 10):
    electronPrefix = f"{electronPrefix} 2p6"
  if (requestNum > 16):
    electronPrefix = f"{electronPrefix} 3s2"
  if (requestNum > 18):
    electronPrefix = f"{electronPrefix} 3p6"
  if (requestNum > 18):
    electronPrefix = f"{electronPrefix} 3p6"
  electronString = f"{electronPrefix} {electronConfigList[requestNum]}"
  elementName = elementNames[requestNum]
  print(f"Name: {elementNames[requestNum]}")
  print(f"Symbol: {symbolList[requestNum]}")
  print(f"Electron Configuration: {electronString}")