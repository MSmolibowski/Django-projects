from django import forms


class SeqContentForm(forms.Form):
	sequence = forms.CharField(
		widget=forms.Textarea(attrs={
			'placeholder': 'Plain sequence',
			'class': 'form-control'
			}),
		min_length=5,
		required=True)
	word_size = forms.IntegerField(
		initial=1,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)



	def clean_sequence(self):
		sequence = self.cleaned_data['sequence']

		new_seq = ''

		switcher = 1

		for nt in sequence:
			if nt == '>':
				switcher = 0
			if nt == '\n':
				switcher = 1
			
			if switcher == 1:
				new_seq += nt

		sequence = new_seq

		return sequence.upper()

	def clean_word_size(self):
		word_size = self.cleaned_data['word_size']
		if word_size < 1:
			raise forms.ValidationError('Word size must be >= 1')
		return word_size




	def clean(self):
		sequence = self.cleaned_data.get('sequence')
		word_size = self.cleaned_data.get('word_size')
        # Only do something if both fields are valid so far
		if sequence and word_size:
			if len(sequence) < word_size:
				raise forms.ValidationError('Sequence cannot be shorter than word size')




class Transcript_SeqContentForm(forms.Form):
	sequence = forms.CharField(
		widget=forms.Textarea(attrs={
			'placeholder': 'Plain sequence',
			'class': 'form-control'
			}),
		min_length=5,
		required=True)


	def clean_sequence(self):
		sequence = self.cleaned_data['sequence']

		new_seq = ''

		switcher = 1

		for nt in sequence:
			if nt == '>':
				switcher = 0
			if nt == '\n':
				switcher = 1
			
			if switcher == 1:
				new_seq += nt

		sequence = new_seq

		return sequence.upper()


	
	def transcript(self):
		sequence = self.cleaned_data['sequence']

		rev_seq = ' '

		for i in range(0,len(sequence)):
			if sequence[i] == 'A':
				rev_seq += 'T'
			if sequence[i] == 'T':
				rev_seq+= 'A'
			if sequence[i] == 'C':
				rev_seq+= 'G'
			if sequence[i] == 'G':
				rev_seq+= 'C'
			if sequence[i] == '\n':
				rev_seq+='\n'

		return rev_seq 

	

	
	



