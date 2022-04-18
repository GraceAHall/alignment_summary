


from dataclasses import dataclass

ignore_suffixes = [
    'contig', 'scaffold', 'complete', 'plasmid', 'chromosome'
]

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
    
    def get_strain_name(self) -> str:
        name_split = self.rname.split('_')
        if name_split[5] in ignore_suffixes or name_split[3] == 'sp.':
            return f'{name_split[2]} {name_split[3]} {name_split[4]}'
        return f'{name_split[2]} {name_split[3]} {name_split[4]} {name_split[5]}'
    
    def get_read_len(self) -> int:
        return self.qlen

    def get_align_block(self) -> float:
        return self.aln_block / self.qlen * 100
    
    def get_identity(self) -> float:
        return self.matches / self.aln_block * 100