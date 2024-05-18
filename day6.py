#막대기
n = int(input())
a=[]
b=1

for i in range(n):
	a.append(int(input()))
	
max_ = a[-1]

for i in range(n-1, -1, -1):
	if max_ < a[i-1]:
		b +=1
		
print(b)

#의좋은 형제
n1,n2 = map(int,input().split())
d = int(input())

for i in range(1, d+1):
	if i % 2 == 1:
		if n1 % 2 == 0:
			n2 += (n1//2)
			n1 //= 2
		else:
			n2 += (n1//2 + 1)
			n1 //= 2
	else:
		if n2 % 2 == 0:
			n1 += (n2//2)
			n2 //= 2
		else:
			n1 += (n2//2 + 1)
			n2 //= 2

print(n1, n2)

#구름 장식물
n =  int(input())
a = [1,1]
c = 0			#둘레
for i in range(1,n):			#피보나치 수열 구하기
	a.append(a[i] + a[i-1])

for i in a:		#다 더해주기
	c += i
c-=a[-1]		#타일 갯수와 반복횟수가 달라서 더해줌
print(c*2+2)			#계산