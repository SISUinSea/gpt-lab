"""
먼저 corpus를 '한글자'씩 짤라 -> list에 담아
``` python
for c in corpus:
    temp.append(c)
    # TODO. temp 이름 바꿔

# 순회하면서 list안에 있는 한글자씩 byte로 변환해서 등록해 ex) 한글이라면 3개를, 영어라면 1개를 -> merges
for c in temp:
    merges.append(tuple(utf8_encode(c))) # TODO. utf8 형식으로 어떻게 인코딩함??

merges.sort(reverse) # TODO. 길이가 긴 것부터 짧은 거로 sort 해야 해.
# TODO. merges에 '모든' 애들이 다 들어가있나??

corpus_encoded = str_to_encodedlist(corpus)

# 반복 (merges < vocab_size - id to token)
# corpus 순회하면서 짝찌 지어서 빈도수 측정해 -> 제일 높은놈 사전에 등록 -> merges
while len(merges) <= vocab_size - len(id_to_token): # TODO. vocab_size 를 0으로 줄여나가는 방식은 어떨까?
    freq_dic = defaultdict(tuple, int)
    corpus_idx = 0
    while corpus_idx < len(corpus_encoded):
        t1, t2 = "", ""
        for word in merges:
            if corpus_idx + len(word) < len(corpus) and word == corpus[corpus_idx: corpus_idx + len(word)]: # starts with 같은 함수가 있나?? 없다면 만드는건 어떨까? 왜냐하면 그냥 조건문으로 넣기에는 너무 지저분해보인다.
                t1 = word
                corpus_idx += len(word)
                break
        if corpus_idx >= len(corpus):
            freq_dic.add((t1+t2))
            break
        for word in merges:
            if corpus_idx + len(word) < len(corpus) and word == corpus[corpus_idx: corpus_idx + len(word)]:
                t2 = word
                corpus_idx += len(word)
                break
        freq_dic.add((t1+t2))
    add merges the most frequently added word in freq_dic
    # 근데 merges에 정렬된 상태로 집어넣어야 하는데?? 새롭게 만들어지는 애가 항상 최장길이 word라는 보장이 있나?
    




 

# merges에있는거 id to token, token to id에 넣어

```


마지막




어떻게 짝찌어
list안에 있는 단어를 voca에서 단

주의:
모든 등록에는 voca_size를 1 늘려줄 것
"""
