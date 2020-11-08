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
	flag1 dword 0, 0 
	cnt1 dword 0, 0 
	b2 dword 0, 0 
	c3 dword 0, 0 

.code 
otherfunc proc 
	mov eax, 0 
	push eax 
	pop dword ptr [flag1] 
	mov eax, 100 
	push eax 
	pop dword ptr [cnt1] 
	push dword ptr [flag1] 
	pop eax 
	cmp eax, 0 
	jz _else_1 
	mov eax, 13 
	push eax 
	pop dword ptr [b2] 
	mov eax, 2 
	push eax 
	push dword ptr [b2] 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	pop dword ptr [c3] 
	push dword ptr [b2] 
 _else_1: 
	push dword ptr [cnt1] 
	mov eax, 4 
	push eax 
	pop ebx 
	pop eax 
	cdq 
	idiv ebx 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
