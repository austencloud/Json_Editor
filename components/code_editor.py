
from PyQt5.Qsci import QsciScintilla, QsciLexerJSON
from PyQt5.QtCore import Qt

class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the JSON lexer for syntax highlighting
        lexer = QsciLexerJSON()
        self.setLexer(lexer)

        # Enable line numbers
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, 40)

        # Enable folding
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)

        # Set tab width
        self.setTabWidth(4)

        # Set UTF-8 encoding
        self.setUtf8(True)

        # Enable auto-completion
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionThreshold(1)

    def set_code(self, code):
        self.setText(code)

    def get_code(self):
        return self.text()
