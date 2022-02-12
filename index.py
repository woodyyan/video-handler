import json
import logging
import sys
from multiprocessing.dummy import Pool as ThreadPool

import requests

# 日志配置
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def main_handler(event, context):
    logger.info("start main handler")
    request_id = context.get('request_id')

    if "body" not in event.keys():
        return {"code": 410, "errorMsg": "event is not come from api gateway"}

    req_body = event['body']
    req_param = json.loads(req_body)
    logger.info("输入参数: " + json.dumps(req_param))
    videos = req_param['Data']['Videos']
    audio = req_param['Data']['Audio']
    callback_url = req_param['Data']['CallbackURL']
    vod_region = req_param['Data']['Output']['Vod']['Region']
    sub_app_id = req_param['Data']['Output']['Vod']['SubAppId']
    class_id = req_param['Data']['Output']['Vod']['ClassId']

    param_list = []
    for video in videos:
        json_str = json.dumps(video)
        print(json_str)
        param_list.append(json_str)

    pool = ThreadPool(6)
    results = pool.map(process, param_list)
    print(results)
    pool.close()
    pool.join()

    urls = []
    logger.info("开始拼接视频")
    for result in results:
        result_str = result.decode("utf-8")
        print(result_str)
        result_json = json.loads(result_str)
        print(result_json)
        if 'Failure' in result_json:
            return result_json
        url = result_json['Data']['OutputUrl']
        urls.append(url)
    splice_data = {
        "Action": "SpliceVideo",
        "Data": {
            "Input": {
                "URLs": urls,
                "Audio": audio,
                "Transitions": "None",
                "CallbackURL": callback_url
            },
            "Output": {
                "Vod": {
                    "Region": vod_region,
                    "SubAppId": sub_app_id,
                    "ClassId": class_id
                }
            }
        }
    }
    print(splice_data)
    return splice_data


def process(param_json):
    response = requests.post(
        'https://service-ngvp1ppd-1307427535.cd.apigw.tencentcs.com/release/shifang-ffmpeg-composition-sync',
        data=param_json)
    print(response.content)
    return response.text.encode('utf8')

