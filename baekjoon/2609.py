# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

def gcd(a, b):
  if b==0:
    return a
  return gcd(b, a%b)

def lcm(a, b):
  return int(a*b/gcd(a,b))

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
