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
	a_1 dword 0, 0 
	a_2 dword 0, 0 
	a_4 dword 0, 0 
	b_5 dword 0, 0 

.code 
otherfunc proc 
	mov eax, 0 
	push eax 
	pop dword ptr [a_4] 
	pop eax 
	mov eax, 0 
	push eax 
	pop dword ptr [b_5] 
	pop eax 
	push dword ptr [a_4] 
	pop dword ptr [a_1] 
	mov eax, 1 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_1 
	push dword ptr [a_2] 
	mov eax, 100000 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	jmp _sum_end
 _else_1: 
	mov eax, 0 
	push eax 
	jmp _sum_end
 _sum_end: 
	pop dword ptr [a_4] 
	pop eax 
	mov eax, 1 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_2 
	push dword ptr [a_4] 
	mov eax, 10 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_4] 
	pop eax 
	jmp _else_end_2
 _else_2: 
	push dword ptr [a_4] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a_4] 
	pop eax 
 _else_end_2: 
	mov eax, 0 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_3 
	mov eax, 10 
	push eax 
	pop dword ptr [b_5] 
	pop eax 
	jmp _else_end_3
 _else_3: 
	mov eax, 100 
	push eax 
	pop dword ptr [b_5] 
	pop eax 
 _else_end_3: 
	push dword ptr [a_4] 
	push dword ptr [b_5] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	jmp _main_end
 _main_end: 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
