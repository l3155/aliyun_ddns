#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author  张军军[zhangjunjun@aactechnologies.com]
@version
@since

-------------------------------------------------
日期   张军军 [Init]      初始化
-------------------------------------------------

说明
"""
import json
import urllib.request as url_request
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def get_local_ip():
    ip = json.loads(
        url_request.urlopen('www.jsonip.com').read().decode('utf-8')
    )['ip']
    return ip


class AliApi:
    def __init__(self):
        self.client = AcsClient(
            '',
            '',
            ''
        )
        self.request = CommonRequest()
        self.request.set_domain('alidns.aliyuncs.com')
        self.request.set_version('2015-01-09')

    def get_domain_recorded_ip(self, domain_name):
        self.request.set_action_name('DescribeDomainRecords')
        self.request.add_query_param('DomainName', domain_name)
        response = self.client.do_action_with_exception(self.request)
        record = json.loads(response.decode('utf-8'))['DomainRecords']['Record']
        return record[0]['Value']

    def update_domain_record_ip(self, new_value):
        self.request.set_action_name('UpdateDomainRecord')
        self.request.add_query_param('RecordId', '17233251617867776')
        self.request.add_query_param('RR', 'www')
        self.request.add_query_param('Type', 'A')
        self.request.add_query_param('Value', new_value)
        response = self.client.do_action_with_exception(self.request)
        print(response)


if __name__ == '__main__':
    local_ip = get_local_ip()
    ali = AliApi()
    record_ip = ali.get_domain_recorded_ip('muzg.cn')
    if local_ip != record_ip:
        ali.update_domain_record_ip(local_ip)
