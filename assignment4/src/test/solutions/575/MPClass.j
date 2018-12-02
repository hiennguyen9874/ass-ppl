.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 100
	ineg
	istore_1
Label2:
	iload_1
	bipush 100
	if_icmpgt Label4
	iconst_0
	istore_1
Label5:
	iload_1
	bipush 100
	if_icmpgt Label7
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
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
