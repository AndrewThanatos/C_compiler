.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 
	a dword 0, 0 
	b dword 0, 0 

.code 
otherfunc proc 
	mov eax, 3 
	push eax 
	pop dword ptr [a] 
	pop eax 
	mov eax, 4 
	push eax 
	pop dword ptr [b] 
	pop eax 
	push dword ptr [a] 
	mov eax, 1 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	push dword ptr [b] 
	mov eax, 3 
	push eax 
	pop ebx 
	pop eax 
	imul eax, ebx 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a] 
	pop eax 
	push dword ptr [a] 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
