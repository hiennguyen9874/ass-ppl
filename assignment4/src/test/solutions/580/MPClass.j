.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static searchArr([III)I
.var 0 is m [I from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is n I from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
.var 4 is i I from Label2 to Label4
Label2:
	iconst_5
	newarray int
	iconst_0
	istore 4
Label3:
	iload 4
	iconst_5
	if_icmpge Label4
	dup
	iload 4
	aload_0
	iload 4
	iaload
	iastore
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label3
Label4:
	astore_0
	iconst_1
	istore_3
Label5:
	iload_3
	iload_2
	if_icmpgt Label7
	aload_0
	iload_3
	iconst_1
	isub
	iaload
	iload_1
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iload_3
	goto Label1
Label10:
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label5
Label7:
	iconst_1
	ineg
	goto Label1
Label1:
	ireturn
.limit stack 5
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is j I from Label0 to Label1
.var 2 is result I from Label0 to Label1
.var 3 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	astore_3
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpgt Label4
	aload_3
	iload_1
	iconst_1
	isub
	iload_1
	iconst_1
	iadd
	iastore
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	aload_3
	iconst_3
	iconst_5
	invokestatic MPClass/searchArr([III)I
	istore_2
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
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
