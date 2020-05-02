from collections import namedtuple
from functions_iterators_generators import static_mapping
import pytest

Color = namedtuple("Color", ("red", "green", "blue", "name"))


SEQUENCE = (Color(red=239, green=222, blue=205, name="Almond"),
            Color(red=205, green=149, blue=117, name="Antique Brass"),
            Color(red=253, green=217, blue=181, name="Apricot"),
            Color(red=197, green=227, blue=132, name="Yellow Green"),
            Color(red=255, green=174, blue=66, name="Yellow Orange")
        )

SEQ = [(c.name, c) for c in SEQUENCE]
name_map = dict(SEQ)

print(SEQ)
print(type(SEQ))
def test_mapping():
    for n,c in SEQ:
        print(n, c)

    static_map = static_mapping.StaticMapping(SEQ)

    for c in SEQUENCE:
        assert(static_map[c.name] == name_map[c.name])


def test_value_error():
    static_map = static_mapping.StaticMapping(SEQ)

    with pytest.raises(ValueError):
        static_map["asd"]


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v"]))

