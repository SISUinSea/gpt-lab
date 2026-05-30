# -*- coding: utf-8 -*-
"""Multi-Head Self-Attention 과제 템플릿."""

import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):
    """
    GPT의 causal self-attention을 구현합니다.

    구현할 핵심:
    - Q/K/V projection
    - head 분리: (B, T, C) -> (B, n_heads, T, head_dim)
    - attention score = QK^T / sqrt(head_dim)
    - causal mask로 미래 토큰 가리기
    - attention weight와 V를 곱한 뒤 head를 다시 합치기
    """

    def __init__(
        self,
        d_model: int,
        n_heads: int,
        drop_rate: float = 0.1,
        qkv_bias: bool = False,
    ):
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        self.d_model = d_model  # 이게 책에서는 d_out
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        
        self.W_query = nn.Linear(d_model, d_model, qkv_bias)
        self.W_key = nn.Linear(d_model, d_model, qkv_bias)
        self.W_value = nn.Linear(d_model, d_model, qkv_bias)

        self.out_proj = nn.Linear(d_model, d_model)  # TODO. 이거 왜 해주는거임??? -> 인정!
        self.dropout = nn.Dropout(drop_rate)

        

    def forward(
        self,
        x: torch.Tensor,
        causal_mask: bool = True,
        return_attention_weights: bool = False,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        """
        TODO: multi-head attention forward를 구현합니다.

        Args:
            x: (batch_size, seq_len, d_model)
            causal_mask: True이면 미래 위치를 볼 수 없게 mask 처리
            return_attention_weights: True이면 attention weight도 함께 반환
        """
        b, seq_len, _ = x.shape
        
        # keys, values, queries 를 만든다.
        keys = self.W_key(x)
        values = self.W_value(x)
        queries = self.W_query(x)

        # kvq를 (batch, tokens, head num , head dim)으로 해석하는 텐서로 만든다.
        keys = keys.view(b, seq_len, self.n_heads, self.head_dim)
        values = keys.view(b, seq_len, self.n_heads, self.head_dim)
        queries = keys.view(b, seq_len, self.n_heads, self.head_dim)

        # kvq를 (batch, head num, tokens, head dim)으로 transpose 한다.
        keys = keys.transpose(1, 2)
        values = values.transpose(1, 2)
        queries = queries.transpose(1, 2)

        # attention scores를 계산한다.
        attention_scores = queries @ keys.transpose(2, 3)

        # causal mask를 적용한다(causal_mask가 true인 경우에만 적용)
        if causal_mask:
            mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
            attention_scores = attention_scores.masked_fill(mask.bool(), -torch.inf)


        # softmax를 적용해서 attention weight을 계산한다.
        attention_weights = torch.softmax(attention_scores / self.head_dim ** 0.5, dim=-1)
        
        # dropout을 적용한다.
        attention_weights = self.dropout(attention_weights)

        # 최종적인 context vector 값을 계산한다.
        context_vector = (attention_weights @ values).transpose(1, 2)

        # context vector의 head를 결합한다.
        context_vector = context_vector.contiguous().view(b, seq_len, self.d_model)

        # out_projection을 통과시켜 값들을 합친다.
        context_vector = self.out_proj(context_vector)

        return context_vector, attention_weights if return_attention_weights else context_vector

        

