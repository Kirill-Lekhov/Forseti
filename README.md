# Forseti Language
The system for determining the compliance of the text with the specified rules

##How to install:
PyPi installation guide
```shell
pip install forseti-lang
```

##How to use:
```python
from forseti.execute import execute_condition

condition = "TRUE AND FALSE"
text = ""
execute_condition(condition, text)  # False
```

##Supported logic operators
### English
Below is a table of available logical operators and their description.

| Operator               | Description                                 | Priority |
|------------------------|---------------------------------------------|----------|
| ()                     | The conditions in quotes will be met first  | 0        |
| AND                    | Logical **AND**                             | 1        |
| AND NOT                | Logical **AND NOT**                         | 2        |
| OR                     | Logical **OR**                              | 3        |
| Atoms (TRUE and FALSE) | Minimum logical unit                        | 4        |

###Russian
Forseti was developed for the analysis of texts in Russian.
So, you can use:

| RU  | ENG |
|-----|-----|
| И   | AND |
| ИЛИ | OR  |

####Note
You can combine ru and eng operators.

##Supported functions
We really lacked a simple syntax (but regular expressions did not allow us to achieve this), so we created our own
functions!

| Function         | In Forseti | Description                                                | Priority |
|------------------|------------|------------------------------------------------------------|----------|
| f text length    | ll, lg     | Text length check function                                 | 5        |
| f words distance | wN, cN, N  | Checks whether the words are in the specified interval     | 6        |
| f words nearby   | nearby     | Checks the words that are next to another word             | 7        |
| f regex search   |            | Checks the occurrence of a regular expression in the text  | 8        |

###Explanations
* ll - length less
* lg - length great
* wN - word in distance 'N words'
* cN - word in distance 'N characters'
* N - alias of wN
* nearby - the word is nearby to the words (word1 |nearby word2 | word3 | word4)

####Notes
* All function starts with special symbol: "|". That's why we don't support it in regular expressions
* It is also forbidden to use the "-" symbol, it is used in the distance function
* The function of finding words at a distance will allow you to exclude constructions with a word at a distance,
for example:
```
condition - "hello |w1 -world"
text      - "Hello beautiful world!"
result    - False
```
* You cannot combine two functions in one expression
* Nearby only works in one direction
* Text length and word distance functions don't work with negative values

##Priority table

| Operator               | Description                                                | Priority |
|------------------------|------------------------------------------------------------|----------|
| ()                     | The conditions in quotes will be met first                 | 0        |
| AND                    | Logical **AND**                                            | 1        |
| AND NOT                | Logical **AND NOT**                                        | 2        |
| OR                     | Logical **OR**                                             | 3        |
| Atoms (TRUE and FALSE) | Minimum logical unit                                       | 4        |
| f text length          | Text length check function                                 | 5        |
| f words distance       | Checks whether the words are in the specified interval     | 6        |
| f words nearby         | Checks the words that are next to another word             | 7        |
| f regex search         | Checks the occurrence of a regular expression in the text  | 8        |
