.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "bat dau if"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	ifle Label2
	ldc "Dung"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "Sai"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
	ldc "ket thuc if"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
