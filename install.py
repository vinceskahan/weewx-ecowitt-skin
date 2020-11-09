
# installer for the ecowitt skin extension

from setup import ExtensionInstaller

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version="0.1",
            name='ecowitt',
            description='ecowitt minimalist custom skin',
            author="Vince Skahan",
            author_email="vinceskahan@gmail.com",
            config={
                'StdReport': {
                    'ecowitt': {
                        'skin': 'ecowitt',
                        'HTML_ROOT': 'ecowitt'
                        }
                }
            },
            files=[
                 ('skins/ecowitt',
                    [
                        'skins/ecowitt/index.html.tmpl',
                        'skins/ecowitt/mystyle.css',
                        'skins/ecowitt/skin.conf'
                    ],
                 ),
            ]
        )
