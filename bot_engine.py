import time
import threading
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from selenium.webdriver.common.proxy import Proxy, ProxyType
from ip_manager import renew_tor_ip
from log_store import log
import os

def launch_bot(video_link, screen_count, like_option):
    threads = []
    for i in range(screen_count):
        t = threading.Thread(target=watch_reel, args=(video_link, like_option, i+1))
        threads.append(t)
        t.start()
        time.sleep(random.uniform(2, 4))
    for t in threads:
        t.join()

def watch_reel(video_link, like_option, screen_id):
    log(screen_id, "⏳ Launching with new TOR IP...")
    renew_tor_ip()

    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')

    driver = webdriver.Chrome(options=chrome_options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        driver.get(video_link)
        log(screen_id, "▶️ Watching reel...")
        simulate_human(driver)

        for watch_num in range(2):
            log(screen_id, f"👁️ Watch {watch_num+1}")
            time.sleep(random.uniform(20, 40))

            if like_option == "on":
                try:
                    like_button = driver.find_element(By.XPATH, "//span[@aria-label='Like']")
                    ActionChains(driver).move_to_element(like_button).pause(random.uniform(1, 2)).click().perform()
                    log(screen_id, "❤️ Liked the reel.")
                except Exception as e:
                    log(screen_id, f"⚠️ Like failed: {e}")

        log(screen_id, "🔁 Refreshing screen...")

        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/screen_{screen_id}.png")
        log(screen_id, "📸 Screenshot saved.")

    except Exception as e:
        log(screen_id, f"❌ Error: {e}")
    finally:
        driver.quit()
        log(screen_id, "✅ Closed screen.")

    

    try:
        driver.get(video_link)
        log(screen_id, "▶️ Watching reel...")
        simulate_human(driver)

        for watch_num in range(2):
            log(screen_id, f"👁️ Watch {watch_num+1}")
            time.sleep(random.uniform(20, 40))

            if like_option == "on":
                try:
                    like_button = driver.find_element(By.XPATH, "//span[@aria-label='Like']")
                    ActionChains(driver).move_to_element(like_button).pause(random.uniform(1, 2)).click().perform()
                    log(screen_id, "❤️ Liked the reel.")
                except Exception as e:
                    log(screen_id, f"⚠️ Like failed: {e}")

        log(screen_id, "🔁 Refreshing screen...")

        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/screen_{screen_id}.png")
        log(screen_id, "📸 Screenshot saved.")

    except Exception as e:
        log(screen_id, f"❌ Error: {e}")
    finally:
        driver.quit()
        log(screen_id, "✅ Closed screen.")

def simulate_human(driver):
    for _ in range(random.randint(1, 3)):
        scroll_y = random.randint(100, 500)
        driver.execute_script(f"window.scrollBy(0, {scroll_y});")
        time.sleep(random.uniform(1, 2))