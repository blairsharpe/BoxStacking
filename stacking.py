
def is_stackable(total_size, num_stacks):
    """Checks if the boxes are capable of being stacked evenly

        total_size (int): The sum of all the boxes size added together
        num_stacks (int): The number of stacks to make out of the boxes

    Returns:
        bool: True if stackable, False otherwise.
    """
    if total_size % num_stacks == 0:

        return True

    else:

        return False

def parse(stack_info):
    """Parses the string to find stack size and number of stacks to make

        stack_info (str): String containing stack size and # stacks to make

    Returns:
        tuple: Tuple returning total size, number of stacks, and box sizes
    """

    total_size = 0
    parsed = stack_info.split(" ")

    for number in parsed[1]:
        total_size += int(number)

    num_stacks = int(parsed[0])
    boxes = parsed[1]
    return (total_size, num_stacks, boxes)

def stack_boxes(total_size, num_stacks, boxes):
    """Stacks boxes evenly based on the requirements passed in

        total_size (int): The sum of all the boxes size added together
        num_stacks (int): The number of stacks to make out of the boxes
        boxes      (str): list of all the sizes of boxes

    Returns:
        bool: Returns True for success. False, otherwise.
    """
    # Create a list of integers for size of boxes with ascending order
    boxes = list(boxes)
    boxes = [int(box) for box in boxes]
    boxes.sort(reverse=True)

    # Go through one less than the amount of stacks needed
    # Because leftovers will be equal to the group size
    for number in range(0, num_stacks-1):

        # Reset the group size and the items in the stack
        group_size = int(total_size / num_stacks)
        stack = []

        for box in boxes:

            # Check if the boxes can fit, if so remove from boxes into stack
            if box <= group_size:

                stack.append(box)
                boxes.remove(box)
                group_size -= box

        print(stack)


    # The leftovers in the box will equal the group size
    print(boxes)

    return True

# String containing the the amount of stacks and all the size of each box
string = "4 064876318535318"

total_size, num_stacks, boxes = parse(string)

# Check if we can make x amount of stacks evenly
if is_stackable(total_size, num_stacks):

    stack_boxes(total_size, num_stacks, boxes)

else:

    print("\nThe boxes cannot be stacked evenly")

