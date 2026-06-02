# Long Token Report

Showing up to 30 rows per section. See `tokens.csv` for the full table.

## Longest By Byte Length

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 4529 | merge | 48 | 16 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3  ...</code> | long_bytes, long_chars, repeated_run |
| 7119 | merge | 48 | 16 | <code>&quot;ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3  ...</code> | long_bytes, long_chars, repeated_run |
| 9404 | merge | 32 | 32 | <code>&quot;................................&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e</code> | long_bytes, long_chars, repeated_run |
| 6603 | merge | 28 | 12 | <code>&quot;강추@강추@강추@강추@&quot;</code> | <code>ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40</code> | - |
| 3466 | merge | 25 | 9 | <code>&quot; ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>20 e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | contains_whitespace, repeated_run |
| 7835 | merge | 25 | 11 | <code>&quot;tv 전기세가 아깝다&quot;</code> | <code>74 76 20 ec a0 84 ea b8 b0 ec 84 b8 ea b0 80 20 ec 95 84 ea b9 9d eb 8b a4</code> | contains_whitespace |
| 1282 | merge | 24 | 8 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 3594 | merge | 24 | 8 | <code>&quot;ㅠㅠㅠㅠㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0</code> | repeated_run |
| 8323 | merge | 24 | 10 | <code>&quot; 여운이 남는 영화&quot;</code> | <code>20 ec 97 ac ec 9a b4 ec 9d b4 20 eb 82 a8 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 5486 | merge | 23 | 9 | <code>&quot; 처음부터 끝까지&quot;</code> | <code>20 ec b2 98 ec 9d 8c eb b6 80 ed 84 b0 20 eb 81 9d ea b9 8c ec a7 80</code> | contains_whitespace |
| 9673 | merge | 23 | 9 | <code>&quot; 따뜻해지는 영화&quot;</code> | <code>20 eb 94 b0 eb 9c bb ed 95 b4 ec a7 80 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 9718 | merge | 23 | 9 | <code>&quot;\n처음부터 끝까지&quot;</code> | <code>0a ec b2 98 ec 9d 8c eb b6 80 ed 84 b0 20 eb 81 9d ea b9 8c ec a7 80</code> | contains_whitespace, control_char |
| 7648 | merge | 22 | 8 | <code>&quot; 킬링타임용으로&quot;</code> | <code>20 ed 82 ac eb a7 81 ed 83 80 ec 9e 84 ec 9a a9 ec 9c bc eb a1 9c</code> | contains_whitespace |
| 5713 | merge | 21 | 7 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 8798 | merge | 21 | 9 | <code>&quot; 이 영화를 보고&quot;</code> | <code>20 ec 9d b4 20 ec 98 81 ed 99 94 eb a5 bc 20 eb b3 b4 ea b3 a0</code> | contains_whitespace |
| 5062 | merge | 20 | 8 | <code>&quot; 아름다운 영화&quot;</code> | <code>20 ec 95 84 eb a6 84 eb 8b a4 ec 9a b4 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 5969 | merge | 20 | 8 | <code>&quot; 재밌게 봤는데&quot;</code> | <code>20 ec 9e ac eb b0 8c ea b2 8c 20 eb b4 a4 eb 8a 94 eb 8d b0</code> | contains_whitespace |
| 5977 | merge | 20 | 8 | <code>&quot; 최고의 드라마&quot;</code> | <code>20 ec b5 9c ea b3 a0 ec 9d 98 20 eb 93 9c eb 9d bc eb a7 88</code> | contains_whitespace |
| 6088 | merge | 20 | 8 | <code>&quot; 감동적인 영화&quot;</code> | <code>20 ea b0 90 eb 8f 99 ec a0 81 ec 9d b8 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 7618 | merge | 20 | 8 | <code>&quot; 배우들의 연기&quot;</code> | <code>20 eb b0 b0 ec 9a b0 eb 93 a4 ec 9d 98 20 ec 97 b0 ea b8 b0</code> | contains_whitespace |
| 7916 | merge | 20 | 8 | <code>&quot; 재미없는 영화&quot;</code> | <code>20 ec 9e ac eb af b8 ec 97 86 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 8101 | merge | 20 | 8 | <code>&quot; 스토리가 너무&quot;</code> | <code>20 ec 8a a4 ed 86 a0 eb a6 ac ea b0 80 20 eb 84 88 eb ac b4</code> | contains_whitespace |
| 8219 | merge | 20 | 8 | <code>&quot; 배우들 연기도&quot;</code> | <code>20 eb b0 b0 ec 9a b0 eb 93 a4 20 ec 97 b0 ea b8 b0 eb 8f 84</code> | contains_whitespace |
| 8284 | merge | 20 | 8 | <code>&quot; 나왔으면 좋겠&quot;</code> | <code>20 eb 82 98 ec 99 94 ec 9c bc eb a9 b4 20 ec a2 8b ea b2 a0</code> | contains_whitespace |
| 8500 | merge | 20 | 8 | <code>&quot; 정말 재미있게&quot;</code> | <code>20 ec a0 95 eb a7 90 20 ec 9e ac eb af b8 ec 9e 88 ea b2 8c</code> | contains_whitespace |
| 8982 | merge | 20 | 8 | <code>&quot; 무섭지도 않고&quot;</code> | <code>20 eb ac b4 ec 84 ad ec a7 80 eb 8f 84 20 ec 95 8a ea b3 a0</code> | contains_whitespace |
| 9009 | merge | 20 | 8 | <code>&quot; 생각나는 영화&quot;</code> | <code>20 ec 83 9d ea b0 81 eb 82 98 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 9117 | merge | 20 | 8 | <code>&quot;인의 명복을 빕&quot;</code> | <code>ec 9d b8 ec 9d 98 20 eb aa 85 eb b3 b5 ec 9d 84 20 eb b9 95</code> | contains_whitespace |
| 9180 | merge | 20 | 8 | <code>&quot; 많은 사람들이&quot;</code> | <code>20 eb a7 8e ec 9d 80 20 ec 82 ac eb 9e 8c eb 93 a4 ec 9d b4</code> | contains_whitespace |
| 9761 | merge | 20 | 8 | <code>&quot; 잊혀지지 않는&quot;</code> | <code>20 ec 9e 8a ed 98 80 ec a7 80 ec a7 80 20 ec 95 8a eb 8a 94</code> | contains_whitespace |

## Longest By Character Length

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 9404 | merge | 32 | 32 | <code>&quot;................................&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e</code> | long_bytes, long_chars, repeated_run |
| 2797 | merge | 16 | 16 | <code>&quot;................&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e 2e</code> | long_chars, repeated_run |
| 4529 | merge | 48 | 16 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3  ...</code> | long_bytes, long_chars, repeated_run |
| 6688 | merge | 16 | 16 | <code>&quot;!!!!!!!!!!!!!!!!&quot;</code> | <code>21 21 21 21 21 21 21 21 21 21 21 21 21 21 21 21</code> | long_chars, repeated_run |
| 7119 | merge | 48 | 16 | <code>&quot;ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3  ...</code> | long_bytes, long_chars, repeated_run |
| 8396 | merge | 16 | 16 | <code>&quot;????????????????&quot;</code> | <code>3f 3f 3f 3f 3f 3f 3f 3f 3f 3f 3f 3f 3f 3f 3f 3f</code> | long_chars, repeated_run |
| 6603 | merge | 28 | 12 | <code>&quot;강추@강추@강추@강추@&quot;</code> | <code>ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40 ea b0 95 ec b6 94 40</code> | - |
| 7835 | merge | 25 | 11 | <code>&quot;tv 전기세가 아깝다&quot;</code> | <code>74 76 20 ec a0 84 ea b8 b0 ec 84 b8 ea b0 80 20 ec 95 84 ea b9 9d eb 8b a4</code> | contains_whitespace |
| 8323 | merge | 24 | 10 | <code>&quot; 여운이 남는 영화&quot;</code> | <code>20 ec 97 ac ec 9a b4 ec 9d b4 20 eb 82 a8 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 3466 | merge | 25 | 9 | <code>&quot; ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>20 e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | contains_whitespace, repeated_run |
| 5486 | merge | 23 | 9 | <code>&quot; 처음부터 끝까지&quot;</code> | <code>20 ec b2 98 ec 9d 8c eb b6 80 ed 84 b0 20 eb 81 9d ea b9 8c ec a7 80</code> | contains_whitespace |
| 8798 | merge | 21 | 9 | <code>&quot; 이 영화를 보고&quot;</code> | <code>20 ec 9d b4 20 ec 98 81 ed 99 94 eb a5 bc 20 eb b3 b4 ea b3 a0</code> | contains_whitespace |
| 9238 | merge | 9 | 9 | <code>&quot;.........&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e 2e</code> | repeated_run |
| 9673 | merge | 23 | 9 | <code>&quot; 따뜻해지는 영화&quot;</code> | <code>20 eb 94 b0 eb 9c bb ed 95 b4 ec a7 80 eb 8a 94 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 9718 | merge | 23 | 9 | <code>&quot;\n처음부터 끝까지&quot;</code> | <code>0a ec b2 98 ec 9d 8c eb b6 80 ed 84 b0 20 eb 81 9d ea b9 8c ec a7 80</code> | contains_whitespace, control_char |
| 1179 | merge | 8 | 8 | <code>&quot;........&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e</code> | repeated_run |
| 1282 | merge | 24 | 8 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 2260 | merge | 8 | 8 | <code>&quot;!!!!!!!!&quot;</code> | <code>21 21 21 21 21 21 21 21</code> | repeated_run |
| 3594 | merge | 24 | 8 | <code>&quot;ㅠㅠㅠㅠㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0</code> | repeated_run |
| 3848 | merge | 8 | 8 | <code>&quot;????????&quot;</code> | <code>3f 3f 3f 3f 3f 3f 3f 3f</code> | repeated_run |
| 5062 | merge | 20 | 8 | <code>&quot; 아름다운 영화&quot;</code> | <code>20 ec 95 84 eb a6 84 eb 8b a4 ec 9a b4 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 5421 | merge | 8 | 8 | <code>&quot;~~~~~~~~&quot;</code> | <code>7e 7e 7e 7e 7e 7e 7e 7e</code> | repeated_run |
| 5969 | merge | 20 | 8 | <code>&quot; 재밌게 봤는데&quot;</code> | <code>20 ec 9e ac eb b0 8c ea b2 8c 20 eb b4 a4 eb 8a 94 eb 8d b0</code> | contains_whitespace |
| 5977 | merge | 20 | 8 | <code>&quot; 최고의 드라마&quot;</code> | <code>20 ec b5 9c ea b3 a0 ec 9d 98 20 eb 93 9c eb 9d bc eb a7 88</code> | contains_whitespace |
| 6088 | merge | 20 | 8 | <code>&quot; 감동적인 영화&quot;</code> | <code>20 ea b0 90 eb 8f 99 ec a0 81 ec 9d b8 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 6563 | merge | 8 | 8 | <code>&quot;.......\n&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 0a</code> | contains_whitespace, control_char, repeated_run |
| 6888 | merge | 8 | 8 | <code>&quot;;;;;;;;;&quot;</code> | <code>3b 3b 3b 3b 3b 3b 3b 3b</code> | repeated_run |
| 7618 | merge | 20 | 8 | <code>&quot; 배우들의 연기&quot;</code> | <code>20 eb b0 b0 ec 9a b0 eb 93 a4 ec 9d 98 20 ec 97 b0 ea b8 b0</code> | contains_whitespace |
| 7648 | merge | 22 | 8 | <code>&quot; 킬링타임용으로&quot;</code> | <code>20 ed 82 ac eb a7 81 ed 83 80 ec 9e 84 ec 9a a9 ec 9c bc eb a1 9c</code> | contains_whitespace |
| 7661 | merge | 18 | 8 | <code>&quot; 쓰레기 영화\n&quot;</code> | <code>20 ec 93 b0 eb a0 88 ea b8 b0 20 ec 98 81 ed 99 94 0a</code> | contains_whitespace, control_char |

## Repeated Character Runs

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 373 | merge | 3 | 3 | <code>&quot;...&quot;</code> | <code>2e 2e 2e</code> | repeated_run |
| 427 | merge | 4 | 4 | <code>&quot;....&quot;</code> | <code>2e 2e 2e 2e</code> | repeated_run |
| 475 | merge | 4 | 4 | <code>&quot;...\n&quot;</code> | <code>2e 2e 2e 0a</code> | contains_whitespace, control_char, repeated_run |
| 584 | merge | 12 | 4 | <code>&quot;ㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 891 | merge | 4 | 4 | <code>&quot;!!!!&quot;</code> | <code>21 21 21 21</code> | repeated_run |
| 971 | merge | 6 | 4 | <code>&quot;다...&quot;</code> | <code>eb 8b a4 2e 2e 2e</code> | repeated_run |
| 1078 | merge | 5 | 5 | <code>&quot;....\n&quot;</code> | <code>2e 2e 2e 2e 0a</code> | contains_whitespace, control_char, repeated_run |
| 1179 | merge | 8 | 8 | <code>&quot;........&quot;</code> | <code>2e 2e 2e 2e 2e 2e 2e 2e</code> | repeated_run |
| 1211 | merge | 3 | 3 | <code>&quot;!!!&quot;</code> | <code>21 21 21</code> | repeated_run |
| 1240 | merge | 9 | 3 | <code>&quot;ㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 1282 | merge | 24 | 8 | <code>&quot;ㅋㅋㅋㅋㅋㅋㅋㅋ&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | repeated_run |
| 1391 | merge | 7 | 5 | <code>&quot;다...\n&quot;</code> | <code>eb 8b a4 2e 2e 2e 0a</code> | contains_whitespace, control_char, repeated_run |
| 1406 | merge | 4 | 4 | <code>&quot;!!!\n&quot;</code> | <code>21 21 21 0a</code> | contains_whitespace, control_char, repeated_run |
| 1680 | merge | 4 | 4 | <code>&quot;????&quot;</code> | <code>3f 3f 3f 3f</code> | repeated_run |
| 1715 | merge | 10 | 4 | <code>&quot; ㅋㅋㅋ&quot;</code> | <code>20 e3 85 8b e3 85 8b e3 85 8b</code> | contains_whitespace, repeated_run |
| 1797 | merge | 12 | 4 | <code>&quot;ㅠㅠㅠㅠ&quot;</code> | <code>e3 85 a0 e3 85 a0 e3 85 a0 e3 85 a0</code> | repeated_run |
| 1826 | merge | 4 | 4 | <code>&quot;~~~~&quot;</code> | <code>7e 7e 7e 7e</code> | repeated_run |
| 1831 | merge | 4 | 4 | <code>&quot; ...&quot;</code> | <code>20 2e 2e 2e</code> | contains_whitespace, repeated_run |
| 1886 | merge | 3 | 3 | <code>&quot;,,,&quot;</code> | <code>2c 2c 2c</code> | repeated_run |
| 1925 | merge | 13 | 5 | <code>&quot; ㅋㅋㅋㅋ&quot;</code> | <code>20 e3 85 8b e3 85 8b e3 85 8b e3 85 8b</code> | contains_whitespace, repeated_run |
| 2087 | merge | 7 | 5 | <code>&quot;다....&quot;</code> | <code>eb 8b a4 2e 2e 2e 2e</code> | repeated_run |
| 2089 | merge | 10 | 4 | <code>&quot;ㅋㅋㅋ\n&quot;</code> | <code>e3 85 8b e3 85 8b e3 85 8b 0a</code> | contains_whitespace, control_char, repeated_run |
| 2208 | merge | 5 | 5 | <code>&quot;.....&quot;</code> | <code>2e 2e 2e 2e 2e</code> | repeated_run |
| 2221 | merge | 11 | 5 | <code>&quot; ㅋㅋㅋ\n&quot;</code> | <code>20 e3 85 8b e3 85 8b e3 85 8b 0a</code> | contains_whitespace, control_char, repeated_run |
| 2260 | merge | 8 | 8 | <code>&quot;!!!!!!!!&quot;</code> | <code>21 21 21 21 21 21 21 21</code> | repeated_run |
| 2272 | merge | 4 | 4 | <code>&quot; OOO&quot;</code> | <code>20 4f 4f 4f</code> | contains_whitespace, repeated_run |
| 2280 | merge | 4 | 4 | <code>&quot;;;;;&quot;</code> | <code>3b 3b 3b 3b</code> | repeated_run |
| 2337 | merge | 3 | 3 | <code>&quot;???&quot;</code> | <code>3f 3f 3f</code> | repeated_run |
| 2343 | merge | 3 | 3 | <code>&quot;~~~&quot;</code> | <code>7e 7e 7e</code> | repeated_run |
| 2530 | merge | 3 | 3 | <code>&quot;;;;&quot;</code> | <code>3b 3b 3b</code> | repeated_run |
