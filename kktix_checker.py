import requests
import os

# 從 GitHub Secrets 讀取 Token 和 User ID
CHANNEL_TOKEN = os.getenv('LINE_CHANNEL_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')
KKTIX_URL = 'https://kktix.com/events/c36e1c56/registrations/new'

def send_line_push(text):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {CHANNEL_TOKEN}',
    }
    payload = {
        'to': USER_ID,
        'messages': [{'type': 'text', 'text': text}]
    }
    r = requests.post(url, headers=headers, json=payload)
    print('LINE Push 回傳：', r.status_code, r.text)

def check_ticket():
    try:
        response = requests.get(KKTIX_URL)
        if response.status_code == 200:
            print('KKTIX 網頁成功讀取')
            send_line_push('【KKTIX票券檢查】已檢查票券，請手動確認網站。')
        else:
            print('KKTIX 網頁讀取失敗')
            send_line_push('【KKTIX票券檢查】網站讀取失敗，請檢查。')
    except Exception as e:
        print('發生錯誤：', e)
        send_line_push(f'【KKTIX票券檢查】發生錯誤：{e}')

if __name__ == '__main__':
    check_ticket()
