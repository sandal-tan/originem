"""Create a file from the original and patches."""

import os
from filecmp import cmp as compare_files # Seriously? Linter complains about fp but we get this in the standard library
from typing import Optional, Any

from dataclasses import dataclass

@dataclass(eq=False)
class AbsoluteFile:
    """An file that cannot be modified unless patched.

    Args:
        path: The path of the file

    """

    path: str
    _contents: Optional[str] = None

    def __post_init__(self):
        self.path = os.path.expanduser(self.path)
        if self._contents is None:
            with open(self.path) as _fp:
                self._contents = _fp.read()

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, AbsoluteFile):
            return compare_files(self.path, other.path)
        return False

    def apply_patch(self, patch_file: str) -> str:
        """Apply a patch file to an absolute file, thus modifying modifying the underlying contents for a user.

        The patched contents are returned to the user without modifying the absolute file representation.

        Args:
            patch_file: The path of patch file

        Returns:
            The patched contents of the file

        """
        with open(os.path.expanduser(patch_file)) as _fp:
           contents = _fp.read()

