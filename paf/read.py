


from startup.cli_args import Settings
from .AlignmentRegister import AlignmentRegister


def read_paf(context: Settings) -> AlignmentRegister:
    register = AlignmentRegister()
    with open(context.paf_path, 'r') as fp:
        line = fp.readline().strip('\n').split('\t')
        while line:
            if len(line) == 1 and line[0] == '':
                break
            register.add(line)
            line = fp.readline().strip('\n').split('\t')
    return register
