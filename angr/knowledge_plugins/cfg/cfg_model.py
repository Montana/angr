
import networkx


class CFGModel:
    """
    This class describes a Control Flow Graph for a specific range of code.
    """

    def __init__(self):

        # The graph
        self.graph = networkx.DiGraph()

        # Jump tables
        self.jump_tables = { }

        # Memory references
        # A mapping between address and the actual data in memory
        self.memory_data = { }
        # A mapping between address of the instruction that's referencing the memory data and the memory data itself
        self.insn_addr_to_memory_data = { }
