from src.example_package_nelskev import text_box

def test_text_box():
    # Test with default parameters
    result = text_box("Hello world", display=False)
    expected = (
        "***************\n"
        "* Hello world *\n"
        "***************"
    )
    assert result == expected

    # Test with custom width
    result = text_box("Hello world", width=20, display=False)
    expected = (
        "********************\n"
        "*     Hello world   *\n"
        "********************"
    )
    assert result == expected

    # Test with margin
    result = text_box("Hello world", margin=1, display=False)
    expected = (
        "\n"
        "***************\n"
        "* Hello world *\n"
        "***************\n"
    )
    assert result == expected