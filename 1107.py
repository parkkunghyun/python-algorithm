"""
0-9 + -
0 -눌러도 안됨
채널은 무한대
N
버튼을 최소 몇번 눌러야하는지
100번이 디폴트

N 100
5455++
100
500000
455555
+1
0 +

재귀로 풀어야할듯? -> 근데 잘못해서 무한 루프 들어가면?
1. 일단 바로 갈 수 있는지 확인
2. 그 다음 가장 가까이 접근 -> 더 높기 / 더 낮게
3. 그리고 계속 접근하기
4. 그리고 가장 작은거 나오면 끝 -> 즉 전보다 더 값이 커지면 그만 계산
무한르프 안빠지게!
"""

