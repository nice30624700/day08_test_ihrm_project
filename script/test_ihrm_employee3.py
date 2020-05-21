import loggingimport unittestimport requestsimport appfrom api.employee_api import TestEmplyeeApifrom utils import assert_commonclass TestIHRMEmployee3(unittest.TestCase):    # 方法级别    def setUp(self):        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"        self.emp_api = TestEmplyeeApi()    # 编写测试函数    def test01_login(self):        # 登录        response = requests.post(url=self.login_url, json={"mobile": "13800000002", "password": "123456"})        # 打印登录的数据        # print("登录的结果为:", response.json().get("message"))        # 提取令牌        token = response.json().get('data')        # 保存令牌到请求头当中        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}        app.HEADERS = headers        # 断言        assert_common(self, 200, True, 10000, "操作成功", response)    # 添加员工    def test02_add_emp(self):        response = self.emp_api.add_emp(app.HEADERS, "莱布尼兹", "136200000011")        logging.info("添加员工的结果为:{}".format(response.json()))        # 断言        assert_common(self, 200, True, 10000, "操作成功", response)        # 获取员工id        emp_id = response.json().get("data").get("id")        app.EMP_ID = emp_id        # 断言        assert_common(self, 200, True, 10000, "操作成功",response)    # 查询员工    def test03_query_emp(self):        # 发送查询员工的请求        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)        logging.info("添加员工的结果为:{}".format(response.json()))        # 断言        assert_common(self, 200, True, 10000, "操作成功", response)    # 修改员工    def test04_modify_emp(self):        response = self.emp_api.modify_emp(app.EMP_ID, "小天才", app.HEADERS)        logging.info("修改员工的结果为:{}".format(response.json()))        # 断言        assert_common(self, 200, True, 10000, "操作成功", response)    # 删除员工    def test05_delete_emp(self):        # 发送删除员工的请求        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)        # 打印删除的结果        logging.info("删除的结果为:{}".format(response.json()))        # 断言        assert_common(self, 200, True, 10000, "操作成功", response)