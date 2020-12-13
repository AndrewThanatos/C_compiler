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
	b_2 dword 0, 0 
	num1_4 dword 0, 0 
	num2_5 dword 0, 0 
	sum_6 dword 0, 0 
	bigger_7 dword 0, 0 
	i_8 dword 0, 0 

.code 
otherfunc proc 
mov eax 14push eaxpop dword ptr [num1]mov eax 15push eaxpop dword ptr [num2]	jmp __main_start 
 __max_start: 
	push dword ptr [a_1] 
	push dword ptr [b_2] 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jg _true_1 
	mov eax, 0 
 _true_1: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_1 
	push dword ptr [a_1] 
	jmp _else_end_1
 _else_1: 
	push dword ptr [b_2] 
 _else_end_1: 
	jmp __max_end
 __max_end: 
	jmp _resume_

 __main_start: 
	mov eax, 15 
	push eax 
	pop dword ptr [num1_4] 
	mov eax, 14 
	push eax 
	pop dword ptr [num2_5] 
	mov eax, 0 
	push eax 
	pop dword ptr [sum_6] 
	push dword ptr [num1_4] 
	pop dword ptr [a_1] 
	push dword ptr [num2_5] 
	pop dword ptr [b_2] 
	jmp __max_start
 _resume_0: 
	push dword ptr [func_count] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [func_count] 
	pop dword ptr [bigger_7] 
	mov eax, 1 
	push eax 
	pop dword ptr [i_8] 
 _loop_condition_2: 
	push dword ptr [i_8] 
	push dword ptr [bigger_7] 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	jle _true_2 
	mov eax, 0 
 _true_2: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _loop_end_2 
	push dword ptr [bigger_7] 
	push dword ptr [i_8] 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push edx 
	mov eax, 0 
	push eax 
	pop eax 
	pop ebx 
	cmp ebx, eax 
	mov eax, 1 
	je _true_3 
	mov eax, 0 
 _true_3: 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_3 
	push dword ptr [sum_6] 
	push dword ptr [i_8] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [sum_6] 
 _else_3: 
	push dword ptr [i_8] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [i_8] 
	jmp _loop_condition_2
 _loop_end_2: 
	push dword ptr [sum_6] 
	jmp __main_end
 __main_end: 

	pop eax 
	jmp _output__ 

 _resume_: 
	push dword ptr [func_count]
	pop eax 
	cmp eax, 0 
	jz _resume_0 
 _output__: 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
