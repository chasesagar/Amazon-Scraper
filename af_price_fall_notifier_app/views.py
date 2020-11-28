from django.shortcuts import render
from django.contrib import messages   # for error messages
from script import scriptAmazon, scriptSelenium # import of external scraping scripts
# Create your views here.

def HomePageView(request):
    if request.method == 'POST':
        URL = request.POST.get('actualurl')
        print(URL)
        # beautifulsoup script call and recording result
        result_amazon = scriptAmazon(URL) #calling external amazon scraping script which is based upon beautifulsoup
        result_amazon_price = result_amazon[0]
        result_amazon_description = result_amazon[1]

        #selenium script call and recroding results
        result_selenium = scriptSelenium(URL)
        result_selenium_min = result_selenium[0]
        result_selenium_avg = result_selenium[1]
        result_selenium_max = result_selenium[2]
        return render( request, "index.html")
    else:
        return render(request, "home.html ")

def ResPageView(request):
    return render( request, "index.html")

# def RevcompPageView(request):
#     if request.method == 'POST':
#         xseq = request.POST.get('sequence')
        
#         xoption = request.POST.get('option')

#         my_dna = validateseq(xseq)
#         if my_dna == "error":
#             messages.info(request, 'Only DNA sequence allowed')
#             return render(request, "rev_comp.html")
        
#         else:
#             if xoption == "1":
#                 rev = reverse(my_dna[0])
#                 return render(request, "rev_comp_result.html",{
#                     'seq':my_dna[0] ,
#                     'reverse':rev ,
#                 })
#             elif xoption == "2":
#                 comp = complement(my_dna[0])
#                 return render(request, "rev_comp_result.html",{
#                     'seq':my_dna[0] ,
#                     'comp':comp ,
#                 })
#             elif xoption == "3":
#                 revcomp = reverse_complement(my_dna[0])
#                 return render(request, "rev_comp_result.html",{
#                     'seq':my_dna[0] ,
#                     'revcomp':revcomp ,
#                 })
#             else:
#                 rev = reverse(my_dna[0])
#                 comp = complement(my_dna[0])
#                 revcomp = reverse_complement(my_dna[0])
#                 return render(request, "rev_comp_result.html",{
#                     'seq':my_dna[0] ,
#                     'comp':comp ,
#                     'reverse':rev ,
#                     'revcomp':revcomp ,
#                 })
#     else:
#          return render( request, "rev_comp.html")
