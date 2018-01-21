# -*- coding: utf-8 -*-
"""
@author: ruchenshanghai
"""
from splinter.browser import Browser
from time import sleep
import traceback
import time, sys


class huoche(object):
    """docstring for huoche"""
    driver_name = ''
    executable_path = ''
    # 用户名，密码
    username = u""
    passwd = u""
    # cookies值得自己去找, 下面两个分别是成都东, 深圳东
    starts = u"%u6210%u90FD%u4E1C%2CICW"
    ends = u"%u6DF1%u5733%u4E1C%2CBJQ"
    # 时间格式2018-01-19
    dtime = u"2018-02-19"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 0
    ###乘客名
    users = [u"陈光芬", u"黄大安"]
    ##席位
    xb = u"硬座"
    pz = u"成人票"

    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    login_url = 'https://kyfw.12306.cn/otn/login/init'

    def __init__(self):
        self.driver_name = 'chrome'
        self.executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print u"等待验证码，自行输入..."
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break

    def start(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(1400, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print u"购票页面开始..."
            # sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})

            self.driver.reload()

            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print u"循环点击查询... 第 %s 次" % count
                    # sleep(1)

                    hardSeatID = 'YZ_76000K10940A'
                    hardSleepID = 'YW_76000K10940A'
                    if (cmp(self.driver.find_by_id(hardSeatID).first.text, u"无") == 0):
                        # if (cmp(self.driver.find_by_id(hardSeatID).first.text, u"无") == 0 and
                        # 		cmp(self.driver.find_by_id(hardSleepID).first.text, u"无")== 0):
                        print "不满足席位条件"
                    else:
                        print "OK"
                        try:
                            self.driver.find_by_text(u"预订")[self.order - 1].click()
                        except Exception as e:
                            print e
                            print u"还没开始预订"
                            continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print u"循环点击查询... 第 %s 次" % count
                    # sleep(0.8)
                    hardSeatID = 'YZ_76000K10940A'
                    hardSleepID = 'YW_76000K10940A'
                    if (cmp(self.driver.find_by_id(hardSeatID).first.text, u"无") == 0):
                        # if (cmp(self.driver.find_by_id(hardSeatID).first.text, u"无") == 0 and
                        # 		cmp(self.driver.find_by_id(hardSleepID).first.text, u"无")== 0):
                        print "不满足席位条件"
                    else:
                        print "ok"
                        try:
                            for i in self.driver.find_by_text(u"预订"):
                                i.click()
                                sleep(1)
                        except Exception as e:
                            print e
                            print u"还没开始预订 %s" % count
                            continue
            print u"开始预订..."
            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print u'开始选择用户...'
            for user in self.users:
                self.driver.find_by_text(user).last.click()

            print u"提交订单..."
            sleep(1)
            self.driver.find_by_text(self.pz).click()
            # self.driver.find_by_id('').select(self.pz)
            sleep(1)
            # self.driver.find_by_text(self.xb).click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            # print u"开始选座..."
            # self.driver.find_by_id('1D').last.click()
            # self.driver.find_by_id('1F').last.click()

            sleep(1.5)
            print u"确认选座..."
            self.driver.find_by_id('qr_submit_id').click()

        except Exception as e:
            print e


if __name__ == '__main__':
    huoche = huoche()
    huoche.start()
