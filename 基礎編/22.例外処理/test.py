#try, except, finally
# def exception_test(value_1, value_2):
 
#     print('＝＝＝＝計算開始＝＝＝＝')
 
#     result = 0
 
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算出来ませんでした！')
#     finally:
#         print('計算終了')
 
#     return result
     
 
# print(exception_test(100, 200))
# print(exception_test(100, '200'))

#raise
# def exception_test(value_1, value_2):
 
#     print('＝＝＝＝計算開始＝＝＝＝')
 
#     result = 0
 
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算出来ませんでした！')
#         raise
#     finally:
#         print('計算終了')
 
#     return result
 
 
# try:
#     print(exception_test(100, 100))
#     print(exception_test(200, 200))
#     print(exception_test(300, '300'))
# except:
#     print('エラーを受け取りました')

#エラー内容（スタックトレース）の取得
import sys
import traceback
 
def exception_test(value_1, value_2):
 
    print('＝＝＝＝計算開始＝＝＝＝')
 
    result = 0
 
    try:
        result = value_1 + value_2
    except:
        print('計算出来ませんでした！')
        raise
    finally:
        print('計算終了')
 
    return result
     
 
try:
    print(exception_test(100, '200'))
except:
    print('---------------------------------------')
    print(traceback.format_exc(sys.exc_info()[2]))
    print('---------------------------------------')