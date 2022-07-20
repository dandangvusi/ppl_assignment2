# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u01b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\2\3\3")
        buf.write("\5\3j\n\3\3\4\3\4\3\4\3\4\5\4p\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6|\n\6\3\7\3\7\5\7\u0080\n\7\3")
        buf.write("\b\3\b\3\b\5\b\u0085\n\b\3\t\3\t\3\t\3\t\5\t\u008b\n\t")
        buf.write("\3\n\5\n\u008e\n\n\3\13\3\13\3\13\3\13\5\13\u0094\n\13")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u009a\n\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00a7\n\16\3\17\3\17\3")
        buf.write("\17\5\17\u00ac\n\17\3\20\3\20\3\20\5\20\u00b1\n\20\3\20")
        buf.write("\3\20\3\20\3\21\5\21\u00b7\n\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00bf\n\22\3\23\3\23\3\23\3\23\5\23\u00c5")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u00d0\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u00d9")
        buf.write("\n\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00e3")
        buf.write("\n\27\3\27\5\27\u00e6\n\27\3\27\3\27\5\27\u00ea\n\27\5")
        buf.write("\27\u00ec\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00f5\n\30\3\31\3\31\3\31\3\31\5\31\u00fb\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0109\n\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0112\n\33\3\33\3\33\3\33\3\34\3\34\5\34\u0119\n\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\5\37\u0129\n\37\3\37\3\37\3\37\3 \3 \5")
        buf.write(" \u0130\n \3 \3 \3!\3!\3!\3!\3!\5!\u0139\n!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u0141\n\"\f\"\16\"\u0144\13\"\3#\3")
        buf.write("#\3#\3#\3#\3#\7#\u014c\n#\f#\16#\u014f\13#\3$\3$\3$\3")
        buf.write("$\3$\3$\7$\u0157\n$\f$\16$\u015a\13$\3%\3%\3%\5%\u015f")
        buf.write("\n%\3&\3&\3&\3&\5&\u0165\n&\3\'\3\'\5\'\u0169\n\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0176\n(\3)\3)\5)\u017a")
        buf.write("\n)\3*\3*\3*\3*\3*\3*\5*\u0182\n*\3+\3+\3+\5+\u0187\n")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\5,\u0190\n,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u0199\n-\3.\3.\3.\3.\5.\u019f\n.\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u01ae\n")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01b6\n\62\3\62")
        buf.write("\2\5BDF\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\b\3\2%/\3\2")
        buf.write("\61\62\4\2\34\35!\"\4\2\36 #$\4\2\35\35\"\"\3\2\3\5\2")
        buf.write("\u01c4\2d\3\2\2\2\4i\3\2\2\2\6o\3\2\2\2\bq\3\2\2\2\n{")
        buf.write("\3\2\2\2\f\177\3\2\2\2\16\u0081\3\2\2\2\20\u0086\3\2\2")
        buf.write("\2\22\u008d\3\2\2\2\24\u0093\3\2\2\2\26\u0095\3\2\2\2")
        buf.write("\30\u009d\3\2\2\2\32\u00a6\3\2\2\2\34\u00ab\3\2\2\2\36")
        buf.write("\u00ad\3\2\2\2 \u00b6\3\2\2\2\"\u00be\3\2\2\2$\u00c4\3")
        buf.write("\2\2\2&\u00cf\3\2\2\2(\u00d1\3\2\2\2*\u00d8\3\2\2\2,\u00de")
        buf.write("\3\2\2\2.\u00f4\3\2\2\2\60\u00f6\3\2\2\2\62\u00fc\3\2")
        buf.write("\2\2\64\u010d\3\2\2\2\66\u0116\3\2\2\28\u011f\3\2\2\2")
        buf.write(":\u0122\3\2\2\2<\u0125\3\2\2\2>\u012d\3\2\2\2@\u0138\3")
        buf.write("\2\2\2B\u013a\3\2\2\2D\u0145\3\2\2\2F\u0150\3\2\2\2H\u015e")
        buf.write("\3\2\2\2J\u0164\3\2\2\2L\u0168\3\2\2\2N\u0175\3\2\2\2")
        buf.write("P\u0179\3\2\2\2R\u0181\3\2\2\2T\u0183\3\2\2\2V\u018f\3")
        buf.write("\2\2\2X\u0198\3\2\2\2Z\u019e\3\2\2\2\\\u01a0\3\2\2\2^")
        buf.write("\u01a4\3\2\2\2`\u01ad\3\2\2\2b\u01b5\3\2\2\2de\5\4\3\2")
        buf.write("ef\5\22\n\2fg\7\2\2\3g\3\3\2\2\2hj\5\6\4\2ih\3\2\2\2i")
        buf.write("j\3\2\2\2j\5\3\2\2\2kl\5\b\5\2lm\5\6\4\2mp\3\2\2\2np\5")
        buf.write("\b\5\2ok\3\2\2\2on\3\2\2\2p\7\3\2\2\2qr\7\31\2\2rs\7;")
        buf.write("\2\2st\5\n\6\2tu\7:\2\2u\t\3\2\2\2vw\5\f\7\2wx\7<\2\2")
        buf.write("xy\5\n\6\2y|\3\2\2\2z|\5\f\7\2{v\3\2\2\2{z\3\2\2\2|\13")
        buf.write("\3\2\2\2}\u0080\5\16\b\2~\u0080\5\20\t\2\177}\3\2\2\2")
        buf.write("\177~\3\2\2\2\u0080\r\3\2\2\2\u0081\u0084\7>\2\2\u0082")
        buf.write("\u0083\7\63\2\2\u0083\u0085\5X-\2\u0084\u0082\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0085\17\3\2\2\2\u0086\u0087\7>\2")
        buf.write("\2\u0087\u008a\5Z.\2\u0088\u0089\7\63\2\2\u0089\u008b")
        buf.write("\5^\60\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\21\3\2\2\2\u008c\u008e\5\24\13\2\u008d\u008c\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\23\3\2\2\2\u008f\u0090\5\26")
        buf.write("\f\2\u0090\u0091\5\24\13\2\u0091\u0094\3\2\2\2\u0092\u0094")
        buf.write("\5\26\f\2\u0093\u008f\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\25\3\2\2\2\u0095\u0096\7\24\2\2\u0096\u0097\7;\2\2\u0097")
        buf.write("\u0099\7>\2\2\u0098\u009a\5\30\r\2\u0099\u0098\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\5")
        buf.write("\36\20\2\u009c\27\3\2\2\2\u009d\u009e\7\26\2\2\u009e\u009f")
        buf.write("\7;\2\2\u009f\u00a0\5\32\16\2\u00a0\31\3\2\2\2\u00a1\u00a2")
        buf.write("\5\34\17\2\u00a2\u00a3\7<\2\2\u00a3\u00a4\5\32\16\2\u00a4")
        buf.write("\u00a7\3\2\2\2\u00a5\u00a7\5\34\17\2\u00a6\u00a1\3\2\2")
        buf.write("\2\u00a6\u00a5\3\2\2\2\u00a7\33\3\2\2\2\u00a8\u00ac\7")
        buf.write(">\2\2\u00a9\u00aa\7>\2\2\u00aa\u00ac\5Z.\2\u00ab\u00a8")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\35\3\2\2\2\u00ad\u00ae")
        buf.write("\7\t\2\2\u00ae\u00b0\7;\2\2\u00af\u00b1\5 \21\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b3\7\17\2\2\u00b3\u00b4\7=\2\2\u00b4\37\3\2")
        buf.write("\2\2\u00b5\u00b7\5\"\22\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\5$\23\2\u00b9")
        buf.write("!\3\2\2\2\u00ba\u00bb\5(\25\2\u00bb\u00bc\5\"\22\2\u00bc")
        buf.write("\u00bf\3\2\2\2\u00bd\u00bf\5(\25\2\u00be\u00ba\3\2\2\2")
        buf.write("\u00be\u00bd\3\2\2\2\u00bf#\3\2\2\2\u00c0\u00c1\5&\24")
        buf.write("\2\u00c1\u00c2\5$\23\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5")
        buf.write("\5&\24\2\u00c4\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("%\3\2\2\2\u00c6\u00d0\5*\26\2\u00c7\u00d0\5,\27\2\u00c8")
        buf.write("\u00d0\5\62\32\2\u00c9\u00d0\5\64\33\2\u00ca\u00d0\5\66")
        buf.write("\34\2\u00cb\u00d0\58\35\2\u00cc\u00d0\5:\36\2\u00cd\u00d0")
        buf.write("\5<\37\2\u00ce\u00d0\5> \2\u00cf\u00c6\3\2\2\2\u00cf\u00c7")
        buf.write("\3\2\2\2\u00cf\u00c8\3\2\2\2\u00cf\u00c9\3\2\2\2\u00cf")
        buf.write("\u00ca\3\2\2\2\u00cf\u00cb\3\2\2\2\u00cf\u00cc\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\'\3\2\2")
        buf.write("\2\u00d1\u00d2\7\31\2\2\u00d2\u00d3\7;\2\2\u00d3\u00d4")
        buf.write("\5\n\6\2\u00d4\u00d5\7:\2\2\u00d5)\3\2\2\2\u00d6\u00d9")
        buf.write("\7>\2\2\u00d7\u00d9\5L\'\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\7\63\2\2\u00db")
        buf.write("\u00dc\5@!\2\u00dc\u00dd\7:\2\2\u00dd+\3\2\2\2\u00de\u00df")
        buf.write("\7\25\2\2\u00df\u00e0\5@!\2\u00e0\u00e2\7\30\2\2\u00e1")
        buf.write("\u00e3\5 \21\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e5\3\2\2\2\u00e4\u00e6\5.\30\2\u00e5\u00e4\3")
        buf.write("\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00eb\3\2\2\2\u00e7\u00e9")
        buf.write("\7\r\2\2\u00e8\u00ea\5 \21\2\u00e9\u00e8\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e7\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\7")
        buf.write("\20\2\2\u00ee\u00ef\7=\2\2\u00ef-\3\2\2\2\u00f0\u00f1")
        buf.write("\5\60\31\2\u00f1\u00f2\5.\30\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f5\5\60\31\2\u00f4\u00f0\3\2\2\2\u00f4\u00f3\3\2\2")
        buf.write("\2\u00f5/\3\2\2\2\u00f6\u00f7\7\16\2\2\u00f7\u00f8\5@")
        buf.write("!\2\u00f8\u00fa\7\30\2\2\u00f9\u00fb\5 \21\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\61\3\2\2\2\u00fc\u00fd")
        buf.write("\7\23\2\2\u00fd\u00fe\7\66\2\2\u00fe\u00ff\7>\2\2\u00ff")
        buf.write("\u0100\7\63\2\2\u0100\u0101\5@!\2\u0101\u0102\7<\2\2\u0102")
        buf.write("\u0103\5@!\2\u0103\u0104\7<\2\2\u0104\u0105\5@!\2\u0105")
        buf.write("\u0106\7\67\2\2\u0106\u0108\7\f\2\2\u0107\u0109\5 \21")
        buf.write("\2\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010b\7\21\2\2\u010b\u010c\7=\2\2\u010c")
        buf.write("\63\3\2\2\2\u010d\u010e\7\32\2\2\u010e\u010f\5@!\2\u010f")
        buf.write("\u0111\7\f\2\2\u0110\u0112\5 \21\2\u0111\u0110\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\7")
        buf.write("\22\2\2\u0114\u0115\7=\2\2\u0115\65\3\2\2\2\u0116\u0118")
        buf.write("\7\f\2\2\u0117\u0119\5 \21\2\u0118\u0117\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\7\32\2")
        buf.write("\2\u011b\u011c\5@!\2\u011c\u011d\7\33\2\2\u011d\u011e")
        buf.write("\7=\2\2\u011e\67\3\2\2\2\u011f\u0120\7\n\2\2\u0120\u0121")
        buf.write("\7:\2\2\u01219\3\2\2\2\u0122\u0123\7\13\2\2\u0123\u0124")
        buf.write("\7:\2\2\u0124;\3\2\2\2\u0125\u0126\7>\2\2\u0126\u0128")
        buf.write("\7\66\2\2\u0127\u0129\5V,\2\u0128\u0127\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\7\67\2")
        buf.write("\2\u012b\u012c\7:\2\2\u012c=\3\2\2\2\u012d\u012f\7\27")
        buf.write("\2\2\u012e\u0130\5@!\2\u012f\u012e\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\7:\2\2\u0132")
        buf.write("?\3\2\2\2\u0133\u0134\5B\"\2\u0134\u0135\t\2\2\2\u0135")
        buf.write("\u0136\5B\"\2\u0136\u0139\3\2\2\2\u0137\u0139\5B\"\2\u0138")
        buf.write("\u0133\3\2\2\2\u0138\u0137\3\2\2\2\u0139A\3\2\2\2\u013a")
        buf.write("\u013b\b\"\1\2\u013b\u013c\5D#\2\u013c\u0142\3\2\2\2\u013d")
        buf.write("\u013e\f\4\2\2\u013e\u013f\t\3\2\2\u013f\u0141\5D#\2\u0140")
        buf.write("\u013d\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2")
        buf.write("\u0142\u0143\3\2\2\2\u0143C\3\2\2\2\u0144\u0142\3\2\2")
        buf.write("\2\u0145\u0146\b#\1\2\u0146\u0147\5F$\2\u0147\u014d\3")
        buf.write("\2\2\2\u0148\u0149\f\4\2\2\u0149\u014a\t\4\2\2\u014a\u014c")
        buf.write("\5F$\2\u014b\u0148\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014eE\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0151\b$\1\2\u0151\u0152\5H%\2\u0152\u0158")
        buf.write("\3\2\2\2\u0153\u0154\f\4\2\2\u0154\u0155\t\5\2\2\u0155")
        buf.write("\u0157\5H%\2\u0156\u0153\3\2\2\2\u0157\u015a\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159G\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b\u015c\7\60\2\2\u015c\u015f\5H%\2")
        buf.write("\u015d\u015f\5J&\2\u015e\u015b\3\2\2\2\u015e\u015d\3\2")
        buf.write("\2\2\u015fI\3\2\2\2\u0160\u0161\t\6\2\2\u0161\u0165\5")
        buf.write("J&\2\u0162\u0165\5L\'\2\u0163\u0165\5P)\2\u0164\u0160")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("K\3\2\2\2\u0166\u0169\7>\2\2\u0167\u0169\5T+\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016b\5N(\2\u016bM\3\2\2\2\u016c\u016d\7\64\2\2\u016d")
        buf.write("\u016e\5@!\2\u016e\u016f\7\65\2\2\u016f\u0176\3\2\2\2")
        buf.write("\u0170\u0171\7\64\2\2\u0171\u0172\5@!\2\u0172\u0173\7")
        buf.write("\65\2\2\u0173\u0174\5N(\2\u0174\u0176\3\2\2\2\u0175\u016c")
        buf.write("\3\2\2\2\u0175\u0170\3\2\2\2\u0176O\3\2\2\2\u0177\u017a")
        buf.write("\5T+\2\u0178\u017a\5R*\2\u0179\u0177\3\2\2\2\u0179\u0178")
        buf.write("\3\2\2\2\u017aQ\3\2\2\2\u017b\u0182\5X-\2\u017c\u0182")
        buf.write("\7>\2\2\u017d\u017e\7\66\2\2\u017e\u017f\5@!\2\u017f\u0180")
        buf.write("\7\67\2\2\u0180\u0182\3\2\2\2\u0181\u017b\3\2\2\2\u0181")
        buf.write("\u017c\3\2\2\2\u0181\u017d\3\2\2\2\u0182S\3\2\2\2\u0183")
        buf.write("\u0184\7>\2\2\u0184\u0186\7\66\2\2\u0185\u0187\5V,\2\u0186")
        buf.write("\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0189\7\67\2\2\u0189U\3\2\2\2\u018a\u018b\5@!\2")
        buf.write("\u018b\u018c\7<\2\2\u018c\u018d\5V,\2\u018d\u0190\3\2")
        buf.write("\2\2\u018e\u0190\5@!\2\u018f\u018a\3\2\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190W\3\2\2\2\u0191\u0199\7\3\2\2\u0192\u0199")
        buf.write("\7\4\2\2\u0193\u0199\7\5\2\2\u0194\u0199\7\6\2\2\u0195")
        buf.write("\u0199\7\7\2\2\u0196\u0199\7\b\2\2\u0197\u0199\5^\60\2")
        buf.write("\u0198\u0191\3\2\2\2\u0198\u0192\3\2\2\2\u0198\u0193\3")
        buf.write("\2\2\2\u0198\u0194\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199Y\3\2\2\2\u019a\u019b")
        buf.write("\5\\/\2\u019b\u019c\5Z.\2\u019c\u019f\3\2\2\2\u019d\u019f")
        buf.write("\5\\/\2\u019e\u019a\3\2\2\2\u019e\u019d\3\2\2\2\u019f")
        buf.write("[\3\2\2\2\u01a0\u01a1\7\64\2\2\u01a1\u01a2\t\7\2\2\u01a2")
        buf.write("\u01a3\7\65\2\2\u01a3]\3\2\2\2\u01a4\u01a5\78\2\2\u01a5")
        buf.write("\u01a6\5`\61\2\u01a6\u01a7\79\2\2\u01a7_\3\2\2\2\u01a8")
        buf.write("\u01a9\5b\62\2\u01a9\u01aa\7<\2\2\u01aa\u01ab\5`\61\2")
        buf.write("\u01ab\u01ae\3\2\2\2\u01ac\u01ae\5b\62\2\u01ad\u01a8\3")
        buf.write("\2\2\2\u01ad\u01ac\3\2\2\2\u01aea\3\2\2\2\u01af\u01b6")
        buf.write("\7\3\2\2\u01b0\u01b6\7\4\2\2\u01b1\u01b6\7\5\2\2\u01b2")
        buf.write("\u01b6\7\6\2\2\u01b3\u01b6\7\b\2\2\u01b4\u01b6\5^\60\2")
        buf.write("\u01b5\u01af\3\2\2\2\u01b5\u01b0\3\2\2\2\u01b5\u01b1\3")
        buf.write("\2\2\2\u01b5\u01b2\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4")
        buf.write("\3\2\2\2\u01b6c\3\2\2\2.io{\177\u0084\u008a\u008d\u0093")
        buf.write("\u0099\u00a6\u00ab\u00b0\u00b6\u00be\u00c4\u00cf\u00d8")
        buf.write("\u00e2\u00e5\u00e9\u00eb\u00f4\u00fa\u0108\u0111\u0118")
        buf.write("\u0128\u012f\u0138\u0142\u014d\u0158\u015e\u0164\u0168")
        buf.write("\u0175\u0179\u0181\u0186\u018f\u0198\u019e\u01ad\u01b5")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
                     "'While'", "'EndDo'", "'+'", "'-'", "'*'", "'\\'", 
                     "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", 
                     "'<=.'", "'>=.'", "'!'", "'&&'", "'||'", "'='", "'['", 
                     "']'", "'('", "')'", "'{'", "'}'", "';'", "':'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "DEC_INT_LIT", "HEX_INT_LIT", "OCT_INT_LIT", 
                      "FLT_LIT", "BOOL_LIT", "STR_LIT", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "ADD_I", 
                      "SUB_I", "MUL_I", "DIV_I", "MOD_I", "ADD_F", "SUB_F", 
                      "MUL_F", "DIV_F", "EQ_I", "NEQ_I", "LT_I", "GT_I", 
                      "LTE_I", "GTE_I", "NEQ_F", "LT_F", "GT_F", "LTE_F", 
                      "GTE_F", "NOT", "AND", "OR", "ASSIGN", "LS", "RS", 
                      "LB", "RB", "LC", "RC", "SEMI", "COLON", "COMMA", 
                      "DOT", "ID", "COMMENT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_glob_var_decl_part = 1
    RULE_var_decl_list = 2
    RULE_var_decl = 3
    RULE_var_list = 4
    RULE_var = 5
    RULE_scalar_var = 6
    RULE_compo_var = 7
    RULE_func_decl_part = 8
    RULE_func_decl_list = 9
    RULE_func_decl = 10
    RULE_func_param = 11
    RULE_param_list = 12
    RULE_param = 13
    RULE_func_body = 14
    RULE_stmt_list = 15
    RULE_var_decl_stmt_list = 16
    RULE_other_stmt_list = 17
    RULE_other_stmt = 18
    RULE_var_decl_stmt = 19
    RULE_assign_stmt = 20
    RULE_if_stmt = 21
    RULE_else_if_list = 22
    RULE_else_if = 23
    RULE_for_stmt = 24
    RULE_while_stmt = 25
    RULE_do_while_stmt = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_call_stmt = 29
    RULE_return_stmt = 30
    RULE_exp = 31
    RULE_exp1 = 32
    RULE_exp2 = 33
    RULE_exp3 = 34
    RULE_exp4 = 35
    RULE_exp5 = 36
    RULE_index_exp = 37
    RULE_index_operator = 38
    RULE_func_call_exp = 39
    RULE_operand = 40
    RULE_func_call = 41
    RULE_exp_list = 42
    RULE_literal = 43
    RULE_dimensions = 44
    RULE_dimension = 45
    RULE_array_lit = 46
    RULE_array_element_list = 47
    RULE_array_element = 48

    ruleNames =  [ "program", "glob_var_decl_part", "var_decl_list", "var_decl", 
                   "var_list", "var", "scalar_var", "compo_var", "func_decl_part", 
                   "func_decl_list", "func_decl", "func_param", "param_list", 
                   "param", "func_body", "stmt_list", "var_decl_stmt_list", 
                   "other_stmt_list", "other_stmt", "var_decl_stmt", "assign_stmt", 
                   "if_stmt", "else_if_list", "else_if", "for_stmt", "while_stmt", 
                   "do_while_stmt", "break_stmt", "continue_stmt", "call_stmt", 
                   "return_stmt", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "index_exp", "index_operator", "func_call_exp", 
                   "operand", "func_call", "exp_list", "literal", "dimensions", 
                   "dimension", "array_lit", "array_element_list", "array_element" ]

    EOF = Token.EOF
    DEC_INT_LIT=1
    HEX_INT_LIT=2
    OCT_INT_LIT=3
    FLT_LIT=4
    BOOL_LIT=5
    STR_LIT=6
    BODY=7
    BREAK=8
    CONTINUE=9
    DO=10
    ELSE=11
    ELSEIF=12
    ENDBODY=13
    ENDIF=14
    ENDFOR=15
    ENDWHILE=16
    FOR=17
    FUNCTION=18
    IF=19
    PARAMETER=20
    RETURN=21
    THEN=22
    VAR=23
    WHILE=24
    ENDDO=25
    ADD_I=26
    SUB_I=27
    MUL_I=28
    DIV_I=29
    MOD_I=30
    ADD_F=31
    SUB_F=32
    MUL_F=33
    DIV_F=34
    EQ_I=35
    NEQ_I=36
    LT_I=37
    GT_I=38
    LTE_I=39
    GTE_I=40
    NEQ_F=41
    LT_F=42
    GT_F=43
    LTE_F=44
    GTE_F=45
    NOT=46
    AND=47
    OR=48
    ASSIGN=49
    LS=50
    RS=51
    LB=52
    RB=53
    LC=54
    RC=55
    SEMI=56
    COLON=57
    COMMA=58
    DOT=59
    ID=60
    COMMENT=61
    WS=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def glob_var_decl_part(self):
            return self.getTypedRuleContext(BKITParser.Glob_var_decl_partContext,0)


        def func_decl_part(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_partContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.glob_var_decl_part()
            self.state = 99
            self.func_decl_part()
            self.state = 100
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Glob_var_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_glob_var_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlob_var_decl_part" ):
                return visitor.visitGlob_var_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def glob_var_decl_part(self):

        localctx = BKITParser.Glob_var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_glob_var_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 102
                self.var_decl_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = BKITParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl_list)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.var_decl()
                self.state = 106
                self.var_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(BKITParser.VAR)
            self.state = 112
            self.match(BKITParser.COLON)
            self.state = 113
            self.var_list()
            self.state = 114
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BKITParser.VarContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_list)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.var()
                self.state = 117
                self.match(BKITParser.COMMA)
                self.state = 118
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def compo_var(self):
            return self.getTypedRuleContext(BKITParser.Compo_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKITParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.compo_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scalar_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(BKITParser.ID)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 128
                self.match(BKITParser.ASSIGN)
                self.state = 129
                self.literal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compo_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_compo_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompo_var" ):
                return visitor.visitCompo_var(self)
            else:
                return visitor.visitChildren(self)




    def compo_var(self):

        localctx = BKITParser.Compo_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compo_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BKITParser.ID)
            self.state = 133
            self.dimensions()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 134
                self.match(BKITParser.ASSIGN)
                self.state = 135
                self.array_lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_part" ):
                return visitor.visitFunc_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_part(self):

        localctx = BKITParser.Func_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.FUNCTION:
                self.state = 138
                self.func_decl_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(BKITParser.Func_declContext,0)


        def func_decl_list(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_list" ):
                return visitor.visitFunc_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_list(self):

        localctx = BKITParser.Func_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_decl_list)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.func_decl()
                self.state = 142
                self.func_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.func_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def func_param(self):
            return self.getTypedRuleContext(BKITParser.Func_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(BKITParser.FUNCTION)
            self.state = 148
            self.match(BKITParser.COLON)
            self.state = 149
            self.match(BKITParser.ID)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 150
                self.func_param()


            self.state = 153
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_param" ):
                return visitor.visitFunc_param(self)
            else:
                return visitor.visitChildren(self)




    def func_param(self):

        localctx = BKITParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BKITParser.PARAMETER)
            self.state = 156
            self.match(BKITParser.COLON)
            self.state = 157
            self.param_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKITParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.param()
                self.state = 160
                self.match(BKITParser.COMMA)
                self.state = 161
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(BKITParser.ID)
                self.state = 168
                self.dimensions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(BKITParser.BODY)
            self.state = 172
            self.match(BKITParser.COLON)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 173
                self.stmt_list()


            self.state = 176
            self.match(BKITParser.ENDBODY)
            self.state = 177
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Other_stmt_listContext,0)


        def var_decl_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 179
                self.var_decl_stmt_list()


            self.state = 182
            self.other_stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_stmt(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_stmtContext,0)


        def var_decl_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt_list" ):
                return visitor.visitVar_decl_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt_list(self):

        localctx = BKITParser.Var_decl_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_decl_stmt_list)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.var_decl_stmt()
                self.state = 185
                self.var_decl_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.var_decl_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def other_stmt(self):
            return self.getTypedRuleContext(BKITParser.Other_stmtContext,0)


        def other_stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Other_stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_other_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_stmt_list" ):
                return visitor.visitOther_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def other_stmt_list(self):

        localctx = BKITParser.Other_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_other_stmt_list)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.other_stmt()
                self.state = 191
                self.other_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.other_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_other_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_stmt" ):
                return visitor.visitOther_stmt(self)
            else:
                return visitor.visitChildren(self)




    def other_stmt(self):

        localctx = BKITParser.Other_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_other_stmt)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 202
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 203
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 204
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt" ):
                return visitor.visitVar_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt(self):

        localctx = BKITParser.Var_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(BKITParser.VAR)
            self.state = 208
            self.match(BKITParser.COLON)
            self.state = 209
            self.var_list()
            self.state = 210
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_exp(self):
            return self.getTypedRuleContext(BKITParser.Index_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 212
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 213
                self.index_exp()
                pass


            self.state = 216
            self.match(BKITParser.ASSIGN)
            self.state = 217
            self.exp()
            self.state = 218
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def else_if_list(self):
            return self.getTypedRuleContext(BKITParser.Else_if_listContext,0)


        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BKITParser.IF)
            self.state = 221
            self.exp()
            self.state = 222
            self.match(BKITParser.THEN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 223
                self.stmt_list()


            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 226
                self.else_if_list()


            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 229
                self.match(BKITParser.ELSE)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                    self.state = 230
                    self.stmt_list()




            self.state = 235
            self.match(BKITParser.ENDIF)
            self.state = 236
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if(self):
            return self.getTypedRuleContext(BKITParser.Else_ifContext,0)


        def else_if_list(self):
            return self.getTypedRuleContext(BKITParser.Else_if_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_list" ):
                return visitor.visitElse_if_list(self)
            else:
                return visitor.visitChildren(self)




    def else_if_list(self):

        localctx = BKITParser.Else_if_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_if_list)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.else_if()
                self.state = 239
                self.else_if_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.else_if()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = BKITParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_else_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(BKITParser.ELSEIF)
            self.state = 245
            self.exp()
            self.state = 246
            self.match(BKITParser.THEN)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 247
                self.stmt_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BKITParser.FOR)
            self.state = 251
            self.match(BKITParser.LB)
            self.state = 252
            self.match(BKITParser.ID)
            self.state = 253
            self.match(BKITParser.ASSIGN)
            self.state = 254
            self.exp()
            self.state = 255
            self.match(BKITParser.COMMA)
            self.state = 256
            self.exp()
            self.state = 257
            self.match(BKITParser.COMMA)
            self.state = 258
            self.exp()
            self.state = 259
            self.match(BKITParser.RB)
            self.state = 260
            self.match(BKITParser.DO)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 261
                self.stmt_list()


            self.state = 264
            self.match(BKITParser.ENDFOR)
            self.state = 265
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.WHILE)
            self.state = 268
            self.exp()
            self.state = 269
            self.match(BKITParser.DO)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 270
                self.stmt_list()


            self.state = 273
            self.match(BKITParser.ENDWHILE)
            self.state = 274
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKITParser.DO)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 277
                self.stmt_list()


            self.state = 280
            self.match(BKITParser.WHILE)
            self.state = 281
            self.exp()
            self.state = 282
            self.match(BKITParser.ENDDO)
            self.state = 283
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(BKITParser.BREAK)
            self.state = 286
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(BKITParser.CONTINUE)
            self.state = 289
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BKITParser.ID)
            self.state = 292
            self.match(BKITParser.LB)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT) | (1 << BKITParser.SUB_I) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LC) | (1 << BKITParser.ID))) != 0):
                self.state = 293
                self.exp_list()


            self.state = 296
            self.match(BKITParser.RB)
            self.state = 297
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.RETURN)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT) | (1 << BKITParser.SUB_I) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LC) | (1 << BKITParser.ID))) != 0):
                self.state = 300
                self.exp()


            self.state = 303
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQ_I(self):
            return self.getToken(BKITParser.EQ_I, 0)

        def NEQ_I(self):
            return self.getToken(BKITParser.NEQ_I, 0)

        def LT_I(self):
            return self.getToken(BKITParser.LT_I, 0)

        def GT_I(self):
            return self.getToken(BKITParser.GT_I, 0)

        def LTE_I(self):
            return self.getToken(BKITParser.LTE_I, 0)

        def GTE_I(self):
            return self.getToken(BKITParser.GTE_I, 0)

        def NEQ_F(self):
            return self.getToken(BKITParser.NEQ_F, 0)

        def LT_F(self):
            return self.getToken(BKITParser.LT_F, 0)

        def GT_F(self):
            return self.getToken(BKITParser.GT_F, 0)

        def LTE_F(self):
            return self.getToken(BKITParser.LTE_F, 0)

        def GTE_F(self):
            return self.getToken(BKITParser.GTE_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.exp1(0)
                self.state = 306
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ_I) | (1 << BKITParser.NEQ_I) | (1 << BKITParser.LT_I) | (1 << BKITParser.GT_I) | (1 << BKITParser.LTE_I) | (1 << BKITParser.GTE_I) | (1 << BKITParser.NEQ_F) | (1 << BKITParser.LT_F) | (1 << BKITParser.GT_F) | (1 << BKITParser.LTE_F) | (1 << BKITParser.GTE_F))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 307
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 317
                    self.exp2(0) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD_I(self):
            return self.getToken(BKITParser.ADD_I, 0)

        def ADD_F(self):
            return self.getToken(BKITParser.ADD_F, 0)

        def SUB_I(self):
            return self.getToken(BKITParser.SUB_I, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD_I) | (1 << BKITParser.SUB_I) | (1 << BKITParser.ADD_F) | (1 << BKITParser.SUB_F))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 328
                    self.exp3(0) 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL_I(self):
            return self.getToken(BKITParser.MUL_I, 0)

        def MUL_F(self):
            return self.getToken(BKITParser.MUL_F, 0)

        def DIV_I(self):
            return self.getToken(BKITParser.DIV_I, 0)

        def DIV_F(self):
            return self.getToken(BKITParser.DIV_F, 0)

        def MOD_I(self):
            return self.getToken(BKITParser.MOD_I, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 338
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL_I) | (1 << BKITParser.DIV_I) | (1 << BKITParser.MOD_I) | (1 << BKITParser.MUL_F) | (1 << BKITParser.DIV_F))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 339
                    self.exp4() 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp4)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(BKITParser.NOT)
                self.state = 346
                self.exp4()
                pass
            elif token in [BKITParser.DEC_INT_LIT, BKITParser.HEX_INT_LIT, BKITParser.OCT_INT_LIT, BKITParser.FLT_LIT, BKITParser.BOOL_LIT, BKITParser.STR_LIT, BKITParser.SUB_I, BKITParser.SUB_F, BKITParser.LB, BKITParser.LC, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB_I(self):
            return self.getToken(BKITParser.SUB_I, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def index_exp(self):
            return self.getTypedRuleContext(BKITParser.Index_expContext,0)


        def func_call_exp(self):
            return self.getTypedRuleContext(BKITParser.Func_call_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB_I or _la==BKITParser.SUB_F):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 351
                self.exp5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.index_exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.func_call_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp" ):
                return visitor.visitIndex_exp(self)
            else:
                return visitor.visitChildren(self)




    def index_exp(self):

        localctx = BKITParser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 356
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 357
                self.func_call()
                pass


            self.state = 360
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_operator)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(BKITParser.LS)
                self.state = 363
                self.exp()
                self.state = 364
                self.match(BKITParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(BKITParser.LS)
                self.state = 367
                self.exp()
                self.state = 368
                self.match(BKITParser.RS)
                self.state = 369
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_call_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_exp" ):
                return visitor.visitFunc_call_exp(self)
            else:
                return visitor.visitChildren(self)




    def func_call_exp(self):

        localctx = BKITParser.Func_call_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_call_exp)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_operand)
        try:
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.DEC_INT_LIT, BKITParser.HEX_INT_LIT, BKITParser.OCT_INT_LIT, BKITParser.FLT_LIT, BKITParser.BOOL_LIT, BKITParser.STR_LIT, BKITParser.LC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.literal()
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.match(BKITParser.LB)
                self.state = 380
                self.exp()
                self.state = 381
                self.match(BKITParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(BKITParser.ID)
            self.state = 386
            self.match(BKITParser.LB)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT) | (1 << BKITParser.FLT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STR_LIT) | (1 << BKITParser.SUB_I) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LB) | (1 << BKITParser.LC) | (1 << BKITParser.ID))) != 0):
                self.state = 387
                self.exp_list()


            self.state = 390
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = BKITParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp_list)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.exp()
                self.state = 393
                self.match(BKITParser.COMMA)
                self.state = 394
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_INT_LIT(self):
            return self.getToken(BKITParser.DEC_INT_LIT, 0)

        def HEX_INT_LIT(self):
            return self.getToken(BKITParser.HEX_INT_LIT, 0)

        def OCT_INT_LIT(self):
            return self.getToken(BKITParser.OCT_INT_LIT, 0)

        def FLT_LIT(self):
            return self.getToken(BKITParser.FLT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def STR_LIT(self):
            return self.getToken(BKITParser.STR_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.DEC_INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(BKITParser.DEC_INT_LIT)
                pass
            elif token in [BKITParser.HEX_INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(BKITParser.HEX_INT_LIT)
                pass
            elif token in [BKITParser.OCT_INT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.match(BKITParser.OCT_INT_LIT)
                pass
            elif token in [BKITParser.FLT_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 402
                self.match(BKITParser.FLT_LIT)
                pass
            elif token in [BKITParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 403
                self.match(BKITParser.BOOL_LIT)
                pass
            elif token in [BKITParser.STR_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 404
                self.match(BKITParser.STR_LIT)
                pass
            elif token in [BKITParser.LC]:
                self.enterOuterAlt(localctx, 7)
                self.state = 405
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = BKITParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_dimensions)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.dimension()
                self.state = 409
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def DEC_INT_LIT(self):
            return self.getToken(BKITParser.DEC_INT_LIT, 0)

        def HEX_INT_LIT(self):
            return self.getToken(BKITParser.HEX_INT_LIT, 0)

        def OCT_INT_LIT(self):
            return self.getToken(BKITParser.OCT_INT_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(BKITParser.LS)
            self.state = 415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DEC_INT_LIT) | (1 << BKITParser.HEX_INT_LIT) | (1 << BKITParser.OCT_INT_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 416
            self.match(BKITParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(BKITParser.LC, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(BKITParser.Array_element_listContext,0)


        def RC(self):
            return self.getToken(BKITParser.RC, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(BKITParser.LC)
            self.state = 419
            self.array_element_list()
            self.state = 420
            self.match(BKITParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(BKITParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(BKITParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_list" ):
                return visitor.visitArray_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_element_list(self):

        localctx = BKITParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_element_list)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.array_element()
                self.state = 423
                self.match(BKITParser.COMMA)
                self.state = 424
                self.array_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_INT_LIT(self):
            return self.getToken(BKITParser.DEC_INT_LIT, 0)

        def HEX_INT_LIT(self):
            return self.getToken(BKITParser.HEX_INT_LIT, 0)

        def OCT_INT_LIT(self):
            return self.getToken(BKITParser.OCT_INT_LIT, 0)

        def FLT_LIT(self):
            return self.getToken(BKITParser.FLT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(BKITParser.STR_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = BKITParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_element)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.DEC_INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(BKITParser.DEC_INT_LIT)
                pass
            elif token in [BKITParser.HEX_INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(BKITParser.HEX_INT_LIT)
                pass
            elif token in [BKITParser.OCT_INT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(BKITParser.OCT_INT_LIT)
                pass
            elif token in [BKITParser.FLT_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
                self.match(BKITParser.FLT_LIT)
                pass
            elif token in [BKITParser.STR_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 433
                self.match(BKITParser.STR_LIT)
                pass
            elif token in [BKITParser.LC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 434
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.exp1_sempred
        self._predicates[33] = self.exp2_sempred
        self._predicates[34] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




