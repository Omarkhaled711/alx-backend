# 0x02. i18n

Flask-Babel is utilized for localization, enabling dynamic customization of content such as language and date based on the user's location.

## Notes

The provided scripts use an older version of Flask-Babel (== 2.0.0), as well as outdated versions of Flask and Jinja2. The ALX checker is configured with these specific versions. When testing with newer versions, such as Flask-Babel 4.0.0 and the latest Flask and Jinja2 releases, the following adjustments are necessary:

### In babel.cfg

It is recommended to comment out the 'extensions' line, as it is no longer required in newer versions of Jinja2. Including this line may result in an error.

```ini
[python: **.py]
[jinja2: **/templates/**.html]
;extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

### Code Changes

Remove the @babel.localeselector and @babel.timezoneselector decorators. Instead, initialize Babel within your application after defining get_locale() and get_timezone() methods:

``` python
def get_locale():
    # logic for obtaining the locale

def get_timezone():
    # logic for obtaining the timezone

babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)
```

These adjustments ensure compatibility with newer versions of the mentioned libraries
