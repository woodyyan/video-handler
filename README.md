使用方式：
1. 把composition和splice函数部署为同步函数，其他配置和原来一样。
2. 把此函数部署为异步函数，其他配置上面的函数一样。
3. 传入下面的JSON进行调用。

调用方式：

```jsx
{
    "Data": {
        "Videos": [
            {
                "Data": {
                    "Input": {
                        "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/%E7%89%87%E5%A4%B4.mp4",
                        "Audio": true,
                        "CallbackURL": "",
                        "Resolution": {
                            "Width": 720,
                            "Height": 1280
                        },
                        "Framerate": 15,
                        "Bitrate": 1800,
                        "Texts": [],
                        "Pictures": []
                    },
                    "Output": {
                        "Vod": {
                            "Region": "ap-beijing",
                            "SubAppId": 1500009267,
                            "ClassId": 873369
                        }
                    }
                }
            },
            {
                "Data": {
                    "Input": {
                        "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/%E7%89%87%E5%A4%B4.mp4",
                        "Audio": true,
                        "CallbackURL": "",
                        "Resolution": {
                            "Width": 720,
                            "Height": 1280
                        },
                        "Framerate": 15,
                        "Bitrate": 1800,
                        "Texts": [],
                        "Pictures": []
                    },
                    "Output": {
                        "Vod": {
                            "Region": "ap-beijing",
                            "SubAppId": 1500009267,
                            "ClassId": 873369
                        }
                    }
                }
            },
            {
                "Data": {
                    "Input": {
                        "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/3%E5%AE%9E%E6%93%8D8%E7%A7%92%E7%A4%BA%E4%BE%8B.MP4",
                        "Audio": true,
                        "CallbackURL": "",
                        "Resolution": {
                            "Width": 720,
                            "Height": 1280
                        },
                        "Framerate": 15,
                        "Bitrate": 1800,
                        "Texts": [
                            {
                                "Content": "作品名称：包装动画制作-缩放",
                                "X": "(w-text_w)/2",
                                "Y": "(h-text_h)/5",
                                "Size": 30
                            },
                            {
                                "Content": "一米阳光的创作过程",
                                "X": "(w-text_w)/2",
                                "Y": "(h-text_h)/5*4",
                                "Size": 24
                            },
                            {
                                "Content": "2022.1.24",
                                "X": "(w-text_w)/2",
                                "Y": "h/5*4+text_h",
                                "Size": 24
                            }
                        ],
                        "Pictures": [
                            {
                                "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/logo.png",
                                "X": "(W-w)/2",
                                "Y": "(H-h)/7",
                                "Width": 168,
                                "Height": 55
                            },
                            {
                                "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/%E5%AD%A6%E5%91%98%E5%A4%B4%E5%83%8F.jpg",
                                "X": "(W-w)/2",
                                "Y": "(H-h-h*2)",
                                "Width": 50,
                                "Height": 50
                            }
                        ]
                    },
                    "Output": {
                        "Vod": {
                            "Region": "ap-beijing",
                            "SubAppId": 1500009267,
                            "ClassId": 873369
                        }
                    }
                }
            },
            {
                "Data": {
                    "Input": {
                        "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/5%E6%88%90%E6%9E%9C%E8%A7%86%E9%A2%91%E7%A4%BA%E4%BE%8B.mp4",
                        "Audio": true,
                        "CallbackURL": "",
                        "Resolution": {
                            "Width": 720,
                            "Height": 1280
                        },
                        "Framerate": 15,
                        "Bitrate": 1800,
                        "Texts": [],
                        "Pictures": []
                    },
                    "Output": {
                        "Vod": {
                            "Region": "ap-beijing",
                            "SubAppId": 1500009267,
                            "ClassId": 873369
                        }
                    }
                }
            },
            {
                "Data": {
                    "Input": {
                        "URL": "http://1500009267.vod2.myqcloud.com/6c9c6980vodcq1500009267/0d7032f3387702294461673432/pz3wNIkIjCEA.mp4",
                        "Audio": true,
                        "CallbackURL": "",
                        "Resolution": {
                            "Width": 720,
                            "Height": 1280
                        },
                        "Framerate": 15,
                        "Bitrate": 1800,
                        "Texts": [
                            {
                                "Content": "作品名称：包装动画制作-缩放",
                                "X": "(w-text_w)/2",
                                "Y": "(h-text_h)/5",
                                "Size": 30
                            },
                            {
                                "Content": "一米阳光的创作过程",
                                "X": "(w-text_w)/2",
                                "Y": "(h-text_h)/5*4",
                                "Size": 24
                            },
                            {
                                "Content": "2022.1.19",
                                "X": "(w-text_w)/2",
                                "Y": "h/5*4+text_h",
                                "Size": 24
                            }
                        ],
                        "Pictures": [
                            {
                                "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/logo.png",
                                "X": "(W-w)/2",
                                "Y": "(H-h)/7",
                                "Width": 168,
                                "Height": 55
                            },
                            {
                                "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/%E5%AD%A6%E5%91%98%E5%A4%B4%E5%83%8F.jpg",
                                "X": "(W-w)/2",
                                "Y": "(H-h-h*2)",
                                "Width": 50,
                                "Height": 50
                            }
                        ]
                    },
                    "Output": {
                        "Vod": {
                            "Region": "ap-beijing",
                            "SubAppId": 1500009267,
                            "ClassId": 873369
                        }
                    }
                }
            },
            {
                "Action": "CompositionVideo",
                "Data": {
                    "Input": {
                        "URL": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/6%E6%89%8B%E6%9C%BA%E7%AB%AF%E7%89%87%E5%B0%BE.MP4",
                        "Audio": true,
                        "CallbackURL": "",
                        "Resolution": {
                            "Width": 720,
                            "Height": 1280
                        },
                        "Framerate": 15,
                        "Bitrate": 1800,
                        "Texts": [],
                        "Pictures": []
                    },
                    "Output": {
                        "Vod": {
                            "Region": "ap-beijing",
                            "SubAppId": 1500009267,
                            "ClassId": 873369
                        }
                    }
                }
            }
        ],
        "Audio": "https://woody-chengdu-1307427535.cos.ap-chengdu.myqcloud.com/shifang/22.mp3",
        "CallbackURL": "https://enk885gn0j1qox.m.pipedream.net",
        "Output": {
            "Vod": {
                "Region": "ap-beijing",
                "SubAppId": 1500009267,
                "ClassId": 873369
            }
        }
    }
}
```