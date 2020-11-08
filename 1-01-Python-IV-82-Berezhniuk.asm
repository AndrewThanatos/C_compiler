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
	a1 dword 0, 0 

.code 
otherfunc proc 
	mov eax, 3 
	push eax 
	pop dword ptr [a1] 
	mov eax, 0 
	push eax 
	pop eax 
	cmp eax, 0 
	jz _else_1 
	mov eax, 15 
	push eax 
	pop dword ptr [a1] 
 _else_1: 
	mov eax, 25 
	push eax 
	pop dword ptr [a1] 
	push dword ptr [a1] 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 


main:
	invoke otherfunc
	invoke ExitProcess, 0
end main
