.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is iSum I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iload_3
	istore_2
	iload_2
	istore_1
Label2:
	iload_1
	bipush 20
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore_2
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
	iload_2
	iload_1
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	bipush 10
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	goto Label7
Label12:
	iload_2
	iconst_2
	irem
	iconst_1
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	goto Label6
Label15:
	iload_3
	iload_2
	iadd
	istore_3
	goto Label6
Label7:
	iload_1
	iload_2
	irem
	iconst_0
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label2
Label18:
	iload_1
	iload_2
	iadd
	bipush 40
	if_icmple Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label21
	goto Label3
Label21:
	iload_3
	iload_1
	iadd
	istore_3
	goto Label2
Label3:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 4
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
