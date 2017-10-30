#!/usr/bin/env python
import requests as _requests
requests = _requests.Session()
# Request URL:http://classic-blog.udn.com/article/post.jsp

# f_MAIN_ID: uz
# f_SUB_ID: uz1
# f_ART_CATE: 1701321
# f_ART_TITLE: 测试1
# f_ART_ICON: udn001.gif
# f_ART_BODY: 测试2
# f_MEDIA_CODE:
# f_IS_TRACK: Y
# f_TRACK_URL:
# f_ART_TEMPLATE: 1
# f_IS_PUBLISH: N
# rand_numx: 9
# rand_numy: 2
# post_key:
# f_fun: ADD
# f_ART_ID: 0
# f_SUB_ART_CATE: 0
# f_PHOTO_IDS:
# f_POST_CHECK: 999
# f_PUBLISH_DATE:
# xid: gnaWnauygneM

headers = {
    "Cookie": """UdnCasId=w0Z1+VZyW3BbUsZCOODZnL-r; TGT=TGT-2391-UvkSdzHJyL5IrMi4bHmyoNjNHLnT1N7PXOccN11dMroKhBcUzW-cas; nickname=%A4%FD%A9%73%B7%BD; udnmember=MengyuanWang; um2=2%23010%220ddbd10%2B0%22ad0%2B0%220d4%233%2B313%2F3b33313d333%2F33323d30%21%3D; udnemail=0%23010%220ddbd10%2B0%22d%224d0%2B0%220d2%2F0d0%230%2B0b0%24d%22030%210%23%21%3D; membercenter=2%23010%220ddbd10%2B0%22ad0%2B0%220d; syncsns=U; _ga=GA1.2.1355523867.1509357275; _gid=GA1.2.1394502940.1509357297; haslogin=MengyuanWang; logindate=2017%2F10%2F30; isactive=Y; __utmt=1; __asc=1ddcc70b15f6d633fb5e5e8888e; __auc=a6c50b2f15f6cb449f306b0fe9b; __utma=175200637.1355523867.1509357275.1509366006.1509368742.3; __utmb=175200637.90.10.1509368742; __utmc=175200637; __utmz=175200637.1509357275.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"""
}


# <span class="main-text">檢核碼：</span><input type="text" name="rand_numx" id="rand_numx" size="1" value="4" readonly="true"> + <input type="text" name="rand_numy" id="rand_numy" size="1" value="4" readonly="true"> = <input type="text" name="post_key" id="post_key" size="1" maxlength="2" value="" onBlur="javascript:post_check(jQuery('#rand_numx').val(), jQuery('#rand_numy').val(), jQuery('#post_key').val());">


def main():
    page = requests.get(
        "http://classic-blog.udn.com/article/post.jsp", headers=headers
    )
    print(page.content)
    pass


if __name__ == "__main__":
    main()
