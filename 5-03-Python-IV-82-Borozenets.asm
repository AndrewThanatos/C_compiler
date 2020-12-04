.586
.model flat, stdcall

option casemap: none

include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
include \masm32\include\windows.inc
include \masm32\include\masm32rt.inc

includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib


.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 
	func_count dword 0, 0 
	a_1 dword 0, 0 

.code 
otherfunc proc 
	jmp __main_start 
 __fib_start: 
	push dword ptr [a_1] 
	mov eax, 1 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_1 
	mov eax, 0 
 _true_1: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_1 
	mov eax, 1 
	push eax 
	jmp __fib_end
 _else_1: 
	push dword ptr [a_1] 
	mov eax, 0 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_2 
	mov eax, 0 
 _true_2: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_2 
	mov eax, 0 
	push eax 
	jmp __fib_end
 _else_2: 
	push dword ptr [a_1] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	pop dword ptr [a_1] 
	jmp __fib_start
 _resume_0: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	push dword ptr [a_1] 
	mov eax, 2 
	push eax 
	pop ebx 
	pop eax 
	sub eax, ebx 
	push eax 
	pop dword ptr [a_1] 
	jmp __fib_start
 _resume_1: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	jmp __fib_end
 __fib_end: 
	jmp _resume_

 __main_start: 
	mov eax, 5 
	push eax 
	pop dword ptr [a_1] 
	jmp __fib_start
 _resume_2: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	jmp __main_end
 __main_end: 

	pop eax 
	jmp _output__ 

 _resume_: 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 0 
	jz _resume_0 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 1 
	jz _resume_1 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 2 
	jz _resume_2 
 _output__: 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
