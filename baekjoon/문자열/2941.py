# 크로아티아 알파벳 (https://www.acmicpc.net/problem/2941)

dic = {"c=":"1",	
        "c-":"1",
        "dz=":"1",
        "d-":"1",
        "lj":"1",
        "nj":"1",
        "s=":"1",
        "z=":"1"}
	
word = input()
for item in dic.items():
  word = word.replace(item[0], item[1])
print(len(word))
