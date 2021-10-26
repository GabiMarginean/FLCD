import re

INTEGER_REG = re.compile(r"^[-+]?[0-9]+$")
CHAR_REG    = re.compile(r"[a-zA-Z0-9]$")
STR_REG     = re.compile(r'"(.*?)"')
BOOL_REG    = re.compile(r"(?i)^(true|false)$")

CONST_REG_LIST = [INTEGER_REG, CHAR_REG, STR_REG, BOOL_REG]

ID_REG = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]*$')

LINE_COMM_REG  = re.compile(r'^\$.*$')
MLINE_COMM_REG = re.compile(r'^.*-\$$')
COMM_REG_LIST  = [LINE_COMM_REG, MLINE_COMM_REG]
