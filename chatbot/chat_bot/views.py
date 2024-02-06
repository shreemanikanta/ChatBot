from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.
openai_api_key = ''
# openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'meaage': message, 'response': response})
    return render(request, 'chatbot.html')