


from dataclasses import dataclass


@dataclass
class Alignment:
    qname: str
    qlen: int
    rname: str
    aln_block: int
    matches: int
    mapq: int

    def get_species_name(self) -> str:
        name_split = self.rname.split('_')
        species = f'{name_split[2]} {name_split[3]}'
        return species
    
    def get_read_len(self) -> int:
        return self.qlen

    def get_align_block(self) -> float:
        return self.aln_block / self.qlen * 100
    
    def get_identity(self) -> float:
        return self.matches / self.aln_block * 100