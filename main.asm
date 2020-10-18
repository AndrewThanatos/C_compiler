.data
	Caption1 db "Andrew Berezhniuk", 0
	buf dw ? 
	a dword 0, 0 
	b dword 0, 0 

.code 
otherfunc proc 
	mov eax, 5 
	push eax 
	mov eax, 3 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop dword ptr [a] 
	pop eax 
	mov eax, 6 
	push eax 
	mov eax, 3 
	push eax 
	pop eax 
	pop ebx 
	xor edx, edx 
	div ebx 
	push eax 
	pop dword ptr [b] 
	pop eax 
	push dword ptr [a] 
	push dword ptr [b] 
	pop eax 
	mov ebx, -1 
	imul eax, ebx 
	push eax 
	pop ebx 
	pop eax 
	add eax, ebx 
	push eax 
	pop eax 
	fn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK 
	ret 
otherfunc endp 
