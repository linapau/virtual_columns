import re
import pandas

LABEL_PATTERN = re.compile(r'^[a-zA-Z_]+$')
ROLE_PATTERN = re.compile(r'^([a-zA-Z_]+)\s*([+\-*])\s*([a-zA-Z_]+)$')


def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    # check if the new column name is valid (only letters and underscores)
    if not LABEL_PATTERN.match(new_column):
        return pandas.DataFrame([])
    
    # make sure all existing columns in the dataframe follow the naming rules
    # if not, return empty dataframe
    if not all(LABEL_PATTERN.fullmatch(col) for col in df.columns):
        return pandas.DataFrame([])

    # remove extra spaces
    role = role.strip()

    # try to split the expression into: column1 operator column2
    match = ROLE_PATTERN.match(role)
    if not match:
        return pandas.DataFrame([])

    col1, operator, col2 = match.group(1).strip(), match.group(2), match.group(3).strip()

    # extra safety check for column name validity (redundant due to regex)
    if not LABEL_PATTERN.match(col1) or not LABEL_PATTERN.match(col2):
        return pandas.DataFrame([])

    # check if columns exist in dataframe
    if col1 not in df.columns or col2 not in df.columns:
        return pandas.DataFrame([])

    # perform operation
    operations = {
        '+': df[col1] + df[col2],
        '-': df[col1] - df[col2],
        '*': df[col1] * df[col2]
    }

    # return new dataframe with added column (no mutation)
    return df.assign(**{new_column: operations[operator]})
