import pdb


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
        None (TBD?)
    """
    boxes = list(boxes)
    boxes = [int(box) for box in boxes]
    boxes.sort(reverse=True)

    for number in range(0, num_stacks-1):

        group_size = int(total_size / num_stacks)
        stack = []

        for box in boxes:

            if box <= group_size:

                stack.append(box)
                boxes.remove(box)
                group_size -= box

        print(stack)

    print(boxes)

    return True

# String containing the the amount of stacks and all the size of each box
string = "4 064876318535318"

total_size, num_stacks, boxes = parse(string)

print("\nstack #: {}".format(num_stacks))
print("total stack: {}".format(total_size))

# Check if we can make x amount of stacks evenly
if is_stackable(total_size, num_stacks):

    print("\nIt's stackable")
    stack_boxes(total_size, num_stacks, boxes)

else:

    print("\nnot stackable")

print("\n")

