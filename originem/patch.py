
from dataclasses import dataclass

@dataclass
class PatchFile:
    """A patch file which can be applied to an `AbsoluteFile` to mutate it's contents
