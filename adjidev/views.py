from django.shortcuts import render, redirect  
from adjidev.forms import KelasForm, AbstractForm  
from adjidev.models import Kelas, Abstract 
from adjidev import Preproses


# kelas keilmuan manajemen.
def kelasAdd(request):
    if request.method == "POST":  
        form = KelasForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('kelas/')  
            except:  
                pass  
    else:  
        form = KelasForm()  
    return render(request, 'kelas/add.html',{'form':form})  
    
def kelasIndex(request):  
    kelas = Kelas.objects.all()  
    return render(request, "kelas/index.html",{'kelas':kelas})

def editKelas(request, id):  
    kelas = Kelas.objects.get(id=id)    
    return render(request, "kelas/edit.html",{'kelas':kelas})

def updateKelas(request, id):  
    kelas = Kelas.objects.get(id=id)  
    form = KelasForm(request.POST, instance = kelas)  
    if form.is_valid():  
        form.save()  
        return redirect("/kelas/")  
    return render(request, 'kelas/edit.html', {'kelas': kelas})

def destroyKelas(request, id):  
    kelas = Kelas.objects.get(id=id)  
    kelas.delete()  
    return redirect("/kelas/")  

#abstract manajemen
def indexAbstract(request):
    abstracts = Abstract.objects.all()  
    return render(request, "abstract/index.html", {
            'abstracts': abstracts
        })

def addAbstract(request):
    kelases = Kelas.objects.all()
    if request.method == "POST":  
        form = AbstractForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/abstract/')  
            except:  
                pass  
    else:  
        form = AbstractForm()
    return render(request, "abstract/add.html", {
                'kelases': kelases,
                'form': form
            })

def editAbstract(request, id):  
    abstract = Abstract.objects.get(id=id)
    kelases = Kelas.objects.all()    
    return render(request, "abstract/edit.html",{
                'abstract': abstract, 
                'kelases':kelases
            })

def preproses(request, id):
    abstract = Abstract.objects.get(id=id)
    lower = Preproses.text_lowercase(abstract.abstract)
    remove_numbers = Preproses.remove_numbers(lower)
    remove_punctuation = Preproses.remove_punctuation(remove_numbers)
    remove_whitespace = Preproses.remove_whitespace(remove_punctuation)
    remove_stopwords = Preproses.remove_stopwords(remove_whitespace)
    lemmatize_word = Preproses.lemmatize_word(remove_whitespace)
    return render(request, "abstract/preproses.html",{
                'abstract': abstract, 
                'lower':lower,
                'remove_numbers': remove_numbers,
                'remove_punctuation': remove_punctuation,
                'remove_whitespace': remove_whitespace,
                'remove_stopwords': remove_stopwords,
                'lemmatize_word': lemmatize_word
            })

def updateAbstract(request, id):  
    abstract = Abstract.objects.get(id=id)  
    kelases = Kelas.objects.all()  
    form =AbstractForm(request.POST, instance = abstract)  
    if form.is_valid():  
        form.save()  
        return redirect("/abstract/")  
    return render(request, 'abstract/edit.html', {'abstract': abstract, 'kelases': kelases})



