


from collections import defaultdict
from typing import Tuple
from .Alignment import Alignment

class AlignmentRegister:
    def __init__(self):
        # read_id: list of alignments of the read
        self.alignments: dict[str, list[Alignment]] = defaultdict(list)
        
    def add(self, raw_alignment: list[str]) -> None:
        qname = raw_alignment[0]
        alignment = Alignment(
            qname=qname,
            qlen=int(raw_alignment[1]),
            rname=raw_alignment[5],
            aln_block=int(raw_alignment[10]),
            matches=int(raw_alignment[9]),
            mapq=int(raw_alignment[11])
        )
        self.alignments[qname].append(alignment)

    def get_entries(self) -> list[Tuple[str, list[Alignment]]]:
        return list(self.alignments.items())
