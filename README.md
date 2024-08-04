# CPL-Tool
計算機程式助教專用的 Online Judge 自動化工具。
## 使用步驟說明
1. 將學生名單(學號)以 excel 格式放置於資料夾內
2. 請確認帳號的權限為 Super Admin
3. 安裝相關套件 (requirement.txt 待補)
4. 執行時輸入 OJ 的部分域名(bach / mozart / ...)，以及帳號密碼
5. 成功執行後，只須按照 command line 上給的指示，選擇要使用的功能
## 實作內容簡介
### 前置作業
- open_chrome_driver.py: 使用 selenium 套件模擬瀏覽器登入
- CPL_login.py: 登入以取得權限
- copy_cookies.py: 登入後改用 requests 套件，以提升效率
- OJ_API.py: 將 API request 封裝，以利其他函數調用
### 主要功能
- CPL_students.py: 讀取學生名單
- CPL_contest.py: 統計成績、下載競賽題目、下載程式碼提交紀錄 (皆與 contest 相關)
- CPL_user.py: 批量停用或啟用帳號、生成考試專用的帳號密碼(皆與 user 相關)
### 資料夾
- excel: 讀取學生名單、儲存成績紀錄、儲存帳密檔案
- problems: 儲存競賽題目
- submissions: 儲存程式碼提交紀錄
## 參數設定
1. contest_id: 點進 contest 頁面後，可從網址得知 id
2. user_id: 從後台 -> General -> User 即可得知。需輸入兩個數字，代表批量處理的範圍。
3. postfix: 生成考試專用帳號時的後綴
