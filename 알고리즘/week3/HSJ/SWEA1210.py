def move(y, x):
  if y == 0:
    return x

  for di, dj in [[0, -1], [0, 1], [-1, 0]]:
    ni, nj = y + di, x + dj
    if ni >= 0 and ni < 100 and nj >= 0 and nj < 100:
      if visited[ni][nj] != 1 and arr[ni][nj] == 1:
        visited[ni][nj] = 1
        break
      else:
        continue

  return move(ni, nj)

for _ in range(10):
  tc = int(input())
  arr = [list(map(int, input().split())) for _ in range(100)]
  end = arr[99].index(2)
  visited = [[0]*100 for _ in range(100)]
  visited[99][end] = 1
  
  result = move(99, end)
  
  print(f'#{tc} {result}')




# arr[99]에서 도착점인 2의 인덱스 찾기
  # 상, 좌, 우 에 1이 있는 곳 탐색 (좌우는visited 체크 해줘야겠다)
  # 좌, 우를 우선적으로 탐색하고 거기로 가기
  # 하나만 있으면 그곳으로 위치를 이동하고 또 탐색하면 됨
  # 두개있는 경우엔 이전

  # result = 도착하게되는 출발점의 x좌표