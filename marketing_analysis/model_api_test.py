import requests

result = requests.post('http://127.0.0.1:5000/', {
    'text': 'Я пойду гулять',
    'image': '',
    'social': 1,
    'url': 'https://vk.com/fusionism'
})

print(result)