import torch
import torch.nn as nn

class SelfAttention_v1(nn.Module):
  def __init__(self, d_in, d_out):
    super().__init__()
    self.W_query = nn.Parameter(torch.rand(d_in, d_out))
    self.W_key = nn.Parameter(torch.rand(d_in, d_out))
    self.W_value = nn.Parameter(torch.rand(d_in, d_out))
  
  def forward(self, x):
    """
    여기서 해야 하는거는.... 뭐지?
    어떤 토큰 임베딩 x에 대해서 전체 문장에서의 context_vector를 계산해서 반환하는 것.
    """
    queries = x @ self.W_query
    keys = x @ self.W_key
    values = x @ self.W_value

    attn_scores = queries @ keys.T
    
