import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'index.html')


def get_settings(request):
    if request.method == 'POST':
        try:
            # Извлекаем данные из JSON тела POST-запроса
            data = json.loads(request.body)
            idInstance = data.get('idInstance')
            apiTokenInstance = data.get('apiTokenInstance')

            # Формируем URL на основе полученных данных
            url = f"https://7103.api.greenapi.com/waInstance{idInstance}/getSettings/{apiTokenInstance}"

            # Выполняем GET-запрос к API
            response = requests.get(url)
            response_data = response.json()  # Предполагаем, что ответ приходит в формате JSON
        except requests.exceptions.RequestException as e:
            response_data = {"error": str(e)}
        except json.JSONDecodeError:
            response_data = {"error": "Invalid JSON"}

        # Возвращаем ответ в формате JSON
        return JsonResponse(response_data)

    return JsonResponse({"error": "Invalid request method"}, status=400)


def get_state_instance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idInstance = data.get('idInstance')
            apiTokenInstance = data.get('apiTokenInstance')
            url = f"https://7103.api.greenapi.com/waInstance{idInstance}/getStateInstance/{apiTokenInstance}"
            response = requests.get(url)
            response_data = response.json()
        except requests.exceptions.RequestException as e:
            response_data = {"error": str(e)}
        except json.JSONDecodeError:
            response_data = {"error": "Invalid JSON"}

        return JsonResponse(response_data)

    return JsonResponse({"error": "Invalid request method"}, status=400)


def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idInstance = data.get('idInstance')
            apiTokenInstance = data.get('apiTokenInstance')
            chatId = data.get('phoneNumber')  # Добавляем @c.us к chatId
            message = data.get('message')
            url = f"https://7103.api.greenapi.com/waInstance{idInstance}/sendMessage/{apiTokenInstance}"
            payload = {
                "chatId": f"{str(chatId).strip()}@c.us",
                "message": message
            }

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()
        except requests.exceptions.RequestException as e:
            response_data = {"error": str(e)}
        except json.JSONDecodeError:
            response_data = {"error": "Invalid JSON"}

        return JsonResponse(response_data)

    return JsonResponse({"error": "Invalid request method"}, status=400)


def send_file_by_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idInstance = data.get('idInstance')
            apiTokenInstance = data.get('apiTokenInstance')
            chatId = data.get('phoneNumberFile')
            fileUrl = data.get('fileUrl')
            caption = data.get('caption', '')  # Необязательный параметр

            if not isinstance(chatId, str):
                return JsonResponse({"error": "'chatId' must be a string"}, status=400)

            # chatId = chatId.strip() + "@c.us"  # Убедитесь, что chatId не None и добавьте @c.us

            if not isinstance(fileUrl, str):
                return JsonResponse({"error": "'fileUrl' must be a string"}, status=400)

            url = f"https://7103.api.greenapi.com/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"

            payload = {
                "chatId": f"{str(chatId).strip()}@c.us",
                "urlFile": fileUrl,
                "fileName": "ffjsknfs",
            }

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()
        except requests.exceptions.RequestException as e:
            response_data = {"error": str(e)}
        except json.JSONDecodeError:
            response_data = {"error": "Invalid JSON"}

        return JsonResponse(response_data)

    return JsonResponse({"error": "Invalid request method"}, status=400)

