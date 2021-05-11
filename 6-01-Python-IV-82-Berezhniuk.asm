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
	Text db "Andrew Berezhniuk", 0
	buf dw ? 
	fc dword 0, 0 
	h705_1 dword 0, 0 
	h430_2 dword 0, 0 

.code 
fnc proc 
	jmp __mst 
 __h137_start: 
	mov eax, 19 
	push eax 
	pop dword ptr [h705_1] 
	mov eax, 4 
	push eax 
	pop dword ptr [h430_2] 
	push dword ptr [h705_1] 
	push dword ptr [h430_2] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [h705_1] 
	push dword ptr [h705_1] 
	jmp __h137_end
 __h137_end: 
	jmp _rs_

	pop eax 
	jmp _ot_ 

 _rs_: 
 _ot_: 
	fn MessageBox, 0, str$(eax), ADDR Text, MB_OK 
	ret 
fnc endp 


mn:
	invoke fnc
	invoke ExitProcess, 0
end mn
