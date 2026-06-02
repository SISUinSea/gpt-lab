# Invalid and Hard-To-Display Tokens

Showing up to 30 rows per section. See `tokens.csv` for the full table.

## Invalid UTF-8

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 132 | byte | 1 | 0 | <code>&lt;invalid utf-8: 80&gt;</code> | <code>80</code> | invalid_utf8 |
| 133 | byte | 1 | 0 | <code>&lt;invalid utf-8: 81&gt;</code> | <code>81</code> | invalid_utf8 |
| 134 | byte | 1 | 0 | <code>&lt;invalid utf-8: 82&gt;</code> | <code>82</code> | invalid_utf8 |
| 135 | byte | 1 | 0 | <code>&lt;invalid utf-8: 83&gt;</code> | <code>83</code> | invalid_utf8 |
| 136 | byte | 1 | 0 | <code>&lt;invalid utf-8: 84&gt;</code> | <code>84</code> | invalid_utf8 |
| 137 | byte | 1 | 0 | <code>&lt;invalid utf-8: 85&gt;</code> | <code>85</code> | invalid_utf8 |
| 138 | byte | 1 | 0 | <code>&lt;invalid utf-8: 86&gt;</code> | <code>86</code> | invalid_utf8 |
| 139 | byte | 1 | 0 | <code>&lt;invalid utf-8: 87&gt;</code> | <code>87</code> | invalid_utf8 |
| 140 | byte | 1 | 0 | <code>&lt;invalid utf-8: 88&gt;</code> | <code>88</code> | invalid_utf8 |
| 141 | byte | 1 | 0 | <code>&lt;invalid utf-8: 89&gt;</code> | <code>89</code> | invalid_utf8 |
| 142 | byte | 1 | 0 | <code>&lt;invalid utf-8: 8a&gt;</code> | <code>8a</code> | invalid_utf8 |
| 143 | byte | 1 | 0 | <code>&lt;invalid utf-8: 8b&gt;</code> | <code>8b</code> | invalid_utf8 |
| 144 | byte | 1 | 0 | <code>&lt;invalid utf-8: 8c&gt;</code> | <code>8c</code> | invalid_utf8 |
| 145 | byte | 1 | 0 | <code>&lt;invalid utf-8: 8d&gt;</code> | <code>8d</code> | invalid_utf8 |
| 146 | byte | 1 | 0 | <code>&lt;invalid utf-8: 8e&gt;</code> | <code>8e</code> | invalid_utf8 |
| 147 | byte | 1 | 0 | <code>&lt;invalid utf-8: 8f&gt;</code> | <code>8f</code> | invalid_utf8 |
| 148 | byte | 1 | 0 | <code>&lt;invalid utf-8: 90&gt;</code> | <code>90</code> | invalid_utf8 |
| 149 | byte | 1 | 0 | <code>&lt;invalid utf-8: 91&gt;</code> | <code>91</code> | invalid_utf8 |
| 150 | byte | 1 | 0 | <code>&lt;invalid utf-8: 92&gt;</code> | <code>92</code> | invalid_utf8 |
| 151 | byte | 1 | 0 | <code>&lt;invalid utf-8: 93&gt;</code> | <code>93</code> | invalid_utf8 |
| 152 | byte | 1 | 0 | <code>&lt;invalid utf-8: 94&gt;</code> | <code>94</code> | invalid_utf8 |
| 153 | byte | 1 | 0 | <code>&lt;invalid utf-8: 95&gt;</code> | <code>95</code> | invalid_utf8 |
| 154 | byte | 1 | 0 | <code>&lt;invalid utf-8: 96&gt;</code> | <code>96</code> | invalid_utf8 |
| 155 | byte | 1 | 0 | <code>&lt;invalid utf-8: 97&gt;</code> | <code>97</code> | invalid_utf8 |
| 156 | byte | 1 | 0 | <code>&lt;invalid utf-8: 98&gt;</code> | <code>98</code> | invalid_utf8 |
| 157 | byte | 1 | 0 | <code>&lt;invalid utf-8: 99&gt;</code> | <code>99</code> | invalid_utf8 |
| 158 | byte | 1 | 0 | <code>&lt;invalid utf-8: 9a&gt;</code> | <code>9a</code> | invalid_utf8 |
| 159 | byte | 1 | 0 | <code>&lt;invalid utf-8: 9b&gt;</code> | <code>9b</code> | invalid_utf8 |
| 160 | byte | 1 | 0 | <code>&lt;invalid utf-8: 9c&gt;</code> | <code>9c</code> | invalid_utf8 |
| 161 | byte | 1 | 0 | <code>&lt;invalid utf-8: 9d&gt;</code> | <code>9d</code> | invalid_utf8 |

## Control Characters

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

## Whitespace Tokens

| id | kind | byte_len | char_len | token | hex | flags |
| --- | --- | --- | --- | --- | --- | --- |
| 13 | byte | 1 | 1 | <code>&quot;\t&quot;</code> | <code>09</code> | contains_whitespace, control_char |
| 14 | byte | 1 | 1 | <code>&quot;\n&quot;</code> | <code>0a</code> | contains_whitespace, control_char |
| 15 | byte | 1 | 1 | <code>&quot;\u000b&quot;</code> | <code>0b</code> | contains_whitespace, control_char |
| 16 | byte | 1 | 1 | <code>&quot;\f&quot;</code> | <code>0c</code> | contains_whitespace, control_char |
| 17 | byte | 1 | 1 | <code>&quot;\r&quot;</code> | <code>0d</code> | contains_whitespace, control_char |
| 32 | byte | 1 | 1 | <code>&quot;\u001c&quot;</code> | <code>1c</code> | contains_whitespace, control_char |
| 33 | byte | 1 | 1 | <code>&quot;\u001d&quot;</code> | <code>1d</code> | contains_whitespace, control_char |
| 34 | byte | 1 | 1 | <code>&quot;\u001e&quot;</code> | <code>1e</code> | contains_whitespace, control_char |
| 35 | byte | 1 | 1 | <code>&quot;\u001f&quot;</code> | <code>1f</code> | contains_whitespace, control_char |
| 36 | byte | 1 | 1 | <code>&quot; &quot;</code> | <code>20</code> | contains_whitespace |
| 305 | merge | 7 | 3 | <code>&quot; 영화&quot;</code> | <code>20 ec 98 81 ed 99 94</code> | contains_whitespace |
| 311 | merge | 2 | 2 | <code>&quot;.\n&quot;</code> | <code>2e 0a</code> | contains_whitespace, control_char |
| 322 | merge | 4 | 2 | <code>&quot; 이&quot;</code> | <code>20 ec 9d b4</code> | contains_whitespace |
| 349 | merge | 4 | 2 | <code>&quot; 아&quot;</code> | <code>20 ec 95 84</code> | contains_whitespace |
| 357 | merge | 4 | 2 | <code>&quot; 보&quot;</code> | <code>20 eb b3 b4</code> | contains_whitespace |
| 359 | merge | 4 | 2 | <code>&quot; 그&quot;</code> | <code>20 ea b7 b8</code> | contains_whitespace |
| 388 | merge | 5 | 3 | <code>&quot;다.\n&quot;</code> | <code>eb 8b a4 2e 0a</code> | contains_whitespace, control_char |
| 402 | merge | 4 | 2 | <code>&quot;다\n&quot;</code> | <code>eb 8b a4 0a</code> | contains_whitespace, control_char |
| 406 | merge | 4 | 2 | <code>&quot; 좋&quot;</code> | <code>20 ec a2 8b</code> | contains_whitespace |
| 408 | merge | 4 | 2 | <code>&quot; 나&quot;</code> | <code>20 eb 82 98</code> | contains_whitespace |
| 409 | merge | 4 | 2 | <code>&quot; 없&quot;</code> | <code>20 ec 97 86</code> | contains_whitespace |
| 411 | merge | 4 | 2 | <code>&quot; 하&quot;</code> | <code>20 ed 95 98</code> | contains_whitespace |
| 416 | merge | 4 | 2 | <code>&quot; 다&quot;</code> | <code>20 eb 8b a4</code> | contains_whitespace |
| 430 | merge | 4 | 2 | <code>&quot; 정&quot;</code> | <code>20 ec a0 95</code> | contains_whitespace |
| 431 | merge | 4 | 2 | <code>&quot; 있&quot;</code> | <code>20 ec 9e 88</code> | contains_whitespace |
| 446 | merge | 4 | 2 | <code>&quot; 연&quot;</code> | <code>20 ec 97 b0</code> | contains_whitespace |
| 452 | merge | 7 | 3 | <code>&quot; 너무&quot;</code> | <code>20 eb 84 88 eb ac b4</code> | contains_whitespace |
| 455 | merge | 4 | 2 | <code>&quot; 어&quot;</code> | <code>20 ec 96 b4</code> | contains_whitespace |
| 458 | merge | 4 | 2 | <code>&quot; 만&quot;</code> | <code>20 eb a7 8c</code> | contains_whitespace |
| 461 | merge | 7 | 3 | <code>&quot; 재미&quot;</code> | <code>20 ec 9e ac eb af b8</code> | contains_whitespace |
