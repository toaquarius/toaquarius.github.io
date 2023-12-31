#-*-coding:utf-8
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IS_REAL                 =  False if os.environ['DEV'] == 'Y' else True 
SITE_URL                = "https://toaquarius.github.io"
SITE_NAME               = "toaquarius" 
SITE_DESC               = "물병자리의 주인"
SITE_KIND               = "BOOK" #BOOK
KEYWORDS                = "물병자리 책 리뷰" #BLOG 
ADSENSE_CLIENT          = 'ca-pub-3309468445717403'
ADSENSE_SEARCH          = 'partner-pub-3309468445717403:scakuetu6bz'
ANALYTICS_GTAG          = 'G-4JX9MZGVD0'
DB_INFO                 = os.getenv('DB_INFO').split('|')
DB_HOST	                = DB_INFO[0]
DB_USER	                = DB_INFO[1]
DB_PW 		            = DB_INFO[2]
DB_SID 		            = DB_INFO[3]
NV_INFO                 = os.getenv('NV_CENTER_API').split('|')
NV_API_CID 	            = NV_INFO[0]
NV_API_SID 	            = NV_INFO[1]

print("################ py.setting.config.py 시작")
print("SITE_URL : ", SITE_URL)
print("SITE_NAME : ", SITE_NAME)
print("SITE_DESC : ", SITE_DESC)
print("SITE_KIND : ", SITE_KIND)
print("KEYWORDS : ", KEYWORDS)
print("ADSENSE_CLIENT : ", ADSENSE_CLIENT)
print("ADSENSE_SEARCH : ", ADSENSE_SEARCH)
print("################ py.setting.config.py 끝")

