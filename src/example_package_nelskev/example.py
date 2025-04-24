def text_box(text, icon='*', width: int=None, margin : int=None, outside_margin : int=None, display : bool=False):
    output = []

    def add_line():
        if (len(icon) > 1):
            # print(icon * int(width / len(icon)))
            output.append(icon * int(width / len(icon)))
        else:
            # print(icon * width)
            output.append(icon * width)
    """
    Prints the given text in a centered area surrounded by a box of icons.

    Arguments:
        text (str): The text to be printed.
        icon (str, optional): The icon to be used for the box. Default: '*'.
        width (int, optional): The width of the box. If not provided, the width will be automatically calculated based on the text length. Default: Length of longest line + 4
        margin (int, optional): Adds empty lines to top and bottom of text inside of box. Default: 1
        outside_margin (int, optional): Adds empty lines to top of bottom outside of box. Default: None
        display (bool, optional): Prints output along with returning it. Default: False

    Return values:
        output
    """

   
    # Calculate the width of the box if not provided
    if width is None:
        width = len(max(text.split('\n'), key=len)) + 4

    # Add the top border of the box
    add_line()

    # Split text based on new lines
    lines = text.split('\n')

    # Adds empty string to top and bottom per number for margin (default: 1)
    if margin:
        for _ in range(margin):
            lines.insert(0, "")
            lines.append("")
    if margin == None:
        lines.insert(0, "")
        lines.append("")

    # Print each line of text centered in the box
    for line in lines:
        # print(icon[0] + line.center(width - 2) + icon[0])
        output.append(icon[0] + line.center(width - 2) + icon[0])

    # Print the bottom border of the box
    add_line()

    # Checks for outside margin and adds top and bottom lines accordingly if they have value
    if outside_margin:
        for _ in range(outside_margin):
            output.insert(0, "")
            output.append("")

  

    # Displays each line if display is expected
    if (display==True):
        for line_item in output:
            print(line_item)


    # Creates new string for value to be returned
    output_text = ""

    # Builds output text to be returned
    for line_item in output[:-1]:
        output_text += line_item + "\n"
    output_text += output[-1]
    return output_text




# if __name__ == "__main__":
#     # text_box("Hello world", display=True)


#     new_text_box = text_box("Hello world", display=True, outside_margin=2, margin=0 )
#     print(new_text_box)
    
    
