.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static m [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass/m [I
	iconst_1
	iconst_1
	isub
	iconst_5
	iastore
	getstatic MPClass/m [I
	iconst_1
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 1
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
	bipush 10
	newarray int
	putstatic MPClass.m [I
	return
.limit stack 1
.limit locals 0
.end method
