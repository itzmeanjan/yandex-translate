# yandex-translate
Yandex Translate Service python API


**'yandex-translate' helps you to use Yandex.Translate Service from your python program.

You can simply use it in your python script as below :: 



 *Example usage of 'get_lang_list' :

``` 
 from get_lang_list import get_langs
 
 
 # argument 2, resp_lang, is one of the supported languages by Yandex.Translate, in which you would like to get the response
 # don't make any changes to base_url, which has got a default value
 
 resp = get_langs('put-your-api-key-here', 'en')
 print(resp)
 
```


 *Example usage of 'detect_lang' :

``` 
 from detect_lang import detect_lang
 
 
 #hint will be given first priority while detecting language of provided text, needs to be put in form of list
 #base_url argument has got a default value which needs no change unless someday Yandex.Translate API endpoint changes 
 #hint is not compulsory to provide, but good to provide to get a result faster
 
 resp = detect_lang('put-your-api-key-here', 'put the text you want to detect here', hint = ['en', 'ru'])
 print(resp)
 
```

Response will be a python dictionary, because this program uses Yandex.Translate's JSON API end and which gets converted to a python dict by using json.loads() 


You can get your free api key at this [link]<https://passport.yandex.com/auth?origin=translate&retpath=https%3A%2F%2Ftranslate.yandex.com%2Fdevelopers%2Fkeys> .


Thanks goes to Yandex.Translate because everything in backend is [***powered by Yandex.Translate.]<http://translate.yandex.com/>


Well you can read Terms of Use [here]<https://translate.yandex.com/developers/offer> .


Hope it was helpful.
