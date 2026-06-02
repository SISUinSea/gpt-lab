# Token Samples By ID Region

Showing up to 30 rows per section.

## Byte Tokens

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | byte | 1 | 1 | <code>&quot;\u0000&quot;</code> | <code>00</code> | control_char |
| 5 | byte | 1 | 1 | <code>&quot;\u0001&quot;</code> | <code>01</code> | control_char |
| 6 | byte | 1 | 1 | <code>&quot;\u0002&quot;</code> | <code>02</code> | control_char |
| 7 | byte | 1 | 1 | <code>&quot;\u0003&quot;</code> | <code>03</code> | control_char |
| 8 | byte | 1 | 1 | <code>&quot;\u0004&quot;</code> | <code>04</code> | control_char |
| 9 | byte | 1 | 1 | <code>&quot;\u0005&quot;</code> | <code>05</code> | control_char |
| 10 | byte | 1 | 1 | <code>&quot;\u0006&quot;</code> | <code>06</code> | control_char |
| 11 | byte | 1 | 1 | <code>&quot;\u0007&quot;</code> | <code>07</code> | control_char |
| 12 | byte | 1 | 1 | <code>&quot;\b&quot;</code> | <code>08</code> | control_char |
| 13 | byte | 1 | 1 | <code>&quot;\t&quot;</code> | <code>09</code> | contains_whitespace, control_char |
| 14 | byte | 1 | 1 | <code>&quot;\n&quot;</code> | <code>0a</code> | contains_whitespace, control_char |
| 15 | byte | 1 | 1 | <code>&quot;\u000b&quot;</code> | <code>0b</code> | contains_whitespace, control_char |
| 16 | byte | 1 | 1 | <code>&quot;\f&quot;</code> | <code>0c</code> | contains_whitespace, control_char |
| 17 | byte | 1 | 1 | <code>&quot;\r&quot;</code> | <code>0d</code> | contains_whitespace, control_char |
| 18 | byte | 1 | 1 | <code>&quot;\u000e&quot;</code> | <code>0e</code> | control_char |
| 19 | byte | 1 | 1 | <code>&quot;\u000f&quot;</code> | <code>0f</code> | control_char |
| 20 | byte | 1 | 1 | <code>&quot;\u0010&quot;</code> | <code>10</code> | control_char |
| 21 | byte | 1 | 1 | <code>&quot;\u0011&quot;</code> | <code>11</code> | control_char |
| 22 | byte | 1 | 1 | <code>&quot;\u0012&quot;</code> | <code>12</code> | control_char |
| 23 | byte | 1 | 1 | <code>&quot;\u0013&quot;</code> | <code>13</code> | control_char |
| 24 | byte | 1 | 1 | <code>&quot;\u0014&quot;</code> | <code>14</code> | control_char |
| 25 | byte | 1 | 1 | <code>&quot;\u0015&quot;</code> | <code>15</code> | control_char |
| 26 | byte | 1 | 1 | <code>&quot;\u0016&quot;</code> | <code>16</code> | control_char |
| 27 | byte | 1 | 1 | <code>&quot;\u0017&quot;</code> | <code>17</code> | control_char |
| 28 | byte | 1 | 1 | <code>&quot;\u0018&quot;</code> | <code>18</code> | control_char |
| 29 | byte | 1 | 1 | <code>&quot;\u0019&quot;</code> | <code>19</code> | control_char |
| 30 | byte | 1 | 1 | <code>&quot;\u001a&quot;</code> | <code>1a</code> | control_char |
| 31 | byte | 1 | 1 | <code>&quot;\u001b&quot;</code> | <code>1b</code> | control_char |
| 32 | byte | 1 | 1 | <code>&quot;\u001c&quot;</code> | <code>1c</code> | contains_whitespace, control_char |
| 33 | byte | 1 | 1 | <code>&quot;\u001d&quot;</code> | <code>1d</code> | contains_whitespace, control_char |

## Early Merge Tokens

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 260 | merge | 2 | 0 | <code>&lt;invalid utf-8: 20 ec&gt;</code> | <code>20 ec</code> | invalid_utf8 |
| 261 | merge | 2 | 0 | <code>&lt;invalid utf-8: 20 eb&gt;</code> | <code>20 eb</code> | invalid_utf8 |
| 262 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec 9d&gt;</code> | <code>ec 9d</code> | invalid_utf8 |
| 263 | merge | 2 | 0 | <code>&lt;invalid utf-8: eb 8b&gt;</code> | <code>eb 8b</code> | invalid_utf8 |
| 264 | merge | 2 | 0 | <code>&lt;invalid utf-8: ed 95&gt;</code> | <code>ed 95</code> | invalid_utf8 |
| 265 | merge | 2 | 0 | <code>&lt;invalid utf-8: ea b0&gt;</code> | <code>ea b0</code> | invalid_utf8 |
| 266 | merge | 2 | 2 | <code>&quot;..&quot;</code> | <code>2e 2e</code> | - |
| 267 | merge | 3 | 1 | <code>&quot;이&quot;</code> | <code>ec 9d b4</code> | - |
| 268 | merge | 3 | 1 | <code>&quot;다&quot;</code> | <code>eb 8b a4</code> | - |
| 269 | merge | 2 | 0 | <code>&lt;invalid utf-8: eb 8a&gt;</code> | <code>eb 8a</code> | invalid_utf8 |
| 270 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec 97&gt;</code> | <code>ec 97</code> | invalid_utf8 |
| 271 | merge | 2 | 0 | <code>&lt;invalid utf-8: ea b3&gt;</code> | <code>ea b3</code> | invalid_utf8 |
| 272 | merge | 3 | 1 | <code>&quot;는&quot;</code> | <code>eb 8a 94</code> | - |
| 273 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec a7&gt;</code> | <code>ec a7</code> | invalid_utf8 |
| 274 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec 9e&gt;</code> | <code>ec 9e</code> | invalid_utf8 |
| 275 | merge | 2 | 0 | <code>&lt;invalid utf-8: eb a7&gt;</code> | <code>eb a7</code> | invalid_utf8 |
| 276 | merge | 2 | 0 | <code>&lt;invalid utf-8: ed 99&gt;</code> | <code>ed 99</code> | invalid_utf8 |
| 277 | merge | 3 | 1 | <code>&quot;고&quot;</code> | <code>ea b3 a0</code> | - |
| 278 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec a0&gt;</code> | <code>ec a0</code> | invalid_utf8 |
| 279 | merge | 3 | 1 | <code>&quot;화&quot;</code> | <code>ed 99 94</code> | - |
| 280 | merge | 2 | 0 | <code>&lt;invalid utf-8: 98 81&gt;</code> | <code>98 81</code> | invalid_utf8 |
| 281 | merge | 2 | 0 | <code>&lt;invalid utf-8: eb 8f&gt;</code> | <code>eb 8f</code> | invalid_utf8 |
| 282 | merge | 2 | 0 | <code>&lt;invalid utf-8: ea b2&gt;</code> | <code>ea b2</code> | invalid_utf8 |
| 283 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec 95&gt;</code> | <code>ec 95</code> | invalid_utf8 |
| 284 | merge | 2 | 0 | <code>&lt;invalid utf-8: e3 85&gt;</code> | <code>e3 85</code> | invalid_utf8 |
| 285 | merge | 5 | 0 | <code>&lt;invalid utf-8: 98 81 ed 99 94&gt;</code> | <code>98 81 ed 99 94</code> | invalid_utf8 |
| 286 | merge | 3 | 1 | <code>&quot;지&quot;</code> | <code>ec a7 80</code> | - |
| 287 | merge | 2 | 0 | <code>&lt;invalid utf-8: ec 9a&gt;</code> | <code>ec 9a</code> | invalid_utf8 |
| 288 | merge | 2 | 0 | <code>&lt;invalid utf-8: ea b8&gt;</code> | <code>ea b8</code> | invalid_utf8 |
| 289 | merge | 3 | 1 | <code>&quot;하&quot;</code> | <code>ed 95 98</code> | - |

## Middle Merge Tokens

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 5115 | merge | 7 | 3 | <code>&quot;\n좋은&quot;</code> | <code>0a ec a2 8b ec 9d 80</code> | contains_whitespace, control_char |
| 5116 | merge | 13 | 5 | <code>&quot; 진심으로&quot;</code> | <code>20 ec a7 84 ec 8b ac ec 9c bc eb a1 9c</code> | contains_whitespace |
| 5117 | merge | 10 | 4 | <code>&quot;게 만든&quot;</code> | <code>ea b2 8c 20 eb a7 8c eb 93 a0</code> | contains_whitespace |
| 5118 | merge | 6 | 0 | <code>&lt;invalid utf-8: eb 8b a4 0a ec a1&gt;</code> | <code>eb 8b a4 0a ec a1</code> | invalid_utf8 |
| 5119 | merge | 4 | 2 | <code>&quot; 뭉&quot;</code> | <code>20 eb ad 89</code> | contains_whitespace |
| 5120 | merge | 7 | 3 | <code>&quot;에요\n&quot;</code> | <code>ec 97 90 ec 9a 94 0a</code> | contains_whitespace, control_char |
| 5121 | merge | 10 | 4 | <code>&quot; 영화중&quot;</code> | <code>20 ec 98 81 ed 99 94 ec a4 91</code> | contains_whitespace |
| 5122 | merge | 7 | 3 | <code>&quot; 씁쓸&quot;</code> | <code>20 ec 94 81 ec 93 b8</code> | contains_whitespace |
| 5123 | merge | 6 | 2 | <code>&quot;웃기&quot;</code> | <code>ec 9b 83 ea b8 b0</code> | - |
| 5124 | merge | 10 | 4 | <code>&quot; 무서웠&quot;</code> | <code>20 eb ac b4 ec 84 9c ec 9b a0</code> | contains_whitespace |
| 5125 | merge | 4 | 0 | <code>&lt;invalid utf-8: ac eb 9e 98&gt;</code> | <code>ac eb 9e 98</code> | invalid_utf8 |
| 5126 | merge | 2 | 0 | <code>&lt;invalid utf-8: ad 89&gt;</code> | <code>ad 89</code> | invalid_utf8 |
| 5127 | merge | 7 | 3 | <code>&quot; 되게&quot;</code> | <code>20 eb 90 98 ea b2 8c</code> | contains_whitespace |
| 5128 | merge | 6 | 2 | <code>&quot;외로&quot;</code> | <code>ec 99 b8 eb a1 9c</code> | - |
| 5129 | merge | 9 | 3 | <code>&quot;해주는&quot;</code> | <code>ed 95 b4 ec a3 bc eb 8a 94</code> | - |
| 5130 | merge | 6 | 2 | <code>&quot;저는&quot;</code> | <code>ec a0 80 eb 8a 94</code> | - |
| 5131 | merge | 3 | 1 | <code>&quot;략&quot;</code> | <code>eb 9e b5</code> | - |
| 5132 | merge | 7 | 3 | <code>&quot; 결론&quot;</code> | <code>20 ea b2 b0 eb a1 a0</code> | contains_whitespace |
| 5133 | merge | 3 | 1 | <code>&quot;ㅈ&quot;</code> | <code>e3 85 88</code> | - |
| 5134 | merge | 6 | 2 | <code>&quot;장을&quot;</code> | <code>ec 9e a5 ec 9d 84</code> | - |
| 5135 | merge | 10 | 4 | <code>&quot;한 소재&quot;</code> | <code>ed 95 9c 20 ec 86 8c ec 9e ac</code> | contains_whitespace |
| 5136 | merge | 13 | 5 | <code>&quot;었던 영화&quot;</code> | <code>ec 97 88 eb 8d 98 20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 5137 | merge | 6 | 2 | <code>&quot;들만&quot;</code> | <code>eb 93 a4 eb a7 8c</code> | - |
| 5138 | merge | 6 | 2 | <code>&quot;역대&quot;</code> | <code>ec 97 ad eb 8c 80</code> | - |
| 5139 | merge | 4 | 0 | <code>&lt;invalid utf-8: eb 84 88 eb&gt;</code> | <code>eb 84 88 eb</code> | invalid_utf8 |
| 5140 | merge | 4 | 2 | <code>&quot; 썼&quot;</code> | <code>20 ec 8d bc</code> | contains_whitespace |
| 5141 | merge | 9 | 3 | <code>&quot;어이없&quot;</code> | <code>ec 96 b4 ec 9d b4 ec 97 86</code> | - |
| 5142 | merge | 6 | 2 | <code>&quot;겨진&quot;</code> | <code>ea b2 a8 ec a7 84</code> | - |
| 5143 | merge | 6 | 2 | <code>&quot;대의&quot;</code> | <code>eb 8c 80 ec 9d 98</code> | - |
| 5144 | merge | 10 | 4 | <code>&quot; 몰입감&quot;</code> | <code>20 eb aa b0 ec 9e 85 ea b0 90</code> | contains_whitespace |

## Late Merge Tokens

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 9970 | merge | 13 | 5 | <code>&quot;하는 모습&quot;</code> | <code>ed 95 98 eb 8a 94 20 eb aa a8 ec 8a b5</code> | contains_whitespace |
| 9971 | merge | 7 | 3 | <code>&quot;를 하&quot;</code> | <code>eb a5 bc 20 ed 95 98</code> | contains_whitespace |
| 9972 | merge | 13 | 5 | <code>&quot; 어벤져스&quot;</code> | <code>20 ec 96 b4 eb b2 a4 ec a0 b8 ec 8a a4</code> | contains_whitespace |
| 9973 | merge | 6 | 2 | <code>&quot;앞에&quot;</code> | <code>ec 95 9e ec 97 90</code> | - |
| 9974 | merge | 10 | 4 | <code>&quot; 개노잼&quot;</code> | <code>20 ea b0 9c eb 85 b8 ec 9e bc</code> | contains_whitespace |
| 9975 | merge | 13 | 5 | <code>&quot; 안타까움&quot;</code> | <code>20 ec 95 88 ed 83 80 ea b9 8c ec 9b 80</code> | contains_whitespace |
| 9976 | merge | 4 | 2 | <code>&quot;\n굿&quot;</code> | <code>0a ea b5 bf</code> | contains_whitespace, control_char |
| 9977 | merge | 13 | 5 | <code>&quot; 재미있어&quot;</code> | <code>20 ec 9e ac eb af b8 ec 9e 88 ec 96 b4</code> | contains_whitespace |
| 9978 | merge | 9 | 3 | <code>&quot;놈들이&quot;</code> | <code>eb 86 88 eb 93 a4 ec 9d b4</code> | - |
| 9979 | merge | 13 | 5 | <code>&quot;보다 못한&quot;</code> | <code>eb b3 b4 eb 8b a4 20 eb aa bb ed 95 9c</code> | contains_whitespace |
| 9980 | merge | 7 | 3 | <code>&quot;은 있&quot;</code> | <code>ec 9d 80 20 ec 9e 88</code> | contains_whitespace |
| 9981 | merge | 7 | 3 | <code>&quot;\n주연&quot;</code> | <code>0a ec a3 bc ec 97 b0</code> | contains_whitespace, control_char |
| 9982 | merge | 7 | 3 | <code>&quot; 똑똑&quot;</code> | <code>20 eb 98 91 eb 98 91</code> | contains_whitespace |
| 9983 | merge | 9 | 3 | <code>&quot;크레딧&quot;</code> | <code>ed 81 ac eb a0 88 eb 94 a7</code> | - |
| 9984 | merge | 10 | 4 | <code>&quot;하지만,&quot;</code> | <code>ed 95 98 ec a7 80 eb a7 8c 2c</code> | - |
| 9985 | merge | 10 | 4 | <code>&quot;\n중간에&quot;</code> | <code>0a ec a4 91 ea b0 84 ec 97 90</code> | contains_whitespace, control_char |
| 9986 | merge | 10 | 4 | <code>&quot; 최근에&quot;</code> | <code>20 ec b5 9c ea b7 bc ec 97 90</code> | contains_whitespace |
| 9987 | merge | 4 | 2 | <code>&quot;\n생&quot;</code> | <code>0a ec 83 9d</code> | contains_whitespace, control_char |
| 9988 | merge | 10 | 4 | <code>&quot; 제니퍼&quot;</code> | <code>20 ec a0 9c eb 8b 88 ed 8d bc</code> | contains_whitespace |
| 9989 | merge | 6 | 2 | <code>&quot;다크&quot;</code> | <code>eb 8b a4 ed 81 ac</code> | - |
| 9990 | merge | 13 | 5 | <code>&quot; 파워레인&quot;</code> | <code>20 ed 8c 8c ec 9b 8c eb a0 88 ec 9d b8</code> | contains_whitespace |
| 9991 | merge | 3 | 1 | <code>&quot;밑&quot;</code> | <code>eb b0 91</code> | - |
| 9992 | merge | 7 | 3 | <code>&quot; 낚였&quot;</code> | <code>20 eb 82 9a ec 98 80</code> | contains_whitespace |
| 9993 | merge | 7 | 3 | <code>&quot; 옆에&quot;</code> | <code>20 ec 98 86 ec 97 90</code> | contains_whitespace |
| 9994 | merge | 8 | 4 | <code>&quot; 영화~&quot;</code> | <code>20 ec 98 81 ed 99 94 7e</code> | contains_whitespace |
| 9995 | merge | 6 | 2 | <code>&quot;쥬얼&quot;</code> | <code>ec a5 ac ec 96 bc</code> | - |
| 9996 | merge | 4 | 2 | <code>&quot;\n쓸&quot;</code> | <code>0a ec 93 b8</code> | contains_whitespace, control_char |
| 9997 | merge | 6 | 2 | <code>&quot;니스&quot;</code> | <code>eb 8b 88 ec 8a a4</code> | - |
| 9998 | merge | 9 | 3 | <code>&quot;라는거&quot;</code> | <code>eb 9d bc eb 8a 94 ea b1 b0</code> | - |
| 9999 | merge | 10 | 4 | <code>&quot;의 추억&quot;</code> | <code>ec 9d 98 20 ec b6 94 ec 96 b5</code> | contains_whitespace |
