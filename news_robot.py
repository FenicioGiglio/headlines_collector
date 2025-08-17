import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By # Importa o By para localizar elementos
from selenium.webdriver.common.keys import Keys # Importa Keys para simular pressionamento de teclas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configurações do Chrome
user_data_path = r"C:\Users\fenic\AppData\Local\Google\Chrome\User Data\Default" # Caminho para o perfil do usuário
profile_name = "Default" # Nome do perfil do Chrome
options = uc.ChromeOptions()
options.add_argument(f"--user-data-dir={user_data_path}") # Define o caminho do perfil
options.add_argument(f"--profile-directory={profile_name}") # Define o nome do perfil
options.add_argument("--headless=new") # Executa o Chrome em modo headless (sem interface gráfica)

# Driver
driver = uc.Chrome(options=options, version_main=139)

# Abrindo o site do Globo
news_url = "https://g1.globo.com/"
driver.get(news_url)

# Encontrando as manchetes
wait = WebDriverWait(driver, 15)
news_elements_list = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "bstn-hl-wrapper")))

print(f"Encontradas {len(news_elements_list)} manchetes. Coletando títulos e links...")
print("-" * 30)

all_news = []

# Extraindo títulos e links
for news_element in news_elements_list:
    title = news_element.text
    link = news_element.find_element(By.TAG_NAME, "a").get_attribute("href")

    if title and link:
        print(f"\n Título: {title}")
        print(f"Link: {link} \n")
        print("-" * 30)

        all_news.append({
            "title": title,
            "link": link
        })

# Fechando o navegador
driver.quit()
