import pytest
import file_parsers as fp


def test_color_palette() -> None:
    with open("chapters/recursions_and_reductions/data/crayola.GPL") as f:
        res = fp.row_iter_gpl(f)
        print(res)
        name, cols, colors = fp.color_palette(*res)
    print(name, cols, colors)


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-vv", "-s"]))
