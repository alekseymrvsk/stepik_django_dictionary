from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "home.html")


def words(request):
    words_list = []
    try:
        file = open("file.txt", "r").read().splitlines()
        words_list = []
        for line in file:
            print(line)
            word1, word2 = line.split("-")
            words_list.append((word1, word2))
            print(words_list)
    except:
        pass

    # return words_orig, words_trans
    return render(request=request, template_name="words.html", context={"words": words_list})


def add_word(request):
    # if request.method == "GET":
    #     return render(request, "add_word.html")
    if request.method == "POST":
        if type(request.POST['word_orig']) is type(request.POST['word_trans']) is str:
            with open("file.txt", "a") as file:
                file.write(request.POST['word_orig'] + "-" + request.POST['word_trans'])
            return redirect(index)
    return render(request, "add_word.html")
