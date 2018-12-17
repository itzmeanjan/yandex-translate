# yandex_translate
 Yandex.Translate Service python API


**'yandex_translate' helps you to use Yandex.Translate Service from your python script. Make sure you use python3**


 ## You can simply use it in your python script as below :: 



 ### Example usage of 'get_lang_list' :


``` 
 from yandex_translate.get_lang_list import get_langs
 
 '''
    argument 2, resp_lang, is one of the supported languages by Yandex.Translate, in which you would like to get the response, which is 'en' by default
    don't make any changes to base_url, which has got a default value
'''

 print(get_langs('put-your-api-key-here', 'en'))
 
```



 ### Example usage of 'detect_lang' :


``` 
 from yandex_translate.detect_lang import detect_lang
 

 '''
    hint will be given first priority while detecting language of provided text, needs to be put in form of list
    base_url argument has got a default value which needs no change unless someday Yandex.Translate API endpoint changes 
    hint is not compulsory to provide, but good to provide to get a result faster
 '''

 print(detect_lang('put-your-api-key-here', 'put the text you want to detect here', hint = ['en', 'ru']))
 
```



### Example usage of 'translate' :


``` 
 from yandex_translate.translate import translate 
 
 '''
    This function performs a post query at yandex translate and returns a python dict, holding response.
    If a blank dict gets returned, some error has occurred.
    
    format paramter has got a default value of 'plain', can also be 'html', 
    in that case make you that you pass a html string as text parameter.
    
    text to translate needs to be lesser than 10000 characters for post query
'''
 
 print(translate('put-your-api-key-here', 'put the text you want to detect here', 'en-ru'))
 
```



**New Files Added ::**



#### push_into_db.push(db_name, data) :

    - pushes lang_codes, received on execution of get_lang_list.get_langs() into levelDB.
    - local levelDB is named 'lang_codes', by default.
    - data to be pushed into database, needs to be in python dict format.



#### check_lang_code.check_code(db_name, code) :

    - checks whether code is supported by Yandex.Translate or not.
    - if yes, returns true else returns false.



Response will be a python dictionary, because this program uses Yandex.Translate's JSON API end and which gets converted to a python dict .


Even in occurrence of unexpected error, a dict will be returned, holding possible cause of error.


You can find more info on powerful key-value based database **levelDB** [here](http://leveldb.org/). I'm using python interface [plyvel](https://plyvel.readthedocs.io/en/latest/index.html) for accessing levelDB features.


You can get your free api key [here](https://passport.yandex.com/auth?origin=translate&retpath=https%3A%2F%2Ftranslate.yandex.com%2Fdevelopers%2Fkeys), which has some usage limitation.



Thanks to Yandex.Translate because everything in backend is [**powered by Yandex.Translate**](http://translate.yandex.com/).



Well you can read Terms of Use [here](https://translate.yandex.com/developers/offer).



**Hope it was helpful.**
