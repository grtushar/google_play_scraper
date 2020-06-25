# google_play_scraper
An updated version of google [play scraper](https://github.com/danieliu/play-scraper) with the additional permission list information retrieving capability.

The permission information of an app in the google play store resides inside a modal window. That's why the permission information doesn't exist in the initial html. Also It's not a real link, it does not redirect to another page as classic a tags would (it doesn't have the href attribute anyway). Instead, there is a listener somewhere that opens a popup when the user click on the "View details" under the permission category.Therefore, the google play scraper can't fetch the permission data.

This updated version of google [play scraper](https://github.com/danieliu/play-scraper) perform the click event on the "view details" under permission category using [selenium](https://pypi.org/project/selenium/) and [chrome-driver](https://chromedriver.chromium.org/)

###Usage
Configure the variables in the [permission_info.py](https://github.com/grtushar/google_play_scraper/blob/master/play_scraper/permission_info.py) in order to run this.
[Download](https://chromedriver.chromium.org/downloads) the chrome-driver and then set the *CHROME_DRIVER_PATH* variable of permission_info.py file with the path of the chrome-driver.

Sometimes the information doesn't load, so there is a retry mechanism. You can limit the max retry by setting *MAX_ATTEMPT* variable to your desired retry count.

In addition, to give some time to chrome to load the data of the url the program sleeps for sometime. You can also configure the sleep interval depending on your internet speed by setting the required value *TIME_TO_LOAD_DATE_IN_SECOND* and *TIME_TO_LOAD_MODAL_DATA_IN_SECOND* variables inside the permission_info.py file.
