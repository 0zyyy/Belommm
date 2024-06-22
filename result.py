import requests
import time
import json
import random
import brotli
import sys
from loguru import logger
import datetime

# Setup logger
logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <level>{message}</level>")

def send_request(url, headers, method='GET', params=None):
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
    except Exception as e:
        logger.error("Terjadi kesalahan saat permintaan: {}", e)
        return None

# Hàm xử lý token và thực hiện yêu cầu
def process_tokens(token, url, method='GET', index=None):
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        'Authorization': f'Bearer {token}',
        "Content-Type": "application/json",
        "Origin": "https://telegram.blum.codes",
        "Referer": "https://telegram.blum.codes/",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    data = send_request(url, headers, method)
    if index is not None:
        logger.info(f"Blum {index}: {data}")
    else:
        logger.info(f"Response: {data}")

def process_response(response):
    if response.headers.get('Content-Encoding') == 'br':
        decompressed_data = brotli.decompress(response.content)
        return decompressed_data.decode('utf-8')
    else:
        return response.text

# Hàm lấy token mới từ refresh token
def get_new_tokens(refresh_token):
    url = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
    payload = {"query": refresh_token}
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://telegram.blum.codes"
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if 'token' in response_data and 'access' in response_data['token']:
            return response_data['token']['access']
        else:
            logger.error("Token tidak ditemukan dalam respons : {}", response_data)
            return None
    else:
        logger.error("Gagal mendapatkan token baru, kode status : {}, respons: {}", response.status_code, response.text)
        return None

def get_current_ip():
    response = requests.get("http://ifconfig.me/ip")
    return response.text.strip()

def check_license(token, device):
    url = "https://f88group.my.id/api/check_license.php"
    params = {"token": token, "device": device}
    response = requests.get(url, params=params)
    return response.json()

def hitung_durasi(expired_at):
    expiry_date_obj = datetime.datetime.strptime(expired_at, "%Y-%m-%d %H:%M:%S")
    current_time = datetime.datetime.now()
    time_difference = expiry_date_obj - current_time
    remaining_days = time_difference.days
    remaining_hours = time_difference.seconds // 3600
    return [remaining_days, remaining_hours]

# Hàm chính
def main():
    print("==============================")
    print("-                            -")
    print("- Bot Auto Claim Play Daily  -")
    print("-       Author ADFMIDN       -")
    print("-                            -")
    print("==============================")
    print("")

    # Membaca dan menghitung jumlah akun di data.txt
    with open('data.txt', 'r') as file:
        refresh_tokens = [line.strip() for line in file if line.strip()]
        print(f"Jumlah akun : {len(refresh_tokens)}")
        print("")

    # Set these options to True to enable them automatically
    enable_auto_play = True
    enable_auto_task = False

    while True:
        try:
            if not refresh_tokens:
                continue
            for index, refresh_token in enumerate(refresh_tokens, start=1):
                access_token = get_new_tokens(refresh_token)
                if not access_token:
                    continue

                headers = {
                    'Authorization': f'Bearer {access_token}',
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Content-Type": "application/json",
                    "Origin": "https://telegram.blum.codes",
                    "Referer": "https://telegram.blum.codes/",
                    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                }

                blum_balance = 'https://game-domain.blum.codes/api/v1/user/balance'
                blum_claim_url = 'https://game-domain.blum.codes/api/v1/farming/claim'
                blum_farming_url = 'https://game-domain.blum.codes/api/v1/farming/start'
                daily_reward_url = 'https://game-domain.blum.codes/api/v1/daily-reward'
                daily_reward = "https://game-domain.blum.codes/api/v1/daily-reward?offset=-420"
                play_url = "https://game-domain.blum.codes/api/v1/game/play"
                tasks_url = "https://game-domain.blum.codes/api/v1/tasks"
                friend_url = "https://gateway.blum.codes/v1/friends/balance"
                params = {'offset': -420}

                response = requests.get(daily_reward_url, headers=headers, params=params)
                if response.status_code == 200:
                    response = requests.post(daily_reward, headers=headers)
                    logger.info(f'Blum {index} - Balance : {available_balance}')
                else:
                    pass

                response_balance = send_request(blum_balance, headers=headers)

                if enable_auto_play:
                    if response_balance and "playPasses" in response_balance:
                        play_passes = int(response_balance["playPasses"])
                        for _ in range(play_passes):
                            try:
                                response_play = requests.post(play_url, headers=headers)

                                if response_play.status_code == 200:
                                    logger.info("Bermain game....")
                                    game_id = response_play.json().get("gameId")
                                    time.sleep(30)

                                    if game_id:
                                        # URL for the second API call
                                        claim_url = "https://game-domain.blum.codes/api/v1/game/claim"

                                        # Payload for the second request
                                        points = random.randint(65584, 965584)
                                        logger.info("Mencoba mengklaim poin : {}", points)  # Debug: Cetak poin yang akan diklaim
                                        payload_claim = {"gameId": game_id, "points": str(points)}

                                        # Make the second POST request
                                        response_claim =  requests.post(claim_url, json=payload_claim, headers=headers)

                                        if response_claim.status_code == 200:
                                            logger.info("Klaim berhasil : {}", points)  # Cetak poin yang berhasil diklaim
                                        else:
                                            logger.error("Gagal mengklaim : {}", response_claim.text)  # Cetak kesalahan jika ada
                            except:
                                pass

                # Check balance and farming status
                if 'availableBalance' in response_balance:
                    available_balance = response_balance['availableBalance']
                    logger.info(f"Blum {index} - Balance : {available_balance}")

                try:
                    data = response_balance
                    if 'farming' not in response_balance:
                        process_tokens(access_token, blum_farming_url, method='POST', index=index)
                    balance = float(data["farming"]["balance"])
                    if balance >= 57:
                        try:
                            process_tokens(access_token, blum_claim_url, method='POST', index=index)
                            process_tokens(access_token, blum_farming_url, method='POST', index=index)
                        except:
                            process_tokens(access_token, blum_farming_url, method='POST', index=index)
                except:
                    pass

                try:
                    friend_claim = requests.get(friend_url, headers=headers)
                    freind = json.loads(friend_claim.text)
                    canClaim = freind.get("canClaim", False)
                    if canClaim:
                        claim_url = "https://gateway.blum.codes/v1/friends/claim"
                        response = requests.post(claim_url, headers=headers)
                except:
                    pass

                if enable_auto_task:
                    try:
                        tasks = requests.get(tasks_url, headers=headers)
                        tasklist = json.loads(tasks.text)

                        if tasklist:
                            try:
                                for task in tasklist:
                                    task_id = task["id"]
                                    title = task["title"]
                                    reward = task["reward"]
                                    if task["status"] == "NOT_STARTED":
                                        if task_id == ["d057e7b7-69d3-4c15-bef3-b300f9fb7e31", "a90d8b81-0974-47f1-bb00-807463433bde"]:
                                            if "progressTarget" in task:
                                                progress = float(task["progressTarget"]["progress"])
                                                target = float(task["progressTarget"]["target"])
                                                if progress < target:
                                                    continue  # Skip this task
                                        else:
                                            pass
                                        task_start_url = f"https://game-domain.blum.codes/api/v1/tasks/{task_id}/start"
                                        response_start = requests.post(task_start_url, headers=headers)
                                        logger.info(f"Tugas {title} dimulai")
                                    else:
                                        pass

                                    if task["status"] == "DONE":
                                        task_claim_url = f"https://game-domain.blum.codes/api/v1/tasks/{task_id}/claim"
                                        response_claim = requests.post(task_claim_url, headers=headers)
                                        logger.info(f"Tugas {title} diklaim: {reward}")

                            except Exception as e:
                                logger.error(f"Kesalahan : {e}")
                    except requests.RequestException as e:
                        logger.error(f"Terjadi Kesalahan : {e}")
                    except:
                        pass

                logger.info('-' * 20)

        except Exception as e:
            logger.error("Kesalahan: {}", e)

if __name__ == "__main__":
    main()