.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static searchArr([II)[I
.var 0 is d [I from Label0 to Label1
	iconst_5
	newarray int
	astore_0
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_2
Label2:
	iload_2
	iload_1
	if_icmpgt Label4
	aload_0
	iload_2
	iconst_1
	isub
	iload_2
	iastore
Label3:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label4:
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	astore_1
Label0:
	aload_1
	iconst_5
	invokestatic MPClass/searchArr([II)[I
	iconst_1
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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
