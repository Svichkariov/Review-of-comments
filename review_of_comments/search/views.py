from django.shortcuts import render
import requests
from bs4 import BeautifulSoup



headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

search_star = {1: '— Жуть!', 2: '— Ниже среднего', 3: '— Средне', 4: '— Хорошо', 5: '— Отлично!'}
store_name = {
    1: 'https://936.shop.onliner.by/reviews',
    2: 'https://707.shop.onliner.by/reviews',
    3: 'https://197.shop.onliner.by/reviews',
    4: 'https://585.shop.onliner.by/reviews',
    5: 'https://3886.shop.onliner.by/reviews'
}
number = int
quantity_comments = int
page = int
star = int
response_to_comment = int



def home(request):
    return render(request, 'home.html', {'title': 'Профиль'})


def setup(request):
    parameters=[]
    if request.method == "POST"\
            and request.POST.get('number')\
            and request.POST.get('quantity_comments')\
            and request.POST.get('page')\
            and request.POST.get('star'):
        number = int(request.POST.get('number'))
        quantity_comments = int(request.POST.get('quantity_comments'))
        page = int(request.POST.get('page'))+1
        star = int(request.POST.get('star'))
        if request.POST.get('response_to_comment'):
            response_to_comment = int(request.POST.get('response_to_comment'))
        else:
            response_to_comment = 0


        if response_to_comment == 1:
            parameters.append('с ответом продавца')
        else:
            parameters.append('Ответ продавца отсуствует')

        for j in search_star:
            if star == j:
                parameters.append(search_star[j])


        url = f'{store_name[number]}'
        response = requests.get(url=url, headers=headers)
        bs = BeautifulSoup(response.text, "lxml")
        store = bs.find("h1",
                        class_="catalog-form__title catalog-form__title_base catalog-form__title_nocondensed catalog-form__title_condensed-additional").text.strip()
        rating = bs.find("div", class_="catalog-grade__digit").text.strip()
        total_reviews = bs.find("div",
                                class_="catalog-form__description catalog-form__description_other catalog-form__description_base").text.strip()

        n = 1
        comment_all = {}
        answer_seller_all = {}
        for x in range(1, page):
            if parameters[0] == 'с ответом продавца':
                url = f'{store_name[number]}?has_reply=1&page={x}'
            else:
                url = f'{store_name[number]}?page={x}'
            response = requests.get(url=url, headers=headers)
            bs = BeautifulSoup(response.text, "lxml")
            titles = bs.find_all("div", class_="catalog-form__reviews-unit")


            for title in titles:
                comment_star = title.find("span", class_="catalog-form__rating-count").text.strip()
                for argument in parameters:
                    if comment_star == argument and n <= quantity_comments:
                        comment = title.find("div",
                                             class_="catalog-form__description catalog-form__description_primary catalog-form__description_base-alter catalog-form__description_condensed-default catalog-form__description_multiline").text.strip()
                        comment_all[n] = comment
                        if parameters[0] == 'с ответом продавца':
                            answer_seller = title.find("div", class_="catalog-form__comment").text.strip()
                            answer_seller_all[comment] = answer_seller
                        else:
                            answer_seller_all[comment] = 'Ответ продавца отсуствует'

                        n += 1


            if n - 1 == quantity_comments:
                break

        if n < quantity_comments:
            search_completed = 1
        elif n - 1 == quantity_comments:
            search_completed = 0



        return render(request, 'result.html',
                      {'store': store,
                       'star': star,
                       'comment_star': comment_star,
                       'rating': rating,
                       'total_reviews': total_reviews,
                       'n': n-1,
                       'answer_seller_all': answer_seller_all,
                       'search_completed': search_completed,
                       'quantity_comments': quantity_comments})
    return render(request, 'setup.html')
