import torch

inputs = torch.tensor(
  [[0.43, 0.15, 0.89], # Your     (x^1)
   [0.55, 0.87, 0.66], # journey  (x^2)
   [0.57, 0.85, 0.64], # starts   (x^3)
   [0.22, 0.58, 0.33], # with     (x^4)
   [0.77, 0.25, 0.10], # one      (x^5)
   [0.05, 0.80, 0.55]] # step     (x^6)
)

query = inputs[1]

# 1.0. query == x^2 인 경우에 가중치들의 값을 계산해보세요.
attention_scores_2 = torch.empty(inputs.shape[0]) # TODO. torch로 벡터를 만드는 거랑, 그냥 [] 로 배열을 만드는 거랑 무슨 차이지?
print("[attention_scores]:")
for i, x_i in enumerate(inputs):
    attention_scores_2[i] = torch.dot(query, x_i)
    print(attention_scores_2)
weight_scores_2 = torch.softmax(attention_scores_2, dim=0) # TODO. dim=0를 왜 붙여줘야 하는거지??
print("[weight_scores]:")
print(weight_scores_2)
print(torch.sum(weight_scores_2))

# # 1.1. query 에 대한 어텐션 점수를 계산하세요.
context_vector_2 = torch.empty(query.shape)
print(context_vector_2)
for i, x_i in enumerate(inputs):
    context_vector_2 += weight_scores_2[i] * x_i
    print(context_vector_2)
print(context_vector_2)

# 2.0. 전체 가중치를 한꺼번에 계산하는 방법을 구현하세요.
attn_scores = torch.zeros_like(inputs.shape[0], inputs.shape[0])
print(attn_scores)
for i, x_i in enumerate(inputs):
    for j, x_j in enumerate(inputs):
        attn_scores[i,j] = torch.dot(x_i, x_j)
    print(attn_scores)
attn_scores = inputs @ inputs.T
weight_scores = torch.softmax(attn_scores, dim=-1) # TODO. 여기서 dim = -1이 무슨 뜻이지?
print (weight_scores)

# 2.1. 전체 어텐션 점수를 한번에 계산하는 방법을 구현하세요.
## w * input
result = weight_scores @ inputs
print (result)

# TODO. 근데 이렇게 해서 나온 result가 결국 뭐지? -> 전체 문장의 맥락을 고려했을 때 하나의 토큰에 대해 전체 토큰과 어떤 관계를 가지고 있는지, 어떤 토큰이 더 큰 가중치를 가지고 있는지..? (어떤 토큰과 더 큰 밀접도를 가지고 있는지??)