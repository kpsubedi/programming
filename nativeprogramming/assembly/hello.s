# gcc -c hello.s 
# ld hello.o
# ./a.out
#

    .global _start

    .text

_start: 
    # write(1, message, 28)
    mov $1, %rax
    mov $1, %rdi
    mov $message, %rsi
    mov $28, %rdx
    syscall

    mov $60, %rax
    xor %rdi, %rdi
    syscall

message:
    .ascii "Welcome to Digital Forensic\n"
