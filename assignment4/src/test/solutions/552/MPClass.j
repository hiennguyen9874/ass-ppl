.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass/a I
	getstatic MPClass/a I
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
.var 1 is a I from Label6 to Label7
Label6:
	iconst_2
	istore_1
Label8:
	iload_1
	iconst_3
	if_icmpgt Label10
.var 2 is b I from Label11 to Label12
Label11:
	iload_1
	invokestatic io/putIntLn(I)V
Label12:
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
Label7:
	goto Label5
Label4:
.var 1 is a I from Label13 to Label14
Label13:
	bipush 7
	istore_1
Label15:
	iload_1
	bipush 8
	if_icmpgt Label17
.var 2 is b I from Label18 to Label19
Label18:
	iload_1
	invokestatic io/putIntLn(I)V
Label19:
Label16:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label15
Label17:
Label14:
Label5:
.var 1 is c I from Label20 to Label21
Label20:
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label21:
	goto Label1
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
