# 封装公共断言方法
def common_assert(case,response,status_code,success,code,message):
    # 断言
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(success, response.json().get("success"))
    case.assertEqual(code, response.json().get("code"))
    case.assertIn(message, response.json().get("message"))