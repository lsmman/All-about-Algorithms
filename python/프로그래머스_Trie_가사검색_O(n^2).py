def solution(words, queries):
    answer = []
    words_n_leng = [(word, len(word)) for word in words]
    question_mark  = '?'
    for query in queries:
        cnt = 0
        query_leng = len(query)
        front = True if query[0] is question_mark else False
        if front:
            for idx, char in enumerate(query):
                if not (char is question_mark):
                    q_idx = idx
                    break
            for word, w_leng in words_n_leng:
                if query_leng is w_leng:
                    if query[idx:] == word[q_idx:]:
                        cnt = cnt + 1
        else:
            for idx, char in enumerate(query):
                if (char is question_mark):
                    q_idx = idx
                    break
            for word, w_leng in words_n_leng:
                if query_leng is w_leng:
                    if query[:idx] == word[:idx]:
                        cnt = cnt + 1
        answer.append(cnt)
        
    return answer