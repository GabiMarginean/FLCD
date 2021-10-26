# Lexical Analyzer

> Analyzes the source code and outputs the `sybmol table`, the `program information file` and prints the syntax errors if any.

## Interface

- `LexicalAnalyzer(token_file, separators_file)`

  The constructor takes the path to the file containing the tokens and another file containing the separators, all separated by a new line.

- `analyze(input_file)`

  This method is used to analyze `input_file` and will output two files:

  - `ST.out` containing the `symbol table`

  - `PIF.out`containing the `program information file`

    

  > If any syntax error occur, those will be printed on the console in the form of:
  >
  > `Syntax Error: line 7 at: 'int@'`
  >
  > Otherwise the method will print `Lexically correct`



## Regexes

#### Constants

- Integer:  `^[-+]?[0-9]+$`

  > This matches any string that may begin with a `+` or a `-` followed by one or more digits

- Character: `[a-zA-Z0-9]$`

  > This matches any string that contains only letters from `a-z`, `A-Z`and digits

- String: `"(.*?)"`

  > This matches anything that is between two `"`

- Boolean: `"(?i)^(true|false)$`

  > This matches either `true` or `false`, ignoring the case

#### Identifier: `^[_a-zA-Z][_a-zA-Z0-9]*$`

> This matches any string that starts with either letters from `a-z`, `A-Z`or `_` and further 		contains only those characters or digits

#### Comment Lines

- Beggining of one line / multiple line comment: `^\$.*$`

  > This matches any line that starts with `$`

- Ending of multiple line comment: `^.*-\$$`

  > This matches any line that ends with `-$`

