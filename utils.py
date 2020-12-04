from termcolor import colored

colors = ['white']


def print_block(block, cur_color=0, level=0):
    if block.kind == 'EMPTY':
        return
    if block.value is not None:
        print(level * '  ', colored('( ', 'white'), block.kind.lower(),
              '\"' + block.ex_type.lower() + '\"' if block.ex_type is not None else '',
              block.value if block.value is not None else '', colored(') ', 'white'))
        if block.kind == 'FUNC_CALL':
            for node in block.op1:
                print_block(node, (cur_color + 1) % len(colors), level + 1)
        return
    print(level * '  ', colored('( ', colors[cur_color]), block.kind.lower(),
          '\"' + block.ex_type.lower() + '\"' if block.ex_type is not None else '',
          '\"' + block.cur_func + '\"' if block.cur_func is not None else '')

    if block.kind == 'FOR':
        for i in block.op1['vars']:
            print(level * '  ', colored('( ', 'white'), i.kind.lower(),
                  '\"' + i.ex_type.lower() + '\"' if i.ex_type is not None else '',
                  i.value if i.value is not None else '', colored(') ', 'white'))

        print(level * '  ', colored('( ', 'white'), block.op1['cond'].kind.lower(),
              '\"' + block.op1['cond'].ex_type.lower() + '\"' if block.op1['cond'].ex_type is not None else '',
              block.op1['cond'].value if block.op1['cond'].value is not None else '', colored(') ', 'white'))

        for i in block.op1['expr']:
            print(level * '  ', colored('( ', 'white'), i.kind.lower(),
                  '\"' + i.ex_type.lower() + '\"' if i.ex_type is not None else '',
                  i.value if i.value is not None else '', colored(') ', 'white'))

    else:
        if block.op1 is not None and block.kind != 'FUNC_CALL' and block.kind != 'FUNC':
            print_block(block.op1, (cur_color + 1) % len(colors), level + 1)
    if block.op2 is not None:
        print_block(block.op2, (cur_color + 1) % len(colors), level + 1)
    if block.op3 is not None:
        print_block(block.op3, (cur_color + 1) % len(colors), level + 1)

    print(level * '  ', colored(')', colors[cur_color]))



