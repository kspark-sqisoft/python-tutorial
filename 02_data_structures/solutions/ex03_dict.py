"""
풀이 03: 딕셔너리 단어 빈도 세기.

dict.get(key, default) 패턴은 키가 없을 때 KeyError 없이 기본값을 반환하므로
빈도 카운터 구현에 최적이다. result[word] = result.get(word, 0) + 1 한 줄이
존재 여부 검사 + 초기화 + 증가를 모두 처리한다.
collections.Counter 를 쓰면 더 간결하지만, 여기서는 딕셔너리 기본기를 익히는 것이 목적이다.
"""

sentence = "the quick brown fox jumps over the lazy dog"

freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

assert freq["the"] == 2
assert freq["fox"] == 1
assert freq["dog"] == 1
assert len(freq) == 8
print("OK")
