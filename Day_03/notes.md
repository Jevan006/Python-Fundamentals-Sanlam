# Python - Day 03

- Operators 2
- String methods
  - `count()`
  - `find()`
  - `index()`
- List
- List methods

## Shortcuts

- `Alt + ⬆️` ➡️ For moving lines
- `!<tab>` ➡️ Boiler plate code
- `win + .` ➡️ emojis
- `Ctrl + /` ➡️ comment
- `ctrl + <space>` ➡️ auto complete
- `ctrl + d` ➡️ multi cursor (similar)
- `hold alt` ➡️ multi cursor (similar)

## fstring - DX⬆️

- `{}`➡️ interpolation(substitution)
- `{}`➡️ expressions are alowed
- Auto converts
- Readable

```py
print(f"My age is {age}")
print(f"She has {2 * 1000} followers🎉")
```

## Operators 🔢

- Floor Division
  ```py
  floor = 7 // 3
  ```
- Exponention
  ```py
  exponent = 2 ** 3
  ```
- Modulus
  ```py
  mod = 3 % 2
  ```

## Adding image

![alt text](image-1.png)

## MORE

- \*\* between words - bold
- - between words - italics
- 3 (or more) hyphens makes a line ---

## References

- [markdown sheet](https://chatgpt.com/c/67b57b9a-546c-8011-b0ac-87d0a08980a2)
-

## Colons can be used to align columns.

## colon on right is for right alignment

| Tables            |    Cool |
| ----------------- | ------: |
| `True and True`   |  `True` |
| `True and False`  | `False` |
| `False and True`  | `False` |
| `False and False` | `False` |

## There must be at least 3 dashes separating each header cell.

## The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

| Markdown | Less      | Pretty     |
| -------- | --------- | ---------- |
| _Still_  | `renders` | **nicely** |
| 1        | 2         | 3          |

> All comparison operators and logical operators return `boolean`

## `and`

- If any is `False` then `False`
- Only both `True` then `True`

| Operator          |  Output |
| ----------------- | ------: |
| `True and True`   |  `True` |
| `True and False`  | `False` |
| `False and True`  | `False` |
| `False and False` | `False` |

## `or`

- If any is `True` then `True`
- Only both `False` then `False`

| Operator         |  Output |
| ---------------- | ------: |
| `True or True`   |  `True` |
| ` True or False` |  `True` |
| `False or True`  |  `True` |
| `False or False` | `False` |

```
>>> (3 < 4) and (10 >= 5)
True
>>> (5 != 10) or (800 < 5)
True
>>> ( (80 % 5) == 0) and ( (3 * 6) == 35)
False
>>> ( 7 > 5 ) and (4 != 4 ) or (3 <= 10)
True
>>>

```
