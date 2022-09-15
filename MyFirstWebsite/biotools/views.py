from django.shortcuts import render

from .forms import SeqContentForm, Transcript_SeqContentForm

from . import utils



def seqcontent_view(request):
    if request.method == "POST":
        form = SeqContentForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            word_size = form.cleaned_data['word_size']
            
            seq_length = len(seq); #zmienna do długosci seq

            d = utils.count_words(seq, word_size)
            return render(request, 'biotools/seqcontent.html', {'results': d, 'length' : seq_length})
    else:
        form = SeqContentForm()
    return render(request, 'biotools/seqcontent.html', {'form': form})

def transcript_seq_view(request):
    if request.method == "POST":
        
        form = Transcript_SeqContentForm(request.POST)

        if form.is_valid():
            seq = form.cleaned_data['sequence']   

            rev = form.transcript()
            return render(request, 'biotools/revcomp.html', {'rev': rev, 'seq' : seq})
    else:
        form = Transcript_SeqContentForm()
        
    return render(request, 'biotools/revcomp.html', {'form': form})

    