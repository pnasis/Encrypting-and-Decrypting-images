import heapq

def score (x: int, A: list):
  total = sum(A[x:])
  return total

def calculate_hindex(N: int, citations: list):
  minH = []
  ans = []
  hindex = 0
  for i in range(N):
    if citations[i]>hindex:
      heapq.heappush(minH,citations[i])
    while minH and minH[0] <= hindex:
      heapq.heappop(minH)
    if len(minH) >= hindex+1:
      hindex += 1
    ans.append(hindex)
  return ans

if __name__ == "__main__":
  T = int(input())
  for i in range(T):
   N = int(input())
   K = input()                               # The number of papers
   citations = [int(a) for a in K.split()]   # The number of citations for each paper
   scores = calculate_hindex(N,citations)
   print("Case #%d: " % (i+1), end='')
   print(*scores)
