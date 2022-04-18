

from paf.Alignment import Alignment


class OrganismData:
    def __init__(self):
        self.num_primary_alignments: int = 0
        self.cum_identity: float = 0
        self.cum_block: float = 0

    def get_avg_identity(self) -> float:
        return self.cum_identity / self.num_primary_alignments
    
    def get_avg_block(self) -> float:
        return self.cum_block / self.num_primary_alignments


class Summary:
    def __init__(self):
        self.organism_data: dict[str, OrganismData] = {}

    def add_alignment_entry(self, organism_name: str, alignment: Alignment) -> None:
        # ensure entry for organism
        if organism_name not in self.organism_data:
            self.organism_data[organism_name] = OrganismData()
        
        # update organism data
        self.organism_data[organism_name].num_primary_alignments += 1
        self.organism_data[organism_name].cum_identity += alignment.get_identity()
        self.organism_data[organism_name].cum_block += alignment.get_align_block()
        print()