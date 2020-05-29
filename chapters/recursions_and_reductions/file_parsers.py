from typing import Optional, Text, Callable, List, NamedTuple, TextIO, Tuple, Iterator
import re

def row_iter_csv(source: TextIO) :
    return csv.reader(source, delimiter="\t")


def float_none(data: Optional[Text]) -> Optional[float]:
    try:
        data_f = float(data)
        return data_f
    except ValueError:
        return None


R_Text = List[Optional[Text]]
R_Float = List[Optional[float]]
float_row: Callable[[R_Text], R_Float] = lambda row: list(map(float_none, row))

all_numeric : Callable[[R_Float], bool] = lambda row: all(row) and len(row) == 8


"""
Parsing .GPL (Gimp Palette files)
"""
Head_Body = Tuple[Tuple[str, str], Iterator[List[str]]]

def row_iter_gpl(file_obj: TextIO) -> Head_Body:
    header_pat = re.compile(
        r"GIMP Palette\nName:\s*.(.*?)\nColumns:\s*(.*?)\n#\n",
        re.M
    )

    def read_head(file_obj: TextIO) -> Tuple[Tuple[str, str], TextIO]:

        match = header_pat.match(
            "".join(file_obj.readline() for _ in range(4))
        )

        return (match.group(1), match.group(2)), file_obj

    def read_tail(headers: Tuple[str, str], file_obj: TextIO) -> Head_Body:
        return ( headers, (next_line.split() for next_line in file_obj))

    return read_tail(*read_head(file_obj))


class Color(NamedTuple):
    red: int
    blue: int
    green: int
    name: str


def color_palette(
        headers: Tuple[str, str],
        row_iter: Iterator[List[str]]
        ) -> Tuple[str, str, Tuple[Color, ...]]:
        name, columns = headers
        colors = tuple(
            Color(int(r), int(g), int(b), " ".join(name))
            for r, g, b, *name in row_iter)

        return name, columns, colors
