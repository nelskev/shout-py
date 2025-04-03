from src.example_package_nelskev import example



def test_text_box():
    # Test with default parameters
    result = example.text_box("Hello world", margin=0, display=False)
    expected = (
        "***************\n"
        "* Hello world *\n"
        "***************"
    )
    assert result == expected

    # Test with custom width
    result = example.text_box("Hello world", width=20, margin=0, display=False)
    expected = (
        "********************\n"
        "*   Hello world    *\n"
        "********************"
    )
    assert result == expected

    # Test with margin
    result = example.text_box("Hello world", margin=1, display=False)
    expected = (
        "***************\n"
        "*             *\n"
        "* Hello world *\n"
        "*             *\n"
        "***************"
    )
    assert result == expected

