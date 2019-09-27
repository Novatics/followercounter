# followercounter

## Under Construction

![Under construction](https://thumbs.gfycat.com/JoyfulAfraidAltiplanochinchillamouse-small.gif)

You will be able to get your follower counter for the social medias:

- [x] Youtube
- [ ] Twitter
- [ ] Instagram

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install followercounter.

```bash
pip install followercounter
```

## Usage

```python
from followercounter import youtube, instagram, twitter

# Get your Youtube Key on https://console.developers.google.com on "Google Data Api v3"
youtube('<YOUR__KEY>', 'studiom4') # returns '205312'
instagram('<access_token>') # returns '1334'
twitter('novatics') # returns '130'
```

### Getting your access_token for Instagram

To get the `access_token` first you need to register an application [here](https://www.instagram.com/developer/) and then follow the instructions [here](https://www.instagram.com/developer/authentication/) to authorize your application to access your profile data

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### Setup environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running tests
```bash
python -m pytest tests/
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
