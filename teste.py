from io import StringIO
import sys

entrada = '''3
1 2 3
'''
sys.stdin = StringIO(entrada)

# agora o input() vai funcionar como se tivesse digitado
n = int(input())
nums = list(map(int, input().split()))
print(sum(nums))  # deve imprimir 6
