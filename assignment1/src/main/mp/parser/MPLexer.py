# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


    from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u0206\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\39\39")
        buf.write("\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\3J\3K\3K\3L\6L\u01ae\nL\rL\16L\u01af\3L")
        buf.write("\3L\3M\3M\3M\3M\7M\u01b8\nM\fM\16M\u01bb\13M\3M\3M\3M")
        buf.write("\3M\3M\3N\3N\7N\u01c4\nN\fN\16N\u01c7\13N\3N\3N\3N\3N")
        buf.write("\3O\3O\3O\3O\7O\u01d1\nO\fO\16O\u01d4\13O\3O\3O\3P\3P")
        buf.write("\7P\u01da\nP\fP\16P\u01dd\13P\3Q\6Q\u01e0\nQ\rQ\16Q\u01e1")
        buf.write("\3R\3R\3R\5R\u01e7\nR\3R\3R\5R\u01eb\nR\3R\5R\u01ee\n")
        buf.write("R\3S\3S\5S\u01f2\nS\3S\3S\3T\3T\5T\u01f8\nT\3U\3U\3U\7")
        buf.write("U\u01fd\nU\fU\16U\u0200\13U\3U\3U\3V\3V\3V\4\u01b9\u01c5")
        buf.write("\2W\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20")
        buf.write("S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m")
        buf.write("\36o\37q s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087")
        buf.write("+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095")
        buf.write("\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f\67\u00a1")
        buf.write("8\u00a39\u00a5\2\u00a7:\u00a9;\u00ab\2\3\2$\4\2CCcc\4")
        buf.write("\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJj")
        buf.write("j\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2")
        buf.write("QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4")
        buf.write("\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\5\2\13\f\17\17")
        buf.write("\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3")
        buf.write("\2//\6\2\n\f\16\17$$^^\n\2$$))^^ddhhppttvv\2\u01f6\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\3\u00ad\3\2\2\2\5\u00af\3\2\2\2\7\u00b1")
        buf.write("\3\2\2\2\t\u00b3\3\2\2\2\13\u00b5\3\2\2\2\r\u00b7\3\2")
        buf.write("\2\2\17\u00b9\3\2\2\2\21\u00bb\3\2\2\2\23\u00bd\3\2\2")
        buf.write("\2\25\u00bf\3\2\2\2\27\u00c1\3\2\2\2\31\u00c3\3\2\2\2")
        buf.write("\33\u00c5\3\2\2\2\35\u00c7\3\2\2\2\37\u00c9\3\2\2\2!\u00cb")
        buf.write("\3\2\2\2#\u00cd\3\2\2\2%\u00cf\3\2\2\2\'\u00d1\3\2\2\2")
        buf.write(")\u00d3\3\2\2\2+\u00d5\3\2\2\2-\u00d7\3\2\2\2/\u00d9\3")
        buf.write("\2\2\2\61\u00db\3\2\2\2\63\u00dd\3\2\2\2\65\u00df\3\2")
        buf.write("\2\2\67\u00e1\3\2\2\29\u00e7\3\2\2\2;\u00f0\3\2\2\2=\u00f4")
        buf.write("\3\2\2\2?\u00f7\3\2\2\2A\u00fe\3\2\2\2C\u0101\3\2\2\2")
        buf.write("E\u0104\3\2\2\2G\u0109\3\2\2\2I\u010e\3\2\2\2K\u0115\3")
        buf.write("\2\2\2M\u011b\3\2\2\2O\u0121\3\2\2\2Q\u0125\3\2\2\2S\u012e")
        buf.write("\3\2\2\2U\u0138\3\2\2\2W\u013c\3\2\2\2Y\u0141\3\2\2\2")
        buf.write("[\u0147\3\2\2\2]\u014d\3\2\2\2_\u0150\3\2\2\2a\u0155\3")
        buf.write("\2\2\2c\u015d\3\2\2\2e\u0165\3\2\2\2g\u016c\3\2\2\2i\u0170")
        buf.write("\3\2\2\2k\u0174\3\2\2\2m\u0177\3\2\2\2o\u017b\3\2\2\2")
        buf.write("q\u017f\3\2\2\2s\u0184\3\2\2\2u\u0186\3\2\2\2w\u0188\3")
        buf.write("\2\2\2y\u018a\3\2\2\2{\u018c\3\2\2\2}\u018f\3\2\2\2\177")
        buf.write("\u0191\3\2\2\2\u0081\u0193\3\2\2\2\u0083\u0195\3\2\2\2")
        buf.write("\u0085\u0198\3\2\2\2\u0087\u019b\3\2\2\2\u0089\u019d\3")
        buf.write("\2\2\2\u008b\u019f\3\2\2\2\u008d\u01a1\3\2\2\2\u008f\u01a3")
        buf.write("\3\2\2\2\u0091\u01a5\3\2\2\2\u0093\u01a7\3\2\2\2\u0095")
        buf.write("\u01aa\3\2\2\2\u0097\u01ad\3\2\2\2\u0099\u01b3\3\2\2\2")
        buf.write("\u009b\u01c1\3\2\2\2\u009d\u01cc\3\2\2\2\u009f\u01d7\3")
        buf.write("\2\2\2\u00a1\u01df\3\2\2\2\u00a3\u01ea\3\2\2\2\u00a5\u01ef")
        buf.write("\3\2\2\2\u00a7\u01f7\3\2\2\2\u00a9\u01f9\3\2\2\2\u00ab")
        buf.write("\u0203\3\2\2\2\u00ad\u00ae\t\2\2\2\u00ae\4\3\2\2\2\u00af")
        buf.write("\u00b0\t\3\2\2\u00b0\6\3\2\2\2\u00b1\u00b2\t\4\2\2\u00b2")
        buf.write("\b\3\2\2\2\u00b3\u00b4\t\5\2\2\u00b4\n\3\2\2\2\u00b5\u00b6")
        buf.write("\t\6\2\2\u00b6\f\3\2\2\2\u00b7\u00b8\t\7\2\2\u00b8\16")
        buf.write("\3\2\2\2\u00b9\u00ba\t\b\2\2\u00ba\20\3\2\2\2\u00bb\u00bc")
        buf.write("\t\t\2\2\u00bc\22\3\2\2\2\u00bd\u00be\t\n\2\2\u00be\24")
        buf.write("\3\2\2\2\u00bf\u00c0\t\13\2\2\u00c0\26\3\2\2\2\u00c1\u00c2")
        buf.write("\t\f\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\t\r\2\2\u00c4\32")
        buf.write("\3\2\2\2\u00c5\u00c6\t\16\2\2\u00c6\34\3\2\2\2\u00c7\u00c8")
        buf.write("\t\17\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\t\20\2\2\u00ca")
        buf.write(" \3\2\2\2\u00cb\u00cc\t\21\2\2\u00cc\"\3\2\2\2\u00cd\u00ce")
        buf.write("\t\22\2\2\u00ce$\3\2\2\2\u00cf\u00d0\t\23\2\2\u00d0&\3")
        buf.write("\2\2\2\u00d1\u00d2\t\24\2\2\u00d2(\3\2\2\2\u00d3\u00d4")
        buf.write("\t\25\2\2\u00d4*\3\2\2\2\u00d5\u00d6\t\26\2\2\u00d6,\3")
        buf.write("\2\2\2\u00d7\u00d8\t\27\2\2\u00d8.\3\2\2\2\u00d9\u00da")
        buf.write("\t\30\2\2\u00da\60\3\2\2\2\u00db\u00dc\t\31\2\2\u00dc")
        buf.write("\62\3\2\2\2\u00dd\u00de\t\32\2\2\u00de\64\3\2\2\2\u00df")
        buf.write("\u00e0\t\33\2\2\u00e0\66\3\2\2\2\u00e1\u00e2\5\5\3\2\u00e2")
        buf.write("\u00e3\5%\23\2\u00e3\u00e4\5\13\6\2\u00e4\u00e5\5\3\2")
        buf.write("\2\u00e5\u00e6\5\27\f\2\u00e68\3\2\2\2\u00e7\u00e8\5\7")
        buf.write("\4\2\u00e8\u00e9\5\37\20\2\u00e9\u00ea\5\35\17\2\u00ea")
        buf.write("\u00eb\5)\25\2\u00eb\u00ec\5\23\n\2\u00ec\u00ed\5\35\17")
        buf.write("\2\u00ed\u00ee\5+\26\2\u00ee\u00ef\5\13\6\2\u00ef:\3\2")
        buf.write("\2\2\u00f0\u00f1\5\r\7\2\u00f1\u00f2\5\37\20\2\u00f2\u00f3")
        buf.write("\5%\23\2\u00f3<\3\2\2\2\u00f4\u00f5\5)\25\2\u00f5\u00f6")
        buf.write("\5\37\20\2\u00f6>\3\2\2\2\u00f7\u00f8\5\t\5\2\u00f8\u00f9")
        buf.write("\5\37\20\2\u00f9\u00fa\5/\30\2\u00fa\u00fb\5\35\17\2\u00fb")
        buf.write("\u00fc\5)\25\2\u00fc\u00fd\5\37\20\2\u00fd@\3\2\2\2\u00fe")
        buf.write("\u00ff\5\t\5\2\u00ff\u0100\5\37\20\2\u0100B\3\2\2\2\u0101")
        buf.write("\u0102\5\23\n\2\u0102\u0103\5\r\7\2\u0103D\3\2\2\2\u0104")
        buf.write("\u0105\5)\25\2\u0105\u0106\5\21\t\2\u0106\u0107\5\13\6")
        buf.write("\2\u0107\u0108\5\35\17\2\u0108F\3\2\2\2\u0109\u010a\5")
        buf.write("\13\6\2\u010a\u010b\5\31\r\2\u010b\u010c\5\'\24\2\u010c")
        buf.write("\u010d\5\13\6\2\u010dH\3\2\2\2\u010e\u010f\5%\23\2\u010f")
        buf.write("\u0110\5\13\6\2\u0110\u0111\5)\25\2\u0111\u0112\5+\26")
        buf.write("\2\u0112\u0113\5%\23\2\u0113\u0114\5\35\17\2\u0114J\3")
        buf.write("\2\2\2\u0115\u0116\5/\30\2\u0116\u0117\5\21\t\2\u0117")
        buf.write("\u0118\5\23\n\2\u0118\u0119\5\31\r\2\u0119\u011a\5\13")
        buf.write("\6\2\u011aL\3\2\2\2\u011b\u011c\5\5\3\2\u011c\u011d\5")
        buf.write("\13\6\2\u011d\u011e\5\17\b\2\u011e\u011f\5\23\n\2\u011f")
        buf.write("\u0120\5\35\17\2\u0120N\3\2\2\2\u0121\u0122\5\13\6\2\u0122")
        buf.write("\u0123\5\35\17\2\u0123\u0124\5\t\5\2\u0124P\3\2\2\2\u0125")
        buf.write("\u0126\5\r\7\2\u0126\u0127\5+\26\2\u0127\u0128\5\35\17")
        buf.write("\2\u0128\u0129\5\7\4\2\u0129\u012a\5)\25\2\u012a\u012b")
        buf.write("\5\23\n\2\u012b\u012c\5\37\20\2\u012c\u012d\5\35\17\2")
        buf.write("\u012dR\3\2\2\2\u012e\u012f\5!\21\2\u012f\u0130\5%\23")
        buf.write("\2\u0130\u0131\5\37\20\2\u0131\u0132\5\7\4\2\u0132\u0133")
        buf.write("\5\13\6\2\u0133\u0134\5\t\5\2\u0134\u0135\5+\26\2\u0135")
        buf.write("\u0136\5%\23\2\u0136\u0137\5\13\6\2\u0137T\3\2\2\2\u0138")
        buf.write("\u0139\5-\27\2\u0139\u013a\5\3\2\2\u013a\u013b\5%\23\2")
        buf.write("\u013bV\3\2\2\2\u013c\u013d\5)\25\2\u013d\u013e\5%\23")
        buf.write("\2\u013e\u013f\5+\26\2\u013f\u0140\5\13\6\2\u0140X\3\2")
        buf.write("\2\2\u0141\u0142\5\r\7\2\u0142\u0143\5\3\2\2\u0143\u0144")
        buf.write("\5\31\r\2\u0144\u0145\5\'\24\2\u0145\u0146\5\13\6\2\u0146")
        buf.write("Z\3\2\2\2\u0147\u0148\5\3\2\2\u0148\u0149\5%\23\2\u0149")
        buf.write("\u014a\5%\23\2\u014a\u014b\5\3\2\2\u014b\u014c\5\63\32")
        buf.write("\2\u014c\\\3\2\2\2\u014d\u014e\5\37\20\2\u014e\u014f\5")
        buf.write("\r\7\2\u014f^\3\2\2\2\u0150\u0151\5%\23\2\u0151\u0152")
        buf.write("\5\13\6\2\u0152\u0153\5\3\2\2\u0153\u0154\5\31\r\2\u0154")
        buf.write("`\3\2\2\2\u0155\u0156\5\5\3\2\u0156\u0157\5\37\20\2\u0157")
        buf.write("\u0158\5\37\20\2\u0158\u0159\5\31\r\2\u0159\u015a\5\13")
        buf.write("\6\2\u015a\u015b\5\3\2\2\u015b\u015c\5\35\17\2\u015cb")
        buf.write("\3\2\2\2\u015d\u015e\5\23\n\2\u015e\u015f\5\35\17\2\u015f")
        buf.write("\u0160\5)\25\2\u0160\u0161\5\13\6\2\u0161\u0162\5\17\b")
        buf.write("\2\u0162\u0163\5\13\6\2\u0163\u0164\5%\23\2\u0164d\3\2")
        buf.write("\2\2\u0165\u0166\5\'\24\2\u0166\u0167\5)\25\2\u0167\u0168")
        buf.write("\5%\23\2\u0168\u0169\5\23\n\2\u0169\u016a\5\35\17\2\u016a")
        buf.write("\u016b\5\17\b\2\u016bf\3\2\2\2\u016c\u016d\5\35\17\2\u016d")
        buf.write("\u016e\5\37\20\2\u016e\u016f\5)\25\2\u016fh\3\2\2\2\u0170")
        buf.write("\u0171\5\3\2\2\u0171\u0172\5\35\17\2\u0172\u0173\5\t\5")
        buf.write("\2\u0173j\3\2\2\2\u0174\u0175\5\37\20\2\u0175\u0176\5")
        buf.write("%\23\2\u0176l\3\2\2\2\u0177\u0178\5\t\5\2\u0178\u0179")
        buf.write("\5\23\n\2\u0179\u017a\5-\27\2\u017an\3\2\2\2\u017b\u017c")
        buf.write("\5\33\16\2\u017c\u017d\5\37\20\2\u017d\u017e\5\t\5\2\u017e")
        buf.write("p\3\2\2\2\u017f\u0180\5/\30\2\u0180\u0181\5\23\n\2\u0181")
        buf.write("\u0182\5)\25\2\u0182\u0183\5\21\t\2\u0183r\3\2\2\2\u0184")
        buf.write("\u0185\7-\2\2\u0185t\3\2\2\2\u0186\u0187\7/\2\2\u0187")
        buf.write("v\3\2\2\2\u0188\u0189\7,\2\2\u0189x\3\2\2\2\u018a\u018b")
        buf.write("\7\61\2\2\u018bz\3\2\2\2\u018c\u018d\7>\2\2\u018d\u018e")
        buf.write("\7@\2\2\u018e|\3\2\2\2\u018f\u0190\7?\2\2\u0190~\3\2\2")
        buf.write("\2\u0191\u0192\7>\2\2\u0192\u0080\3\2\2\2\u0193\u0194")
        buf.write("\7@\2\2\u0194\u0082\3\2\2\2\u0195\u0196\7>\2\2\u0196\u0197")
        buf.write("\7?\2\2\u0197\u0084\3\2\2\2\u0198\u0199\7@\2\2\u0199\u019a")
        buf.write("\7?\2\2\u019a\u0086\3\2\2\2\u019b\u019c\7]\2\2\u019c\u0088")
        buf.write("\3\2\2\2\u019d\u019e\7_\2\2\u019e\u008a\3\2\2\2\u019f")
        buf.write("\u01a0\7<\2\2\u01a0\u008c\3\2\2\2\u01a1\u01a2\7*\2\2\u01a2")
        buf.write("\u008e\3\2\2\2\u01a3\u01a4\7+\2\2\u01a4\u0090\3\2\2\2")
        buf.write("\u01a5\u01a6\7=\2\2\u01a6\u0092\3\2\2\2\u01a7\u01a8\7")
        buf.write("\60\2\2\u01a8\u01a9\7\60\2\2\u01a9\u0094\3\2\2\2\u01aa")
        buf.write("\u01ab\7.\2\2\u01ab\u0096\3\2\2\2\u01ac\u01ae\t\34\2\2")
        buf.write("\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2")
        buf.write("\bL\2\2\u01b2\u0098\3\2\2\2\u01b3\u01b4\7*\2\2\u01b4\u01b5")
        buf.write("\7,\2\2\u01b5\u01b9\3\2\2\2\u01b6\u01b8\13\2\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bc\u01bd\7,\2\2\u01bd\u01be\7+\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01c0\bM\2\2\u01c0\u009a\3\2\2\2\u01c1")
        buf.write("\u01c5\7}\2\2\u01c2\u01c4\13\2\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c7\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c5\u01c3\3")
        buf.write("\2\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9")
        buf.write("\7\177\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\bN\2\2\u01cb")
        buf.write("\u009c\3\2\2\2\u01cc\u01cd\7\61\2\2\u01cd\u01ce\7\61\2")
        buf.write("\2\u01ce\u01d2\3\2\2\2\u01cf\u01d1\n\35\2\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d5\u01d6\bO\2\2\u01d6\u009e\3\2\2\2\u01d7\u01db\t")
        buf.write("\36\2\2\u01d8\u01da\t\37\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01dc\u00a0\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01e0\t")
        buf.write(" \2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u00a2\3\2\2\2\u01e3")
        buf.write("\u01e4\5\u00a1Q\2\u01e4\u01e6\7\60\2\2\u01e5\u01e7\5\u00a1")
        buf.write("Q\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01eb")
        buf.write("\3\2\2\2\u01e8\u01e9\7\60\2\2\u01e9\u01eb\5\u00a1Q\2\u01ea")
        buf.write("\u01e3\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\3\2\2\2")
        buf.write("\u01ec\u01ee\5\u00a5S\2\u01ed\u01ec\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u00a4\3\2\2\2\u01ef\u01f1\t\6\2\2\u01f0")
        buf.write("\u01f2\t!\2\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\5\u00a1Q\2\u01f4\u00a6")
        buf.write("\3\2\2\2\u01f5\u01f8\5W,\2\u01f6\u01f8\5Y-\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8\u00a8\3\2\2\2\u01f9")
        buf.write("\u01fe\7$\2\2\u01fa\u01fd\n\"\2\2\u01fb\u01fd\5\u00ab")
        buf.write("V\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u0200")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0201\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0202\7$\2\2")
        buf.write("\u0202\u00aa\3\2\2\2\u0203\u0204\7^\2\2\u0204\u0205\t")
        buf.write("#\2\2\u0205\u00ac\3\2\2\2\20\2\u01af\u01b9\u01c5\u01d2")
        buf.write("\u01db\u01e1\u01e6\u01ea\u01ed\u01f1\u01f7\u01fc\u01fe")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    TO = 4
    DOWNTO = 5
    DO = 6
    IF = 7
    THEN = 8
    ELSE = 9
    RETURN = 10
    WHILE = 11
    BEGIN = 12
    END = 13
    FUNCTION = 14
    PROCEDURE = 15
    VAR = 16
    TRUE = 17
    FALSE = 18
    ARRAY = 19
    OF = 20
    REAL = 21
    BOOLEAN = 22
    INTEGER = 23
    STRING = 24
    NOT = 25
    AND = 26
    OR = 27
    DIV = 28
    MOD = 29
    WITH = 30
    ADDOP = 31
    SUBOP = 32
    MULOP = 33
    DIVOP = 34
    NOT_EQUAL = 35
    EQUAL = 36
    LT = 37
    GT = 38
    LE = 39
    GE = 40
    LSB = 41
    RSB = 42
    COLON = 43
    LB = 44
    RB = 45
    SEMI = 46
    DOTDOT = 47
    COMMA = 48
    WS = 49
    COMMENT_1 = 50
    COMMENT_2 = 51
    COMMENT_3 = 52
    IDENT = 53
    INTLIT = 54
    FLOATLIT = 55
    BOOLLIT = 56
    STRINGLIT = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ADDOP", 
            "SUBOP", "MULOP", "DIVOP", "NOT_EQUAL", "EQUAL", "LT", "GT", 
            "LE", "GE", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DOTDOT", 
            "COMMA", "WS", "COMMENT_1", "COMMENT_2", "COMMENT_3", "IDENT", 
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "NOT_EQUAL", "EQUAL", "LT", 
                  "GT", "LE", "GE", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", 
                  "DOTDOT", "COMMA", "WS", "COMMENT_1", "COMMENT_2", "COMMENT_3", 
                  "IDENT", "INTLIT", "FLOATLIT", "ExponentPart", "BOOLLIT", 
                  "STRINGLIT", "EscapeSequence" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


