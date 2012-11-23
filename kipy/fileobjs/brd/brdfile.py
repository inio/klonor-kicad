'''
Classes based on SchItem for parsing and rendering
top of .sch file.
'''
from .brditem import BrdItem

class BrdFile(BrdItem):
    _classinit = None

    def __init__(self, sourcefile=None):
        self.lib_info = []
        if sourcefile != None:
            self.sourcefile = sourcefile
            self.startparse(self, sourcefile.readlinetokens())


    def render(self, linelist):
        self.PCBNEW_BOARD.render(self, linelist)
        self.GENERAL.render(self, linelist)
        self.SHEETDESCR.render(self, linelist)
        self.SETUP.render(self, linelist)
        for item in self.items:
            item.render(linelist)
        self.EndBOARD.render(self, linelist)

    def __str__(self):
        result = []
        self.render(result)
        result.append('')
        return '\n'.join(result)
