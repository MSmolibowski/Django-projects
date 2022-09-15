import re

def count_words(seq, word_size):
		d = {
				"words"  : [],
				"counts" : [],
				"percent" : [],
				"index_to_show" : [],
				
		}


		

		seq = seq.replace('\n', '').replace('\r', '') # usuniecie znakow nowej linii i \r

		
		
		#word_sum = sum("counts")

		for i in range(0, len(seq)-word_size+1):
				word = seq[i:i+word_size]

				if word not in d["words"]:


						d["words"].append(word)
						d["counts"].append(0)
						d["percent"].append(0)
						

				el_index = d["words"].index(word)
				d["counts"][el_index] += 1



						
		all_words = sum(d["counts"]) #calkowita ilosc slow

		number_of_words = len(d["words"])

		
		#print(number_of_words)
	
		d["index_to_show"] = list(range(0,number_of_words))
		

	 # print(word_count)
		#print(d)
		for j in range(0,number_of_words):
			d["percent"][j] = round((d["counts"][j]/all_words)*100,2)

		#print(d)
		
		check = sum(d["percent"])
		print(check)
		
		return d