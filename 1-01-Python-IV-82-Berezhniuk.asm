.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 
	b dword 0, 0 
	a dword 0, 0 

.code 
otherfunc proc 
	push dword ptr [b] 
	pop eax 
	mov eax, 4 
	push eax 
	pop dword ptr [b] 
	pop eax 
	mov eax, 3 
	push eax 
	push dword ptr [b] 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a] 
	pop eax 
	push dword ptr [a] 
	mov eax, 3 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
