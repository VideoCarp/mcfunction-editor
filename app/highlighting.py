
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
print("Syntax Highlighter imported.")
def format(color, style=''):
    # color formatter
    _color = QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages

STYLES = {
    'keyword': format([65, 173, 209], 'italic'), # light blue
    'operator': format([52, 125, 235]), # cobalt (almost)
    'brace': format([114,137,218]), # tomato
    'string': format([216, 219, 42]), # yellow
    'string2': format([123, 173, 29]), # olive
    'comment': format([100, 100, 100], 'italic'), # gray/grey
    'numbers': format([188, 66, 245]), # magenta
}


class MCFunction(QSyntaxHighlighter):

    #######################
    #    IMPORTANT:       #
    # regex works on the  #
    # words. escape them. #
    #######################
    keywords = [
        "execute", "tag", "testforblock", "setblock", "fill",
        "effect", "teleport", "summon", "clear", "give", "tellraw", "title",
        "particle", "scoreboard", "testfor", "tickingarea", "add", "remove",
        "gamerule", "true", "false", "tp", "type", "name", "if", "data", "datapack", "function"
    ]

    # operators
    operators = [
       "=", "!", ">", "<", r"\^", "\~"
    ]

    braces = [
        "\{", "\[", "\]", "\}", "\="
    ]
    

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)
        rules = []

        # Keyword, operator, and brace rules
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                  for w in MCFunction.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in MCFunction.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                  for b in MCFunction.braces]

        # All other rules
        rules += [

            (r"\@e|\@s|\@r|\@p|\@a|\+|\-", 0, STYLES['numbers']), # target selectors
            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),


            # From '#' until a newline

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
            (r'#[^\n]*', 0, STYLES['comment']),
        ]
        print("Done ruleset.")

        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]
    def highlightBlock(self, text):
        # apply syntax highlighting
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                #
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
