datne = open("aka.txt", "r", encoding="utf 8")

for i in datne.read():
  print(i)

datne.close()