from termcolor import colored

colors = ['red', 'blue', 'yellow', 'green', 'cyan']


def print_block(block, cur_color=0, level=0):
    if block.kind == 'EMPTY':
        return
    if block.value is not None:
        print(level * '\t', colored('( ', 'magenta'), block.kind,
              '\"' + block.ex_type + '\"' if block.ex_type is not None else '',
              block.value if block.value is not None else '', colored(') ', 'magenta'))
        return
    print(level * '\t', colored('[ ', colors[cur_color]),
          '\"' + block.ex_type + '\"' if block.ex_type is not None else '', block.kind)

    if block.op1 is not None:
        print_block(block.op1, (cur_color + 1) % len(colors), level + 1)
    if block.op2 is not None:
        print_block(block.op2, (cur_color + 1) % len(colors), level + 1)
    if block.op3 is not None:
        print_block(block.op3, (cur_color + 1) % len(colors), level + 1)

    print(level * '\t', colored(']', colors[cur_color]))
