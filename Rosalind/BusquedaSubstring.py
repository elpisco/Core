cadena1 = 'TTAACAGAGAAGCACATCCAAGCACAAAGCACAATAAGCACATCACATAACGGAAGCACACGGAAGCACAACCGTTAAGCACACTCAAGCACAGGAAGCACATAGTAAAGCACAAAGCACAGTTTAAAGCACAAAGTCAAGCACATGGAAGCACATAAGCACAAAGCACAGAAGCACAAAAGCACAAAGCACAGAAGCACACTAAGCACAGCCTTTGAAGCACAAAGCACAAAAGCACACTAAGCACAAATTTGGAAGCACAGCACAAGCACACAAGCACACAAGCACAAAGCACACAAAAGCACAGGAAGCACAAAGCACATGAAGCACAATTGAAGCACAATAAAGCACATCCAAGCACATATATTGTCAAAGCACAAACAAGCACAACATGATTAAGCACAAAGCACAACAAGCACAGTTCAAGCACACGTAAGCACACTAAAAAGCACAAAGCACACAAGCACAATAAAGCACAAGTAAGCACATGTTAGAGGAACATTTAGAAGTTAGACACCAAGCACAGGAAGCACAATAAATTCACGCGGAAGCACATTGTCAAAGCACAACAAAGCACAAAGCACAGCAAGCACAGGCAAGCACACAAAGCACACATTAAAAGCACAACGCTCAAGCACAAGAAGCACAAAGCACAAAGCACAGTAAGCACAAAGCACACGCAAGCACACAAGCACAACCAGTTAAGCACACGGCAAGCACAAAGCACAAAGCACAACGAAAGCACAAAAAGCACAACAAGCACACGAAAGCACAAAGCACACAAGCACAGAGGAAGCACATGAAGCACATGCGGCCAAGCACAAAGCACATCAGGGATGTAAGCACAAAGCACAAGAAGCACAAAGCACAGGTTGCCAAGCACATAAGCACACAAGCACATTACAAGCACAAATTCGAAGCACAAAGCACAGAAGCACAAAGCACAAAGCACACTTAAAGCACATAAGCACACAGA'
cadena2 ='AAGCACAAA'
salida = ''
for i in range(len(cadena1)):
	j=0
	ini = 0
	fin=0
	st=''
	if cadena1[i]==cadena2[0]:
		ini = i
		st = cadena1[i]
		j=i+1
		k=1;
		while j<len(cadena1) and k<len(cadena2) and cadena1[j]==cadena2[k]:
			st = st + cadena1[j]
			j=j+1
			k=k+1
		fin = j
		if st == cadena2:
			salida = salida + str(ini+1) + ' '
			
print salida
