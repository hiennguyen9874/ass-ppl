.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static arr [I

.method public static searchArr([III)I
.var 0 is d [I from Label0 to Label1
	iconst_5
	newarray int
	astore_0
.var 1 is a I from Label0 to Label1
.var 2 is n I from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_3
Label2:
	iload_3
	iload_2
	if_icmpgt Label4
	aload_0
	iload_3
	iconst_1
	isub
	iload_3
	iastore
Label3:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label4:
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is j I from Label0 to Label1
.var 2 is result I from Label0 to Label1
Label0:
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iconst_5
	iastore
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iconst_3
	iastore
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	bipush 11
	iastore
	getstatic MPClass/arr [I
	iconst_4
	iconst_1
	isub
	bipush 19
	iastore
	getstatic MPClass/arr [I
	iconst_5
	iconst_1
	isub
	bipush 20
	iastore
	getstatic MPClass/arr [I
	iconst_3
	iconst_5
	invokestatic MPClass/searchArr([III)I
	istore_2
	iload_2
	invokestatic io/putInt(I)V
	goto Label1
Label1:
	return
.limit stack 3
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

.method public static <clinit>()V
	iconst_5
	newarray int
	putstatic MPClass.arr [I
	return
.limit stack 1
.limit locals 0
.end method
