"""
Contains the cobol code editor widget.

"""
from pyqode.cobol.widgets import CobolCodeEdit as CodeEditBase

from ...compilers import FileType, get_file_type
from ...settings import Settings


class CobolCodeEdit(CodeEditBase):
    @property
    def file_type(self):
        return get_file_type(self.file.path, self.file.encoding)

    @file_type.setter
    def file_type(self, ftype):
        Settings().set_file_type(self.file.path, ftype)
